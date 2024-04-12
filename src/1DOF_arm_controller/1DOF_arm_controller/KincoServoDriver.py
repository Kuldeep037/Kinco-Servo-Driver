import serial
from .registers import ServoFD124 as Servo
import time
from .calculations import (get_checksum, angle_to_kinco_val, rpm_to_kinco_val, 
                          target_torque_to_kinco_value,kinco_value_to_reg_value,
                          rpss_to_kinco_val,verify_feedback, get_angular_position_feedback,
                          get_current_feedback, get_speed_feedback)
class ServoController:
    def __init__(self, port, baudrate, timeout):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.ser = None

    def open_serial_port(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            if self.ser.is_open:
                print(f"Serial port {self.port} opened successfully.")
            else:
                print(f"Failed to open serial port {self.port}.")
                exit()
        except serial.SerialException as e:
            print(f"Error: {e}")
            exit()
        
    def close_serial_port(self):
        if self.ser:
            self.ser.close()

    def send_data(self, data):
        if self.ser:
            
            try:
                self.ser.write(data)
                # self.ser.flushInput()
            except serial.SerialException as e:
                print(f"Error while sending data: {e}")
                exit()

    def receive_response(self, num_bytes):
        if self.ser:
            try:
                data = self.ser.read(num_bytes)
                # data = self.ser.readline().strip()
                # print(data)
                if data:
                    # If decoding fails, treat data as binary
                    decoded_data = data.hex()
                    # data_list = [byte for byte in data]
                return data,decoded_data
                
            except serial.SerialException as e:
                print(f"Error while receiving response: {e}")
                exit()
        return None

    def parse_response(self, response):
        hex_data = response  # Example hexadecimal data

        # Extract the last 3 bytes
        last_three_bytes_hex = hex_data[-4:]  # Extract last 6 characters representing 3 bytes
        decimal_value = int(last_three_bytes_hex, 16)  # Convert the last 3 bytes to decimal

        print("Hex:", last_three_bytes_hex, "Decimal:", decimal_value)

    def set_start_position_mode(self, target_angle):
        control_word = [Servo.motor_id,
                         Servo.CONTROL_WORD["R/W"]["W_2by"],
                         Servo.CONTROL_WORD["Address"][0],
                         Servo.CONTROL_WORD["Address"][1],
                         0x00,
                         Servo.CONTROL_WORD["Value"]["StartAbsolutePosition"][0],
                         Servo.CONTROL_WORD["Value"]["StartAbsolutePosition"][1],
                         0x00,
                         0x00,
                         ] 
        cont_checksum = get_checksum(control_word)
        control_word.append(cont_checksum)

        op_mode = [Servo.motor_id,
                         Servo.OPMODE["R/W"]["W_1by"],
                         Servo.OPMODE["Address"][0],
                         Servo.OPMODE["Address"][1],
                         0x00,
                         Servo.OPMODE["Value"]["Position"],
                         0x00,
                         0x00,
                         0x00,
                         ]
        op_checksum = get_checksum(op_mode)
        op_mode.append(op_checksum)

        temp1 = angle_to_kinco_val(target_angle) #convert the target position from rotations to kinco value
        first_byte = temp1 & 255                 #Break up the data into separate bytes
        second_byte = (temp1 >> 8) & 255
        third_byte = (temp1 >> 16) & 255
        fourth_byte = (temp1 >> 24) & 255

        target_pos = [Servo.motor_id,
                        Servo.PositionCommand["R/W"]["W_4by"],
                        Servo.PositionCommand["Address"][0],
                        Servo.PositionCommand["Address"][1],
                        0x00,
                        first_byte,
                        second_byte,
                        third_byte,
                        fourth_byte,
                        ]
        target_pos_checksum = get_checksum(target_pos)
        target_pos.append(target_pos_checksum)

        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        

        self.send_data(op_mode)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        
        self.send_data(target_pos)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
               
    def abs_position_mode(self, profile_speed, target_position):
        control_word1 = [Servo.motor_id,                             #Set control word to 2F
                         Servo.CONTROL_WORD["R/W"]["W_2by"],
                         Servo.CONTROL_WORD["Address"][0],
                         Servo.CONTROL_WORD["Address"][1],
                         0x00,
                         Servo.CONTROL_WORD["Value"]["AbsolutePosition"]["Set1"],
                         0x00,
                         0x00,
                         0x00,
                         #checkSUM
                         ]
        ctrl_checksum1 = get_checksum(control_word1)
        control_word1.append(ctrl_checksum1)

        op_mode = [Servo.motor_id,                                  #Set Operation mode to position control
                         Servo.OPMODE["R/W"]["W_1by"],
                         Servo.OPMODE["Address"][0],
                         Servo.OPMODE["Address"][1],
                         0x00,
                         Servo.OPMODE["Value"]["Position"],
                         0x00,
                         0x00,
                         0x00,
                         #checkSUM
                         ]
        op_mode_checksum = get_checksum(op_mode)
        op_mode.append(op_mode_checksum)                
                        
        temp1 = angle_to_kinco_val(target_position) #convert the target position from rotations to kinco value
        first_byte = temp1 & 255                 #Break up the data into separate bytes
        second_byte = (temp1 >> 8) & 255
        third_byte = (temp1 >> 16) & 255
        fourth_byte = (temp1 >> 24) & 255              
        target_pos = [Servo.motor_id,
                        Servo.PositionCommand["R/W"]["W_4by"],
                        Servo.PositionCommand["Address"][0],
                        Servo.PositionCommand["Address"][1],
                        0x00,
                        first_byte,
                        second_byte,
                        third_byte,
                        fourth_byte,
                        #checkSUM
                        ]
        target_pos_checksum = get_checksum(target_pos)
        target_pos.append(target_pos_checksum)
                        
        temp2 = rpm_to_kinco_val(profile_speed) #convert profile speed from rpm to kinco counts
        first_byte = temp2 & 255                 #Break up the data into separate bytes
        second_byte = (temp2 >> 8) & 255
        third_byte = (temp2 >> 16) & 255
        fourth_byte = (temp2 >> 24) & 255
        target_speed = [Servo.motor_id,         #communicate data about profile speed
                        Servo.ProfileSpeed_PC["R/W"]["W_4by"],
                        Servo.ProfileSpeed_PC["Address"][0],
                        Servo.ProfileSpeed_PC["Address"][1],
                        0x00,
                        first_byte,
                        second_byte,
                        third_byte,
                        fourth_byte,
                        
                    ]
        target_speed_checksum = get_checksum(target_speed)
        target_speed.append(target_speed_checksum)
        
        control_word2 = [Servo.motor_id,                             #Set control word to 3F to start
                         Servo.CONTROL_WORD["R/W"]["W_2by"],
                         Servo.CONTROL_WORD["Address"][0],
                         Servo.CONTROL_WORD["Address"][1],
                         0x00,
                         Servo.CONTROL_WORD["Value"]["AbsolutePosition"]["Set2"],
                         0x00,
                         0x00,
                         0x00,
                         #checkSUM
                         ]
        ctrl_checksum2 = get_checksum(control_word2)
        control_word2.append(ctrl_checksum2)

        self.send_data(control_word1)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
                                      
        self.send_data(op_mode)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        
        self.send_data(target_pos)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        
        self.send_data(target_speed)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        
        self.send_data(control_word2)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
    def set_velocity_mode(self,target_rpm):
        control_word = [Servo.motor_id,
                         Servo.CONTROL_WORD["R/W"]["W_1by"],
                         Servo.CONTROL_WORD["Address"][0],
                         Servo.CONTROL_WORD["Address"][1],
                         0x00,
                         Servo.CONTROL_WORD["Value"]["Start"],
                         0x00,
                         0x00,
                         0x00,
                         ] 
        ctrl_word_checksum = get_checksum(control_word)
        control_word.append(ctrl_word_checksum)

        op_mode = [Servo.motor_id,
                         Servo.OPMODE["R/W"]["W_1by"],
                         Servo.OPMODE["Address"][0],
                         Servo.OPMODE["Address"][1],
                         0x00,
                         Servo.OPMODE["Value"]["Velocity"],
                         0x00,
                         0x00,
                         0x00,
                         ]
        op_mode_checksum = get_checksum(op_mode)
        op_mode.append(op_mode_checksum)
        
        temp1 = rpm_to_kinco_val(target_rpm) #convert profile speed from rpm to kinco counts
        first_byte = temp1 & 255                 #Break up the data into separate bytes
        second_byte = (temp1 >> 8) & 255
        third_byte = (temp1 >> 16) & 255
        fourth_byte = (temp1 >> 24) & 255
        target_speed = [Servo.motor_id,
                         Servo.TargetSpeed_VC["R/W"]["W_4by"],
                         Servo.TargetSpeed_VC["Address"][0],
                         Servo.TargetSpeed_VC["Address"][1],
                         0x00,
                         first_byte,
                         second_byte,
                         third_byte,
                         fourth_byte,
                         ]
        target_speed_checksum = get_checksum(target_speed)
        target_speed.append(target_speed_checksum)

        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        self.send_data(op_mode)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        self.send_data(target_speed)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
    def set_torque_mode(self,target_torque):
        control_word = [Servo.motor_id,
                         Servo.CONTROL_WORD["R/W"]["W_1by"],
                         Servo.CONTROL_WORD["Address"][0],
                         Servo.CONTROL_WORD["Address"][1],
                         0x00,
                         Servo.CONTROL_WORD["Value"]["Start"],
                         0x00,
                         0x00,
                         0x00,
                         ] 
        ctrl_word_checksum = get_checksum(control_word)
        control_word.append(ctrl_word_checksum)

        op_mode = [Servo.motor_id,                                  #Set Operation mode to position control
                         Servo.OPMODE["R/W"]["W_1by"],
                         Servo.OPMODE["Address"][0],
                         Servo.OPMODE["Address"][1],
                         0x00,
                         Servo.OPMODE["Value"]["Torque"],
                         0x00,
                         0x00,
                         0x00,
                         #checkSUM
                         ]
        op_mode_checksum = get_checksum(op_mode)
        op_mode.append(op_mode_checksum)

        temp = target_torque_to_kinco_value(target_torque)
        torque_op =  [Servo.motor_id,                                  #Set Operation mode to position control
                         Servo.TorqueCommand["R/W"]["W_1by"],
                         Servo.TorqueCommand["Address"][0],
                         Servo.TorqueCommand["Address"][1],
                         0x00,
                         target_torque,
                         0x00,
                         0x00,
                         0x00,
                         #checkSUM
                         ]
        torque_op_checksum = get_checksum(torque_op)
        torque_op.append(torque_op_checksum)

        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        self.send_data(op_mode)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
        self.send_data(torque_op)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
    
    def set_profile_speed(self,profile_speed):     
        temp = rpm_to_kinco_val(profile_speed)
        data1,data2,data3,data4 = kinco_value_to_reg_value(temp)
        
        profile_speed = [Servo.motor_id,
                         Servo.ProfileSpeed_PC["R/W"]["W_4by"],
                         Servo.ProfileSpeed_PC["Address"][0],
                         Servo.ProfileSpeed_PC["Address"][1],
                         0x00,
                         data1,
                         data2,
                         data3,
                         data4,
                         ]
        prof_speed_ckeksum = get_checksum(profile_speed)
        profile_speed.append(prof_speed_ckeksum)
        self.send_data(profile_speed)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
    def set_max_speed(self,maximum_speed):
        temp = rpm_to_kinco_val(maximum_speed)
        data1,data2,data3,data4 = kinco_value_to_reg_value(temp)
        
        max_speed = [Servo.motor_id,
                         Servo.OPMODE["R/W"]["W_1by"],
                         Servo.OPMODE["Address"][0],
                         Servo.OPMODE["Address"][1],
                         0x00,
                         data1,
                         data2,
                         data3,
                         data4,
                         ]
        speed_cheksum = get_checksum(max_speed)
        max_speed.append(speed_cheksum)
        self.send_data(max_speed)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
    def set_acc_and_dcc(self,acc,dcc): 
        temp = rpss_to_kinco_val(acc)
        data1,data2,data3,data4 = kinco_value_to_reg_value(temp)   
        profile_acc = [Servo.motor_id,
                         Servo.ProfileAcceleration["R/W"]["W_4by"],
                         Servo.ProfileAcceleration["Address"][0],
                         Servo.ProfileAcceleration["Address"][1],
                         0x00,
                         data1,
                         data2,
                         data3,
                         data4,
                         ]
        speed_cheksum = get_checksum(profile_acc)
        profile_acc.append(speed_cheksum)
        self.send_data(profile_acc)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        

        temp = rpss_to_kinco_val(dcc)
        data1,data2,data3,data4 = kinco_value_to_reg_value(temp) 
        profile_dcc = [Servo.motor_id,
                         Servo.OPMODE["R/W"]["W_1by"],
                         Servo.OPMODE["Address"][0],
                         Servo.OPMODE["Address"][1],
                         0x00,
                         data1,
                         data2,
                         data3,
                         data4,
                         ]
        speed_cheksum = get_checksum(profile_dcc)
        profile_dcc.append(speed_cheksum)
        self.send_data(profile_dcc)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
      
    def reset_driver(self):
        control_word = [Servo.motor_id,
                            Servo.CONTROL_WORD["R/W"]["W_1by"],
                            Servo.CONTROL_WORD["Address"][0],
                            Servo.CONTROL_WORD["Address"][1],
                            0x00,
                            Servo.CONTROL_WORD["Value"]["Reset"],
                            0x00,
                            0x00,
                            0x00,
                            ] 
        ctrl_word_checksum = get_checksum(control_word)
        control_word.append(ctrl_word_checksum)
        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
    def stop_driver(self):
        control_word = [Servo.motor_id,
                            Servo.CONTROL_WORD["R/W"]["W_1by"],
                            Servo.CONTROL_WORD["Address"][0],
                            Servo.CONTROL_WORD["Address"][1],
                            0x00,
                            Servo.CONTROL_WORD["Value"]["Stop"],
                            0x00,
                            0x00,
                            0x00,
                            ] 
        ctrl_word_checksum = get_checksum(control_word)
        control_word.append(ctrl_word_checksum)
        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
         
    def start_driver(self):
        control_word = [Servo.motor_id,
                            Servo.CONTROL_WORD["R/W"]["W_1by"],
                            Servo.CONTROL_WORD["Address"][0],
                            Servo.CONTROL_WORD["Address"][1],
                            0x00,
                            Servo.CONTROL_WORD["Value"]["Start"],
                            0x00,
                            0x00,
                            0x00,
                            ] 
        ctrl_word_checksum = get_checksum(control_word)
        control_word.append(ctrl_word_checksum)
        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
        
    def motor_direction(self,direction):
        motor_direction =[Servo.motor_id,
                         Servo.MotorDirection["R/W"]["W_1by"],
                         Servo.MotorDirection["Address"][0],
                         Servo.MotorDirection["Address"][1],
                         0x00,
                         direction,
                         0x00,
                         0x00,
                         0x00,
                         ]
        temp_checksum = get_checksum(motor_direction)
        motor_direction.append(temp_checksum)
        self.send_data(motor_direction)
        byte_data,hex_data = self.receive_response(10)
        verify = verify_feedback(hex_data)
          

###################FeedBack Section##########################
        
    def Read_actual_position(self):
        control_word = [Servo.motor_id,                             
                         Servo.Feedback["R/W"]["R"],
                         Servo.Feedback["Address"]["Pos_Actual"][0],
                         Servo.Feedback["Address"]["Pos_Actual"][1],
                         0x00,
                         0x00,
                         0x00,
                         0x00,
                         0x00,
                         
                         ]
        control_word_checksum = get_checksum(control_word)
        control_word.append(control_word_checksum)
        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        position = get_angular_position_feedback(byte_data,hex_data)
        return position
                                             
    def Read_real_current(self):
        control_word = [Servo.motor_id,                             
                         Servo.Feedback["R/W"]["R"],
                         Servo.Feedback["Address"]["Real_current"][0],
                         Servo.Feedback["Address"]["Real_current"][1],
                         0x00,
                         0x00,
                         0x00,
                         0x00,
                         0x00,
                         #checkSUM
                         ]
        control_word_checksum = get_checksum(control_word)
        control_word.append(control_word_checksum)
        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        current = get_current_feedback(byte_data,hex_data)
        return current
                        
    def Read_real_speed(self):
        control_word = [Servo.motor_id,                             
                         Servo.Feedback["R/W"]["R"],
                         Servo.Feedback["Address"]["Real_speed"][0],
                         Servo.Feedback["Address"]["Real_speed"][1],
                         0x00,
                         0x00,
                         0x00,
                         0x00,
                         0x00,
                         #checkSUM
                         ]
        control_word_checksum = get_checksum(control_word)
        control_word.append(control_word_checksum)
        self.send_data(control_word)
        byte_data,hex_data = self.receive_response(10)
        speed = get_speed_feedback(byte_data,hex_data)
        return speed
        
   
