import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from .KincoServoDriver import ServoController
from arm_interfaces.msg import SensorData, MotorCmd, AppParams
from arm_interfaces.srv import SensorFeedback
import time
import threading

class ApplicationNode(Node,ServoController):
    def __init__(self,port,baudrate,timeout):
        super().__init__("application_node")
        self.controller = ServoController(port,baudrate,timeout)
        self.app_param = None
        self.app_mode = None
        self.feedback_data = None
        self.button_status = None
        self.sensor_data_lock = threading.Lock()

        # Create subscribers for each sensor topic
        self.sensor_data_sub = self.create_subscription(SensorData, '/sensor/data', self.SensorData_callback, 10)
        self.apps_param_sub = self.create_subscription(AppParams,'/apps/params',self.AppParams_callback,10)
        self.motor_cmd_pub = self.create_publisher(MotorCmd,'/motor/cmd_data', 10)
        self.motor_cmd_sub = self.create_subscription(MotorCmd,'/motor/cmd_data',self.ButtonStp_status, 10) 
        self.app_mode_sub = self.create_subscription(String,'/app_mode',self.AppMode_callback, 10)
        self.sensor_client = self.create_client(SensorFeedback, '/sensor_feedback')
        self.sensor_client.wait_for_service(timeout_sec=1.0)
        
    def SensorData_callback(self, msg):
        # Callback for processing sensor commands received from another node
        with self.sensor_data_lock:
            self.feedback_data = msg

    def AppParams_callback(self,msg):
        with self.sensor_data_lock:
            self.app_param = msg

    def AppMode_callback(self,msg):
        with self.sensor_data_lock:
            self.app_mode = msg.data

    def ButtonStp_status(self,msg):
        with self.sensor_data_lock:
            self.button_status = msg

    def update_sensor_data(self):
        while True:
            # Simulate updating sensor data
            with self.sensor_data_lock:
                self.sensorData = self.feedback_data
                self.appParams = self.app_param
                self.appMode =  self.app_mode
                self.buttonStatus = self.button_status
            time.sleep(0.1)  # Adjust the update interval as needed

    def access_sensor_data(self):
        while True:
            # with self.sensor_data_lock:
                if self.appMode =="1:Assistive Mode":
                    pass
        
                elif self.appMode =="2:Passive Mode":
                    # print(self.app_mode)
                    self.set_passive_mode(self.appParams,self.sensorData)
                
                elif self.appMode =="3:Resistive ModeA":
                    self.set_resistive_modeA(self.appParams,self.sensorData)

                elif self.appMode =="4:Resistive ModeB":
                    self.set_resistive_modeB(self.appParams,self.sensorData)
                
                time.sleep(0.1)  # Adjust the access interval as needed

    def set_passive_mode(self,app_param,sensor_fb):      # B) Trigger and Go
                self.motor_cmd = MotorCmd()
                self.motor_cmd.cmd = 0
                self.motor_cmd.data = 0
                 
                # threshold1 = 30                  # Set effort threshold
                direction = 0                   # Motor Direction - no need to change, keep it default

                repetitions = app_param.repeat
                start_point = app_param.start
                end_point = app_param.end
                speed = app_param.speed
                delay = app_param.delay
                threshold1 = app_param.threshold

                current_fb =sensor_fb.current
                position_fb = sensor_fb.position
                velocity_fb = sensor_fb.velocity

                operation_finish = False
                x = 0

                if threshold1<9:
                    threshold0 = 0
                else:
                    threshold0 = 12

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
                        if threshold0==0 and threshold1==0:
                            while motor_ready==False and operation_finish == False:
                                position_fb = self.send_request(2)

                                if position_fb!=start_point:     
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = int(round(start_point,1)) 
                                    self.motor_cmd_pub.publish(self.motor_cmd)      
                                    motor_ready = False
                                else:
                                    motor_ready = True
                                    x += 1
                            
                            while motor_ready==True and operation_finish == False:
                                    position_fb = self.send_request(2)

                                    if position_fb!=end_point:     
                                        self.motor_cmd.cmd = 1
                                        self.motor_cmd.data = int(round(end_point,1))
                                        self.motor_cmd_pub.publish(self.motor_cmd)      
                                        motor_ready = True
                                    else:
                                        motor_ready = False
                                        if x==repetitions:
                                            operation_finish = True

                        elif threshold0>0 and threshold1>0:
                            patient_ready = False
                            motor_ready = False
                            # Set to starting_point
                            # print(f"position2: {self.position_feedback}")
                            while motor_ready==False:
                                # self.controller.set_profile_speed(100)
                                self.motor_cmd.cmd = 4
                                self.motor_cmd.data = speed           # Set Profile speed
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
                                self.motor_cmd.data = speed
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
                        threshold0 = -threshold0
                        threshold1 = -threshold1
                        
                        if threshold0==0 and threshold1==0:
                            motor_ready = False
                            while motor_ready==False and operation_finish == False:
                                position_fb = self.send_request(2)

                                if position_fb!=start_point:     
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = int(round(start_point,1)) 
                                    self.motor_cmd_pub.publish(self.motor_cmd)      
                                    motor_ready = False
                                else:
                                    motor_ready = True
                                    x += 1
                            time.sleep(delay)
                            
                            while motor_ready==True and operation_finish == False:
                                position_fb = self.send_request(2)

                                if position_fb!=end_point:     
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = int(round(end_point,1))
                                    self.motor_cmd_pub.publish(self.motor_cmd)      
                                    motor_ready = True
                                else:
                                    motor_ready = False
                                    if x==repetitions:
                                        operation_finish = True
                            time.sleep(delay)

                        elif threshold0>0 and threshold1>0:
                            patient_ready = False
                            motor_ready = False
                            # Set to starting_point
                           
                            while motor_ready==False:
                                # self.controller.set_profile_speed(100)
                                self.motor_cmd.cmd = 4
                                self.motor_cmd.data = speed
                                self.motor_cmd_pub.publish(self.motor_cmd)
                                position_fb = self.send_request(2)
                               
                                if position_fb !=start_point:
                                    # print(f"self.position_feedback: {self.position_feedback}== start point: {start_point}")
                                    # self.controller.set_start_position_mode(start_point)
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = int(round(start_point,1)) 
                                    # print(f"motor command:{self.motor_cmd.cmd}, motor Data: {self.motor_cmd.data}")
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
                                                self.motor_cmd.data = int(round(end_point,1)) 
                                                self.motor_cmd_pub.publish(self.motor_cmd)

                                            elif position_fb==(end_point):
                                                # self.controller.set_velocity_mode(0)
                                                self.motor_cmd.cmd = 2
                                                self.motor_cmd.data = 0
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
                                self.motor_cmd.data = speed
                                self.motor_cmd_pub.publish(self.motor_cmd)
                                # print(position_feedback)
                                position_fb = self.send_request(2)
                                if position_fb!=start_point:
                                    # self.controller.set_start_position_mode(start_point)
                                    self.motor_cmd.cmd = 1
                                    self.motor_cmd.data = int(round(start_point,1)) 
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
                                                self.motor_cmd.data = int(round(end_point,1)) 
                                                self.motor_cmd_pub.publish(self.motor_cmd)

                                            elif position_fb==(end_point):
                                                # self.controller.set_velocity_mode(0)
                                                self.motor_cmd.cmd = 2
                                                self.motor_cmd.data = 0 
                                                self.motor_cmd_pub.publish(self.motor_cmd)
                                                swap = start_point
                                                start_point = int(round(end_point,1))
                                                end_point = swap
                                                # print("ready for next iteration!")
                                                patient_ready=False
    
    def set_resistive_modeA(self,app_param,sensor_fb):
        # threshold0 = 45                  # Set start threshold 
        # threshold1 = -45                  # Set effort threshold
        # direction = 0                   # Motor Direction - no need to change, keep it default
        # speed = 100                     #set homing speed in rpm
        # ------------------------------------------------------
        self.motor_cmd = MotorCmd()
        self.motor_cmd.cmd = 0
        self.motor_cmd.data = 0
        direction = 0                   # Motor Direction - no need to change, keep it default

        repetitions = app_param.repeat
        start_point = app_param.start
        end_point = app_param.end
        speed = app_param.speed
        torque = app_param.torque
        # delay = app_param.delay
        threshold1 = -app_param.threshold
        threshold0 = app_param.threshold

        current_fb =sensor_fb.current
        position_fb = sensor_fb.position
        # velocity_fb = sensor_fb.velocity

        operation_finish = False
        x = 0

        # -------------------------------------------------------
        temp = end_point
        # self.controller.motor_direction(direction)
        patient_ready = False
        motor_ready = False
        
        # Set to starting_point
        while motor_ready==False:
            # position_feedback = self.controller.Read_actual_position()
            position_fb = self.send_request(2)
            self.motor_cmd.cmd = 4
            self.motor_cmd.data = speed
            self.motor_cmd_pub.publish(self.motor_cmd)
            # print(position_fb)
            if position_fb!=start_point:
                # self.controller.set_start_position_mode(start_point)
                self.motor_cmd.cmd = 1
                self.motor_cmd.data = int(round(start_point,1))
                self.motor_cmd_pub.publish(self.motor_cmd)
                motor_ready = False
            else:
                motor_ready = True
                # print("motor is Ready!")

        #If motor is ready at start point then start the operation 
        if motor_ready:
            while True:
                current_fb = self.send_request(1)
                if current_fb>0:
                    if current_fb>threshold0:  
                        direction = 0
                        patient_ready = True
                        break
                else:
                    if current_fb<threshold1: 
                        direction = 1
                        patient_ready = True
                        break
            if patient_ready:
                for i in range (repetitions):
                    self.motor_cmd.cmd = 5
                    self.motor_cmd.data = direction
                    self.motor_cmd_pub.publish(self.motor_cmd)
                    self.motor_cmd.cmd = 3
                    self.motor_cmd.data = torque
                    self.motor_cmd_pub.publish(self.motor_cmd)
                    while True:
                        position_fb = self.send_request(2)
                        position_fb = self.send_request(1)

                        if position_fb<=(-end_point):
                            self.motor_cmd.cmd = 2
                            self.motor_cmd.data = 0
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            if position_fb<=(-threshold0):
                                direction ^= 1
                                end_point=temp+end_point
                                break

    def set_resistive_modeB(self,app_param,sensor_fb):
        self.motor_cmd = MotorCmd()
        self.motor_cmd.cmd = 0
        self.motor_cmd.data = 0
        direction = 0                   # Motor Direction - no need to change, keep it default

        repetitions = app_param.repeat
        start_point = app_param.start
        end_point = app_param.end
        speed = app_param.speed
        torque = app_param.torque
        # delay = app_param.delay
        threshold1 = app_param.threshold

        current_fb =sensor_fb.current
        position_fb = sensor_fb.position
        # velocity_fb = sensor_fb.velocity
        motor_ready = False
        if start_point==0 and end_point>0:
            while motor_ready==False:
                position_fb = self.send_request(2)
                if position_fb!=start_point:     
                    self.motor_cmd.cmd = 1
                    self.motor_cmd.data = int(round(start_point,1)) 
                    self.motor_cmd_pub.publish(self.motor_cmd)      
                    motor_ready = False
                else:
                    motor_ready = True
                    break

            while True:
                if motor_ready:
                    self.motor_cmd.cmd = 5
                    self.motor_cmd.data = direction 
                    self.motor_cmd_pub.publish(self.motor_cmd)
                    while motor_ready:
                        current_fb = self.send_request(1)
                        if current_fb<threshold1:  
                            self.motor_cmd.cmd = 3
                            self.motor_cmd.data = torque 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            torque_mode = True
                            break
                    while torque_mode:
                        position_fb = self.send_request(2)
                        current_fb = self.send_request(1)
                        if position_fb>=end_point:
                            self.motor_cmd.cmd = 2
                            self.motor_cmd.data = 0 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            if current_fb>threshold1:  
                                self.motor_cmd.cmd = 3
                                self.motor_cmd.data = torque 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                            
                        elif position_fb<=start_point:
                            self.motor_cmd.cmd = 2
                            self.motor_cmd.data = 0 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            if current_fb<(-threshold1):  
                                self.motor_cmd.cmd = 3
                                self.motor_cmd.data = torque 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                        
                        else:  
                            self.motor_cmd.cmd = 3
                            self.motor_cmd.data = torque 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            torque_mode = True
                            break

        # elif start_point==0 and end_point<0:
        #     while motor_ready==False:
        #         position_fb = self.send_request(2)
        #         if position_fb!=start_point:     
        #             self.motor_cmd.cmd = 1
        #             self.motor_cmd.data = int(round(start_point,1)) 
        #             self.motor_cmd_pub.publish(self.motor_cmd)      
        #             motor_ready = False
        #         else:
        #             motor_ready = True
        #             break

        #     # while True:
        #     #     if motor_ready:
        #     #         self.motor_cmd.cmd = 5
        #     #         self.motor_cmd.data = direction 
        #     #         self.motor_cmd_pub.publish(self.motor_cmd)
        #     #         while motor_ready:
        #     #             current_fb = self.send_request(1)
        #     #             if current_fb>threshold1:  
        #     #                 self.motor_cmd.cmd = 3
        #     #                 self.motor_cmd.data = torque 
        #     #                 self.motor_cmd_pub.publish(self.motor_cmd)
        #     #                 torque_mode = True
        #     #                 break
        #     #         while torque_mode:
        #     #             position_fb = self.send_request(2)
        #     #             current_fb = self.send_request(1)
        #     #             if position_fb<=end_point:
        #     #                 self.motor_cmd.cmd = 2
        #     #                 self.motor_cmd.data = 0 
        #     #                 self.motor_cmd_pub.publish(self.motor_cmd)
        #                     # if current_fb>threshold1:  
        #                     #     self.motor_cmd.cmd = 3
        #                     #     self.motor_cmd.data = torque 
        #                     #     self.motor_cmd_pub.publish(self.motor_cmd)
                            
        #                 # elif position_fb>=start_point:
        #                 #     self.motor_cmd.cmd = 2
        #                 #     self.motor_cmd.data = 0 
        #                 #     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     # if current_fb<(-threshold1):  
        #                     #     self.motor_cmd.cmd = 3
        #                     #     self.motor_cmd.data = torque 
        #                     #     self.motor_cmd_pub.publish(self.motor_cmd)
                        
        #                 # else:  
        #                 #     self.motor_cmd.cmd = 3
        #                 #     self.motor_cmd.data = torque 
        #                 #     self.motor_cmd_pub.publish(self.motor_cmd)
        #                 #     torque_mode = True
        #                 #     break

        # elif start_point>0 and end_point>0:
        #     if start_point>end_point:
        #         while motor_ready==False:
        #             position_fb = self.send_request(2)
        #             if position_fb!=start_point:     
        #                 self.motor_cmd.cmd = 1
        #                 self.motor_cmd.data = int(round(start_point,1)) 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)      
        #                 motor_ready = False
        #             else:
        #                 motor_ready = True
        #                 break

        #         while True:
        #             if motor_ready:
        #                 self.motor_cmd.cmd = 5
        #                 self.motor_cmd.data = direction 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)
        #                 while motor_ready:
        #                     current_fb = self.send_request(1)
        #                     if current_fb<threshold1:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break
        #                 while torque_mode:
        #                     position_fb = self.send_request(2)
        #                     current_fb = self.send_request(1)
        #                     if position_fb>=end_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb>threshold1:  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                                
        #                     elif position_fb<=start_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb<(-threshold1):  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                            
        #                     else:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break
        #     elif start_point<end_point:
        #         while motor_ready==False:
        #             position_fb = self.send_request(2)
        #             if position_fb!=start_point:     
        #                 self.motor_cmd.cmd = 1
        #                 self.motor_cmd.data = int(round(start_point,1)) 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)      
        #                 motor_ready = False
        #             else:
        #                 motor_ready = True
        #                 break

        #         while True:
        #             if motor_ready:
        #                 self.motor_cmd.cmd = 5
        #                 self.motor_cmd.data = direction 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)
        #                 while motor_ready:
        #                     current_fb = self.send_request(1)
        #                     if current_fb<threshold1:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break
        #                 while torque_mode:
        #                     position_fb = self.send_request(2)
        #                     current_fb = self.send_request(1)
        #                     if position_fb>=end_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb>threshold1:  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                                
        #                     elif position_fb<=start_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb<(-threshold1):  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                            
        #                     else:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break              

        elif start_point>0 and end_point<0:
            while motor_ready==False:
                position_fb = self.send_request(2)
                if position_fb!=start_point:     
                    self.motor_cmd.cmd = 1
                    self.motor_cmd.data = int(round(start_point,1)) 
                    self.motor_cmd_pub.publish(self.motor_cmd)      
                    motor_ready = False
                else:
                    motor_ready = True
                    break

            while True:
                if motor_ready:
                    self.motor_cmd.cmd = 5
                    self.motor_cmd.data = direction 
                    self.motor_cmd_pub.publish(self.motor_cmd)
                    while motor_ready:
                        current_fb = self.send_request(1)
                        if current_fb>threshold1:  
                            self.motor_cmd.cmd = 3
                            self.motor_cmd.data = torque 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            torque_mode = True
                            break
                    while torque_mode:
                        position_fb = self.send_request(2)
                        current_fb = self.send_request(1)
                        if position_fb<=end_point:
                            self.motor_cmd.cmd = 2
                            self.motor_cmd.data = 0 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            if current_fb<(-threshold1):  
                                self.motor_cmd.cmd = 3
                                self.motor_cmd.data = torque 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                            
                        elif position_fb>=start_point:
                            self.motor_cmd.cmd = 2
                            self.motor_cmd.data = 0 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            if current_fb>threshold1:  
                                self.motor_cmd.cmd = 3
                                self.motor_cmd.data = torque 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                        
                        elif position_fb>end_point and position_fb<start_point:  
                            self.motor_cmd.cmd = 3
                            self.motor_cmd.data = torque 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            # torque_mode = True
                            # break
                        # else:
                        #     self.motor_cmd.cmd = 2
                        #     self.motor_cmd.data = 0 
                        #     self.motor_cmd_pub.publish(self.motor_cmd)
        
        elif start_point>0 and end_point==0:
            while motor_ready==False:
                position_fb = self.send_request(2)
                if position_fb!=start_point:     
                    self.motor_cmd.cmd = 1
                    self.motor_cmd.data = int(round(start_point,1)) 
                    self.motor_cmd_pub.publish(self.motor_cmd)      
                    motor_ready = False
                else:
                    motor_ready = True
                    break

            
            for i in range(repetitions):
                # while True:
                if motor_ready:
                    self.motor_cmd.cmd = 5
                    self.motor_cmd.data = direction 
                    self.motor_cmd_pub.publish(self.motor_cmd)
                    while motor_ready:
                        current_fb = self.send_request(1)
                        if current_fb>threshold1:  
                            self.motor_cmd.cmd = 3
                            self.motor_cmd.data = torque 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            torque_mode = True
                            break
                    while torque_mode:
                        position_fb = self.send_request(2)
                        current_fb = self.send_request(1)
                        if position_fb<=end_point:
                            self.motor_cmd.cmd = 2
                            self.motor_cmd.data = 0 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            if current_fb<(-threshold1):  
                                self.motor_cmd.cmd = 3
                                self.motor_cmd.data = torque 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                            
                        elif position_fb>=start_point:
                            self.motor_cmd.cmd = 2
                            self.motor_cmd.data = 0 
                            self.motor_cmd_pub.publish(self.motor_cmd)
                            if current_fb>threshold1:  
                                self.motor_cmd.cmd = 3
                                self.motor_cmd.data = torque 
                                self.motor_cmd_pub.publish(self.motor_cmd)
                        
                        # elif position_fb>end_point and position_fb<start_point:  
                        #     self.motor_cmd.cmd = 3
                        #     self.motor_cmd.data = torque 
                        #     self.motor_cmd_pub.publish(self.motor_cmd)
                        #     torque_mode = True
                        #     break

        # elif start_point<0 and end_point>0:
        #     while motor_ready==False:
        #         position_fb = self.send_request(2)
        #         if position_fb!=start_point:     
        #             self.motor_cmd.cmd = 1
        #             self.motor_cmd.data = int(round(start_point,1)) 
        #             self.motor_cmd_pub.publish(self.motor_cmd)      
        #             motor_ready = False
        #         else:
        #             motor_ready = True
        #             break

        #     while True:
        #         if motor_ready:
        #             self.motor_cmd.cmd = 5
        #             self.motor_cmd.data = direction 
        #             self.motor_cmd_pub.publish(self.motor_cmd)
        #             while motor_ready:
        #                 current_fb = self.send_request(1)
        #                 if current_fb<threshold1:  
        #                     self.motor_cmd.cmd = 3
        #                     self.motor_cmd.data = torque 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     torque_mode = True
        #                     break
        #             while torque_mode:
        #                 position_fb = self.send_request(2)
        #                 current_fb = self.send_request(1)
        #                 if position_fb>=end_point:
        #                     self.motor_cmd.cmd = 2
        #                     self.motor_cmd.data = 0 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     if current_fb>threshold1:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
                            
        #                 elif position_fb<=start_point:
        #                     self.motor_cmd.cmd = 2
        #                     self.motor_cmd.data = 0 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     if current_fb<(-threshold1):  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
                        
        #                 else:  
        #                     self.motor_cmd.cmd = 3
        #                     self.motor_cmd.data = torque 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     torque_mode = True
        #                     break

        # elif start_point<0 and end_point<0:
        #     if start_point>end_point:
        #         while motor_ready==False:
        #             position_fb = self.send_request(2)
        #             if position_fb!=start_point:     
        #                 self.motor_cmd.cmd = 1
        #                 self.motor_cmd.data = int(round(start_point,1)) 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)      
        #                 motor_ready = False
        #             else:
        #                 motor_ready = True
        #                 break

        #         while True:
        #             if motor_ready:
        #                 self.motor_cmd.cmd = 5
        #                 self.motor_cmd.data = direction 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)
        #                 while motor_ready:
        #                     current_fb = self.send_request(1)
        #                     if current_fb<threshold1:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break
        #                 while torque_mode:
        #                     position_fb = self.send_request(2)
        #                     current_fb = self.send_request(1)
        #                     if position_fb>=end_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb>threshold1:  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                                
        #                     elif position_fb<=start_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb<(-threshold1):  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                            
        #                     else:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break
        #     elif start_point<end_point:
        #         while motor_ready==False:
        #             position_fb = self.send_request(2)
        #             if position_fb!=start_point:     
        #                 self.motor_cmd.cmd = 1
        #                 self.motor_cmd.data = int(round(start_point,1)) 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)      
        #                 motor_ready = False
        #             else:
        #                 motor_ready = True
        #                 break

        #         while True:
        #             if motor_ready:
        #                 self.motor_cmd.cmd = 5
        #                 self.motor_cmd.data = direction 
        #                 self.motor_cmd_pub.publish(self.motor_cmd)
        #                 while motor_ready:
        #                     current_fb = self.send_request(1)
        #                     if current_fb<threshold1:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break
        #                 while torque_mode:
        #                     position_fb = self.send_request(2)
        #                     current_fb = self.send_request(1)
        #                     if position_fb>=end_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb>threshold1:  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                                
        #                     elif position_fb<=start_point:
        #                         self.motor_cmd.cmd = 2
        #                         self.motor_cmd.data = 0 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         if current_fb<(-threshold1):  
        #                             self.motor_cmd.cmd = 3
        #                             self.motor_cmd.data = torque 
        #                             self.motor_cmd_pub.publish(self.motor_cmd)
                            
        #                     else:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
        #                         torque_mode = True
        #                         break

        # elif start_point<0 and end_point==0:
        #     while motor_ready==False:
        #         position_fb = self.send_request(2)
        #         if position_fb!=start_point:     
        #             self.motor_cmd.cmd = 1
        #             self.motor_cmd.data = int(round(start_point,1)) 
        #             self.motor_cmd_pub.publish(self.motor_cmd)      
        #             motor_ready = False
        #         else:
        #             motor_ready = True
        #             break

        #     while True:
        #         if motor_ready:
        #             self.motor_cmd.cmd = 5
        #             self.motor_cmd.data = direction 
        #             self.motor_cmd_pub.publish(self.motor_cmd)
        #             while motor_ready:
        #                 current_fb = self.send_request(1)
        #                 if current_fb<threshold1:  
        #                     self.motor_cmd.cmd = 3
        #                     self.motor_cmd.data = torque 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     torque_mode = True
        #                     break
        #             while torque_mode:
        #                 position_fb = self.send_request(2)
        #                 current_fb = self.send_request(1)
        #                 if position_fb>=end_point:
        #                     self.motor_cmd.cmd = 2
        #                     self.motor_cmd.data = 0 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     if current_fb>threshold1:  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
                            
        #                 elif position_fb<=start_point:
        #                     self.motor_cmd.cmd = 2
        #                     self.motor_cmd.data = 0 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     if current_fb<(-threshold1):  
        #                         self.motor_cmd.cmd = 3
        #                         self.motor_cmd.data = torque 
        #                         self.motor_cmd_pub.publish(self.motor_cmd)
                        
        #                 else:  
        #                     self.motor_cmd.cmd = 3
        #                     self.motor_cmd.data = torque 
        #                     self.motor_cmd_pub.publish(self.motor_cmd)
        #                     torque_mode = True
        #                     break

    def send_request(self, a):
        # Prepare the request
        req = SensorFeedback.Request()
        req.sensor = a

        # Send the request
        future = self.sensor_client.call_async(req)
        while rclpy.ok():
            # rclpy.spin_once(self)
            if future.done():
                try:
                    response = future.result()
                    self.get_logger().info(f"Response: {response.data}")
                    break
                except Exception as e:
                    self.get_logger().error(f"Service call failed: {e}")
                    break
        return response.data

    def run(self):
        # Create threads for each function
        update_sensor_thread = threading.Thread(target=self.update_sensor_data)
        access_sensor_thread = threading.Thread(target=self.access_sensor_data)
        # other_task_thread = threading.Thread(target=self.set_passive_mode,args=())

        # Start all threads
        update_sensor_thread.start()
        access_sensor_thread.start()
        # other_task_thread.start()

        # Spin ROS 2 node to handle callbacks
        rclpy.spin(self)

        # Join all threads to main thread
        update_sensor_thread.join()
        access_sensor_thread.join()
        # other_task_thread.join()

def main():
    PORT = '/dev/ttyUSB0' 
    BAUDRATE = 38400  
    TIMEOUT = 0.06  # Timeout in seconds
    rclpy.init()
    node = ApplicationNode(PORT, BAUDRATE, TIMEOUT)
    node.run()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
