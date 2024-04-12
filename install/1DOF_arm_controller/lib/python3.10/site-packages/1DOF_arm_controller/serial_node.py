import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from .KincoServoDriver import ServoController
from arm_interfaces.msg import SensorData
from arm_interfaces.msg import MotorCmd
from arm_interfaces.srv import SensorFeedback

class ControllerNode(Node,ServoController):

    def __init__(self,port,baudrate,timeout):
        super().__init__("serial_node")
        ServoController.__init__(self,port,baudrate,timeout)

        self.open_serial_port()
        self.sensor_data_pub = self.create_publisher(SensorData, '/sensor/data', 10)
        self.cmd_vel_sub = self.create_subscription(MotorCmd, '/motor/cmd_data', self.motor_cmd_callback, 10)
        self.button_event_sub = self.create_subscription(Int32,'/button_events',self.button_event_callback,10)
        self.sensor_srv = self.create_service(SensorFeedback, '/sensor_feedback', self.get_sensor_callback)

        # Timer to trigger data reading and publishing at a fixed rate (adjust as needed)
        self.timer = self.create_timer(0.3, self.read_and_publish_data)  # 10 Hz

    # ==============Publisher Functions===============
    def read_and_publish_data(self):
        #Reading data from Motor
        sensor_data = SensorData()
        sensor_data.current = self.Read_real_current()
        sensor_data.position = self.Read_actual_position()
        sensor_data.velocity = self.Read_real_speed()
        # Publish sensor data on respective topics
        self.sensor_data_pub.publish(sensor_data)



    def subscribe_and_write_data(self):
        
        if self.motor_cmd==1:
            self.set_start_position_mode(self.motor_data)

        elif self.motor_cmd==2:
            self.set_velocity_mode(self.motor_data)

        elif self.motor_cmd==3:
            self.set_torque_mode(self.motor_data)

        elif self.motor_cmd==4:
            self.set_profile_speed(self.motor_data)
        
        elif self.motor_cmd==5:
            self.motor_direction(self.motor_data)

        elif self.motor_cmd==6:
            self.stop_driver()
        
        elif self.motor_cmd==7:
            self.start_driver()

    # ===============Subscriber functions===========
    def motor_cmd_callback(self,msg):
        self.motor_cmd = msg.cmd
        self.motor_data = msg.data
        self.subscribe_and_write_data()

    def button_event_callback(self,msg):
        self.event = msg.data

    #================Service Functions==============
    def get_sensor_callback(self, request, response):
        # This function will be called whenever the service is requested
        self.sensor = request.sensor
        print(self.sensor)
        if self.sensor==1:
            response.data = self.Read_real_current()
        elif self.sensor==2:
            response.data = float(self.Read_actual_position())
        elif self.sensor==3:
            response.data = self.Read_real_speed()
        return response
def main():
    PORT = '/dev/ttyUSB0' 
    BAUDRATE = 38400  
    TIMEOUT = 0.06  # Timeout in seconds
    # apps = SensorNode(PORT,BAUDRATE,TIMEOUT)
    # apps.set_resistive_mode(6,-100,-300,9)
    rclpy.init()
    node = ControllerNode(PORT,BAUDRATE,TIMEOUT)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
