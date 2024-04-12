import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .KincoServoDriver import ServoController
from arm_interfaces.msg import SensorData, MotorCmd, AppParams
from arm_interfaces.srv import SensorFeedback

class ApplicationNode(Node,ServoController):

    def __init__(self,port,baudrate,timeout):
        super().__init__("application_node")
        self.controller = ServoController(port,baudrate,timeout)
        # Create subscribers for each sensor topic
        # self.sensor_data_sub = self.create_subscription(SensorData, '/sensor/data', self.SensorData_callback, 10)
        self.apps_param_sub = self.create_subscription(AppParams,'/apps/params',self.AppParams_callback,10)
        self.motor_cmd_pub = self.create_publisher(MotorCmd,'/motor/cmd_data', 10) 
        self.app_mode_sub = self.create_subscription(String,'/app_mode',self.AppMode_callback, 10) 
        self.sensor_client = self.create_client(SensorFeedback, '/sensor_feeback')
        while not self.sensor_client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')
        self.app_param = None
        self.app_mode = None

    def SensorData_callback(self, msg):
        self.feedback_data = msg

        # if self.app_mode=="2:Passive Mode":
        #     self.set_passive_mode(self.app_param,self.feedback_data)

    def AppParams_callback(self,msg):
        self.app_param = msg

    def AppMode_callback(self,msg):
        self.app_mode = msg.data

    def run_apps(self):
        
        if self.app_mode=="2:Passive Mode":
            self.set_passive_mode(self.app_param,self.feedback_data)
        else:
            pass

    def send_request(self, a):
        # Prepare the request
        req = SensorFeedback.Request()
        req.sensor = a

        # Send the request
        future = self.sensor_client.call_async(req)
        while rclpy.ok():
            rclpy.spin_once(self)
            if future.done():
                try:
                    response = future.result()
                    self.get_logger().info(f"Response: {response.data}")
                    break
                except Exception as e:
                    self.get_logger().error(f"Service call failed: {e}")
                    break
        return response.data

    def set_passive_mode(self,app_param,sensor_fb):      # B) Trigger and Go
                self.motor_cmd = MotorCmd()
                self.motor_cmd.cmd = 0
                self.motor_cmd.data = 0.0
                threshold0 = -30                  # Set start threshold 
                threshold1 = -45                  # Set effort threshold
                direction = 0                   # Motor Direction - no need to change, keep it default

                repetitions = app_param.repeat
                start_point = app_param.start
                end_point = app_param.end
                speed = app_param.speed

                current_fb =sensor_fb.current
                position_fb = sensor_fb.position
                velocity_fb = sensor_fb.velocity

                # speed = 15                      # Set Link motion speed in rpm
                print(f"self.position_feedback1: {position_fb}")
                # repetitions = int(input("how many repeatitions do you want: "))
                # start_point = int(start_point)

                # end_point = int(input("Enter the end point: "))

                if start_point>0 and end_point>0:
                
                    for i in range(repetitions):
                            # direction ^= 1
                        threshold0 = -threshold0
                        threshold1 = -threshold1
                        
                        if threshold0>0 and threshold1>0:
                            patient_ready = False
                            motor_ready = False
                            # Set to starting_point
                            # print(f"position2: {self.position_feedback}")
                            while motor_ready==False:
                                # self.controller.set_profile_speed(100)
                                self.motor_cmd.cmd = 4
                                self.motor_cmd.data = 100.0           # Set Profile speed
                                self.motor_cmd_pub.publish(self.motor_cmd)
                                # print(self.position_feedback)
                                position_fb = self.send_request(2)
                                if position_fb!=start_point:     #Position
                                    # self.controller.set_start_position_mode(start_point)
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = start_point 
                                    self.motor_cmd_pub.publish(self.motor_cmd)      # Set start position mode
                                    motor_ready = False
                                    # print(f"position3: {self.position_feedback}")
                                else:
                                    motor_ready = True
                                    # print("motor is Ready!")

                                #If motor is ready at start point then start the operation 
                                if motor_ready:
                                    # self.controller.set_profile_speed(speed)
                                    self.motor_cmd.cmd = 4
                                    self.motor_cmd.data = 100.0 
                                    self.motor_cmd_pub.publish(self.motor_cmd)
                                    while True:
                                        # current_feedback = self.controller.Read_real_current()
                                        # print(current_feedback)
                                        current_fb = self.send_request(1)
                                        if current_fb>threshold0:
                                            patient_ready = True
                                            # print("patient is ready!")
                                            break
                                            
                                    #If patient is ready then start the motion
                                    if patient_ready:
                                        # self.controller.motor_direction(direction)       #set motor in CW direction
                                        self.motor_cmd.cmd = 5
                                        self.motor_cmd.data = direction 
                                        self.motor_cmd_pub.publish(self.motor_cmd)
                                        while patient_ready:
                                            # current_feedback = self.controller.Read_real_current()
                                            # position_feedback = self.controller.Read_actual_position()
                                            # print("current feedback: ", current_feedback, "position: ", position_feedback)
                                            current_fb = self.send_request(1)
                                            position_fb = self.send_request(2)
                                            if current_fb>threshold1:  
                                                # self.controller.set_start_position_mode(-end_point)
                                                self.motor_cmd.cmd = 1
                                                self.motor_cmd.data = -end_point 
                                                self.motor_cmd_pub.publish(self.motor_cmd)

                                            elif position_fb==(-end_point):
                                                # self.controller.set_velocity_mode(0)
                                                self.motor_cmd.cmd = 2
                                                self.motor_cmd.data = 0.0 
                                                self.motor_cmd_pub.publish(self.motor_cmd)
                                                swap = -start_point
                                                start_point = -end_point
                                                end_point = swap
                                                # print("ready for next iteration!")
                                                patient_ready=False
                                            

                        else:
                            patient_ready = False
                            motor_ready = False
                            # Set to starting_point
                            while motor_ready==False:
                                # self.controller.set_profile_speed(100)
                                self.motor_cmd.cmd = 4
                                self.motor_cmd.data = 100.0 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                                position_fb = self.send_request(2)
                                if position_fb!=start_point:
                                    # self.controller.set_start_position_mode(start_point)
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = start_point 
                                    self.motor_cmd_pub.publish(self.motor_cmd)
                                    motor_ready = False
                                else:
                                    motor_ready = True
                                    # print("motor is Ready!")

                                #If motor is ready at start point then start the operation 
                                if motor_ready:
                                    # self.controller.set_profile_speed(speed)
                                    self.motor_cmd.cmd = 4
                                    self.motor_cmd.data = speed 
                                    self.motor_cmd_pub.publish(self.motor_cmd)
                                    while True:
                                        # current_feedback = self.controller.Read_real_current()
                                        # print(current_feedback)
                                        current_fb = self.send_request(1)
                                        if current_fb<threshold0:
                                            patient_ready = True
                                            # print("patient is ready!")
                                            break
                                            
                                    #If patient is ready then start the motion
                                    if patient_ready:
                                        # self.controller.motor_direction(direction)       #set motor in CW direction
                                        self.motor_cmd.cmd = 5
                                        self.motor_cmd.data = direction 
                                        self.motor_cmd_pub.publish(self.motor_cmd)
                                        while patient_ready:
                                            # current_feedback = self.controller.Read_real_current()
                                            # position_feedback = self.controller.Read_actual_position()
                                            # print("current feedback: ", current_feedback,"position: ", position_feedback)
                                            current_fb = self.send_request(1)
                                            position_fb = self.send_request(2)
                                            if current_fb<threshold1:  
                                                # self.controller.set_start_position_mode(-end_point)
                                                self.motor_cmd.cmd = 1
                                                self.motor_cmd.data = -end_point 
                                                self.motor_cmd_pub.publish(self.motor_cmd)

                                            elif position_fb==(-end_point):
                                                # self.controller.set_velocity_mode(0)
                                                self.motor_cmd.cmd = 2
                                                self.motor_cmd.data = 0.0 
                                                self.motor_cmd_pub.publish(self.motor_cmd)
                                                swap = start_point
                                                start_point = -end_point
                                                end_point = -swap
                                                patient_ready=False
                                            
                else:
                    for i in range(repetitions):
                            # direction ^= 1
                        threshold0 = -threshold0
                        threshold1 = -threshold1
                        print(f"self.position_feedback2: {position_fb}")
                        if threshold0>0 and threshold1>0:
                            patient_ready = False
                            motor_ready = False
                            # Set to starting_point
                            while motor_ready==False:
                                # self.controller.set_profile_speed(100)
                                self.motor_cmd.cmd = 4
                                self.motor_cmd.data = 100.0 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                                # print(position_feedback)
                                position_fb = self.send_request(2)
                                if position_fb !=start_point:
                                    # print(f"self.position_feedback: {self.position_feedback}== start point: {start_point}")
                                    # self.controller.set_start_position_mode(start_point)
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = start_point 
                                    # print(f"motor command:{self.motor_cmd.cmd}, motor Data: {self.motor_cmd.data}")
                                    self.motor_cmd_pub.publish(self.motor_cmd)
                                    motor_ready = False
                                    print(f"self.position_feedback3: {position_fb}")
                                else:
                                    motor_ready = True
                                    # print("motor is Ready!")

                                #If motor is ready at start point then start the operation 
                                if motor_ready:
                                    # self.controller.set_profile_speed(speed)
                                    self.motor_cmd.cmd = 4
                                    self.motor_cmd.data = speed 
                                    self.motor_cmd_pub.publish(self.motor_cmd)
                                    while True:
                                        # current_feedback = self.controller.Read_real_current()
                                        # print(current_feedback)
                                        current_fb = self.send_request(1)
                                        if current_fb>threshold0:
                                            patient_ready = True
                                            # print("patient is ready!")
                                            break
                                            
                                    #If patient is ready then start the motion
                                    if patient_ready:
                                        # self.controller.motor_direction(direction)       #set motor in CW direction
                                        self.motor_cmd.cmd = 5
                                        self.motor_cmd.data = direction 
                                        self.motor_cmd_pub.publish(self.motor_cmd)
                                        while patient_ready:
                                            # current_feedback = self.controller.Read_real_current()
                                            # position_feedback = self.controller.Read_actual_position()
                                            # print("current feedback: ", current_feedback, "position: ", position_feedback)
                                            current_fb = self.send_request(1)
                                            position_fb = self.send_request(2)
                                            if current_fb>threshold1:  
                                                # self.controller.set_start_position_mode(end_point)
                                                self.motor_cmd.cmd = 1
                                                self.motor_cmd.data = end_point 
                                                self.motor_cmd_pub.publish(self.motor_cmd)

                                            elif position_fb==(end_point):
                                                # self.controller.set_velocity_mode(0)
                                                self.motor_cmd.cmd = 2
                                                self.motor_cmd.data = 0.0
                                                self.motor_cmd_pub.publish(self.motor_cmd)
                                                swap = start_point
                                                start_point = end_point
                                                end_point = swap
                                                patient_ready=False
                                            

                        else:
                            patient_ready = False
                            motor_ready = False
                            # Set to starting_point
                            while motor_ready==False:
                                # position_feedback = self.controller.Read_actual_position()
                                # self.controller.set_profile_speed(100)
                                self.motor_cmd.cmd = 4
                                self.motor_cmd.data = 100.0 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                                # print(position_feedback)
                                position_fb = self.send_request(2)
                                if position_fb!=start_point:
                                    # self.controller.set_start_position_mode(start_point)
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = start_point 
                                    self.motor_cmd_pub.publish(self.motor_cmd)
                                    motor_ready = False
                                else:
                                    motor_ready = True
                                    # print("motor is Ready!")

                                #If motor is ready at start point then start the operation 
                                if motor_ready:
                                    # self.controller.set_profile_speed(speed)
                                    self.motor_cmd.cmd = 4
                                    self.motor_cmd.data = speed 
                                    self.motor_cmd_pub.publish(self.motor_cmd)
                                    while True:
                                        # current_feedback = self.controller.Read_real_current()
                                        # print(current_feedback)
                                        current_fb = self.send_request(1)
                                        if current_fb<threshold0:
                                            patient_ready = True
                                            # print("patient is ready!")
                                            break
                                            
                                    #If patient is ready then start the motion
                                    if patient_ready:
                                        # self.controller.motor_direction(direction)       #set motor in CW direction
                                        self.motor_cmd.cmd = 5
                                        self.motor_cmd.data = direction 
                                        self.motor_cmd_pub.publish(self.motor_cmd)
                                        while patient_ready:
                                            # current_feedback = self.controller.Read_real_current()
                                            # position_feedback = self.controller.Read_actual_position()
                                            # print("current feedback: ", current_feedback,"position: ", position_feedback)
                                            current_fb = self.send_request(1)
                                            position_fb = self.send_request(2)
                                            if current_fb<threshold1:  
                                                # self.controller.set_start_position_mode(end_point)
                                                self.motor_cmd.cmd = 1
                                                self.motor_cmd.data = end_point 
                                                self.motor_cmd_pub.publish(self.motor_cmd)

                                            elif position_fb==(end_point):
                                                # self.controller.set_velocity_mode(0)
                                                self.motor_cmd.cmd = 2
                                                self.motor_cmd.data = 0.0 
                                                self.motor_cmd_pub.publish(self.motor_cmd)
                                                swap = start_point
                                                start_point = end_point
                                                end_point = swap
                                                # print("ready for next iteration!")
                                                patient_ready=False

def main():
    PORT = '/dev/ttyUSB0' 
    BAUDRATE = 38400  
    TIMEOUT = 0.06  # Timeout in seconds
    rclpy.init()
    node = ApplicationNode(PORT,BAUDRATE,TIMEOUT)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
