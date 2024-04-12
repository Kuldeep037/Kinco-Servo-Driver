from .KincoServoDriver import ServoController
import time

class Apps:
    def __init__(self,port,baudrate,timeout):
        self.controller = ServoController(port,baudrate,timeout)
        self.controller.open_serial_port()
        
    def set_assistive_mode(self,repetitions,start_point,end_point,speed):       # A) Continous Mode
        threshold0 = -24                   # Set start threshold 
        mid_threshold = -2
        threshold1 = -45                   # Set effort threshold
        wait_time = 3                    # Set motor waiting time in second
        direction = 0                    # Motor Direction - no need to change, keep it default
        # speed = 15                       # Set Link motion speed
        
        # repetitions = int(input("how many repeatitions do you want: "))
        # start_point = int(input("Enter the start point: "))
        # end_point = int(input("Enter the end point: "))

        for i in range(repetitions):
            # direction ^= 1
            threshold0 = -threshold0
            threshold1 = -threshold1
            mid_threshold = -mid_threshold
            if threshold0>0 and threshold1>0:
                patient_ready = False
                motor_ready = False
                # Set to starting_point
                while motor_ready==False:
                    position_feedback = self.controller.Read_actual_position()
                    self.controller.set_profile_speed(100)
                    print(position_feedback)
                    if position_feedback!=start_point:
                        print("position_feedback!=start_point")
                        self.controller.set_start_position_mode(start_point)
                        motor_ready = False
                    else:
                        motor_ready = True
                        print("motor is Ready!")

                    #If motor is ready at start point then start the operation 
                    if motor_ready:
                        self.controller.set_profile_speed(speed)
                        while True:
                            current_feedback = self.controller.Read_real_current()
                            print(current_feedback)
                            if current_feedback>threshold0:
                                patient_ready = True
                                print("patient is ready!")
                                break
                        #If patient is ready then start the motion
                        if patient_ready:
                            self.controller.motor_direction(direction)       #set motor in CW direction
                            while patient_ready:
                                current_feedback = self.controller.Read_real_current()
                                position_feedback = self.controller.Read_actual_position()
                                print("current feedback: ", current_feedback)
                                if current_feedback>threshold1:  
                                    self.controller.set_start_position_mode(-end_point)
                                    print("inside the thr1: position: ",position_feedback)

                                elif current_feedback<threshold1 and current_feedback>mid_threshold:
                                    start_time = time.time()
                                    while time.time() - start_time <= wait_time:  # Check sensor for 3 seconds
                                        sensor_value = self.controller.Read_real_current() # Read sensor value
                                        position_feedback = self.controller.Read_actual_position()
                                        self.controller.set_velocity_mode(0)
                                        print("current feedback < threshold value: ",sensor_value)
                                        if sensor_value > threshold1 or position_feedback<=(-end_point):
                                            break
                                    self.controller.set_start_position_mode(-end_point)
                                elif position_feedback<=(-end_point):
                                    self.controller.set_velocity_mode(0)
                                    swap = -start_point
                                    start_point = -end_point
                                    end_point = swap
                                    print(f"ready for next iteration! start point is: {start_point} and end point is: {end_point}")
                                    patient_ready=False

            else:
                patient_ready = False
                motor_ready = False
                # Set to starting_point
                while motor_ready==False:
                    position_feedback = self.controller.Read_actual_position()
                    self.controller.set_profile_speed(100)
                    print(position_feedback)
                    if position_feedback!=start_point:
                        print("position_feedback!=start_point")
                        self.controller.set_start_position_mode(start_point)
                        motor_ready = False
                    else:
                        motor_ready = True
                        print("motor is Ready!")

                    #If motor is ready at start point then start the operation 
                    if motor_ready:
                        self.controller.set_profile_speed(speed)
                        while True:
                            current_feedback = self.controller.Read_real_current()
                            print(current_feedback)
                            if current_feedback<threshold0:
                                patient_ready = True
                                print("patient is ready!")
                                break
                        #If patient is ready then start the motion
                        if patient_ready:
                            self.controller.motor_direction(direction)       #set motor in CW direction
                            while patient_ready:
                                current_feedback = self.controller.Read_real_current()
                                position_feedback = self.controller.Read_actual_position()
                                print("current feedback: ", current_feedback)
                                if current_feedback<threshold1:  
                                    self.controller.set_start_position_mode(-end_point)
                                    print("inside the thr1: position: ",position_feedback)

                                elif current_feedback<threshold1 and current_feedback<(-mid_threshold):
                                    print(f"current feedback: {current_feedback}, -threshold0: {-threshold0}")
                                    start_time = time.time()
                                    while time.time() - start_time <= wait_time:                                # Check sensor for 3 seconds
                                        current_feedback = self.controller.Read_real_current()                  # Read sensor value
                                        position_feedback = self.controller.Read_actual_position()
                                        self.controller.set_velocity_mode(0)
                                        print("current feedback < threshold value: ",sensor_value)
                                        if current_feedback > threshold1 or position_feedback<=(-end_point):
                                            break
                                    self.controller.set_start_position_mode(-end_point)
                                    print("set start position mode executed")
                                    print(f"ready for next iteration! position feedback 1 is: {position_feedback}")
                                elif position_feedback<=(-end_point):
                                    print(f"ready for next iteration! position feedback is: {position_feedback}")
                                    self.controller.set_velocity_mode(0)
                                    swap = -start_point
                                    start_point = -end_point
                                    end_point = swap
                                    print(f"ready for next iteration! start point is: {start_point} and end point is: {end_point}")
                                    patient_ready=False
        return True
    
    def set_passive_mode(self,repetitions,start_point,end_point,speed):      # B) Trigger and Go
        threshold0 = -30                  # Set start threshold 
        threshold1 = -75                  # Set effort threshold
        direction = 0                   # Motor Direction - no need to change, keep it default
        # speed = 15                      # Set Link motion speed in rpm

        # repetitions = int(input("how many repeatitions do you want: "))
        # start_point = int(input("Enter the start point: "))
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
                    while motor_ready==False:
                        position_feedback = self.controller.Read_actual_position()
                        self.controller.set_profile_speed(100)
                        print(position_feedback)
                        if position_feedback!=start_point:
                            self.controller.set_start_position_mode(start_point)
                            motor_ready = False
                        else:
                            motor_ready = True
                            print("motor is Ready!")

                        #If motor is ready at start point then start the operation 
                        if motor_ready:
                            self.controller.set_profile_speed(speed)
                            while True:
                                current_feedback = self.controller.Read_real_current()
                                print(current_feedback)
                                if current_feedback>threshold0:
                                    patient_ready = True
                                    print("patient is ready!")
                                    break
                                    
                            #If patient is ready then start the motion
                            if patient_ready:
                                self.controller.motor_direction(direction)       #set motor in CW direction
                                while patient_ready:
                                    current_feedback = self.controller.Read_real_current()
                                    position_feedback = self.controller.Read_actual_position()
                                    print("current feedback: ", current_feedback, "position: ", position_feedback)
                                    
                                    if current_feedback>threshold1:  
                                        self.controller.set_start_position_mode(-end_point)

                                    elif position_feedback==(-end_point):
                                        self.controller.set_velocity_mode(0)
                                        swap = -start_point
                                        start_point = -end_point
                                        end_point = swap
                                        print("ready for next iteration!")
                                        patient_ready=False

                else:
                    patient_ready = False
                    motor_ready = False
                    # Set to starting_point
                    while motor_ready==False:
                        position_feedback = self.controller.Read_actual_position()
                        self.controller.set_profile_speed(100)
                        print(position_feedback)
                        if position_feedback!=start_point:
                            self.controller.set_start_position_mode(start_point)
                            motor_ready = False
                        else:
                            motor_ready = True
                            print("motor is Ready!")

                        #If motor is ready at start point then start the operation 
                        if motor_ready:
                            self.controller.set_profile_speed(speed)
                            while True:
                                current_feedback = self.controller.Read_real_current()
                                print(current_feedback)
                                if current_feedback<threshold0:
                                    patient_ready = True
                                    print("patient is ready!")
                                    break
                                    
                            #If patient is ready then start the motion
                            if patient_ready:
                                self.controller.motor_direction(direction)       #set motor in CW direction
                                while patient_ready:
                                    current_feedback = self.controller.Read_real_current()
                                    position_feedback = self.controller.Read_actual_position()
                                    print("current feedback: ", current_feedback,"position: ", position_feedback)
                                    
                                    if current_feedback<threshold1:  
                                        self.controller.set_start_position_mode(-end_point)

                                    elif position_feedback==(-end_point):
                                        self.controller.set_velocity_mode(0)
                                        swap = start_point
                                        start_point = -end_point
                                        end_point = -swap
                                        print("ready for next iteration!")
                                        patient_ready=False
        else:
            for i in range(repetitions):
                    # direction ^= 1
                threshold0 = -threshold0
                threshold1 = -threshold1
                
                if threshold0>0 and threshold1>0:
                    patient_ready = False
                    motor_ready = False
                    # Set to starting_point
                    while motor_ready==False:
                        position_feedback = self.controller.Read_actual_position()
                        self.controller.set_profile_speed(100)
                        print(position_feedback)
                        if position_feedback!=start_point:
                            self.controller.set_start_position_mode(start_point)
                            motor_ready = False
                        else:
                            motor_ready = True
                            print("motor is Ready!")

                        #If motor is ready at start point then start the operation 
                        if motor_ready:
                            self.controller.set_profile_speed(speed)
                            while True:
                                current_feedback = self.controller.Read_real_current()
                                print(current_feedback)
                                if current_feedback>threshold0:
                                    patient_ready = True
                                    print("patient is ready!")
                                    break
                                    
                            #If patient is ready then start the motion
                            if patient_ready:
                                self.controller.motor_direction(direction)       #set motor in CW direction
                                while patient_ready:
                                    current_feedback = self.controller.Read_real_current()
                                    position_feedback = self.controller.Read_actual_position()
                                    print("current feedback: ", current_feedback, "position: ", position_feedback)
                                    
                                    if current_feedback>threshold1:  
                                        self.controller.set_start_position_mode(end_point)

                                    elif position_feedback==(end_point):
                                        self.controller.set_velocity_mode(0)
                                        swap = start_point
                                        start_point = end_point
                                        end_point = swap
                                        print("ready for next iteration!")
                                        patient_ready=False

                else:
                    patient_ready = False
                    motor_ready = False
                    # Set to starting_point
                    while motor_ready==False:
                        position_feedback = self.controller.Read_actual_position()
                        self.controller.set_profile_speed(100)
                        print(position_feedback)
                        if position_feedback!=start_point:
                            self.controller.set_start_position_mode(start_point)
                            motor_ready = False
                        else:
                            motor_ready = True
                            print("motor is Ready!")

                        #If motor is ready at start point then start the operation 
                        if motor_ready:
                            self.controller.set_profile_speed(speed)
                            while True:
                                current_feedback = self.controller.Read_real_current()
                                print(current_feedback)
                                if current_feedback<threshold0:
                                    patient_ready = True
                                    print("patient is ready!")
                                    break
                                    
                            #If patient is ready then start the motion
                            if patient_ready:
                                self.controller.motor_direction(direction)       #set motor in CW direction
                                while patient_ready:
                                    current_feedback = self.controller.Read_real_current()
                                    position_feedback = self.controller.Read_actual_position()
                                    print("current feedback: ", current_feedback,"position: ", position_feedback)
                                    
                                    if current_feedback<threshold1:  
                                        self.controller.set_start_position_mode(end_point)

                                    elif position_feedback==(end_point):
                                        self.controller.set_velocity_mode(0)
                                        swap = start_point
                                        start_point = end_point
                                        end_point = swap
                                        print("ready for next iteration!")
                                        patient_ready=False

    def set_resistive_mode(self,repetitions,start_point,end_point,torque):
        threshold0 = 45                  # Set start threshold 
        threshold1 = -45                  # Set effort threshold
        direction = 0                   # Motor Direction - no need to change, keep it default
        speed = 100                     #set homing speed in rpm
        # torque = 9                      #set torque in percentage of rated torque
        # repetitions = int(input("how many repeatitions do you want: "))
        # start_point = int(input("Enter the start point: "))
        # end_point = int(input("Enter the end point: "))
        temp = end_point
        self.controller.motor_direction(direction)
        patient_ready = False
        motor_ready = False
        # Set to starting_point
        while motor_ready==False:
            position_feedback = self.controller.Read_actual_position()
            self.controller.set_profile_speed(speed)
            print(position_feedback)
            if position_feedback!=start_point:
                self.controller.set_start_position_mode(start_point)
                motor_ready = False
            else:
                motor_ready = True
                print("motor is Ready!")

        #If motor is ready at start point then start the operation 
        if motor_ready:
            while True:
                current_feedback = self.controller.Read_real_current()
                print(current_feedback)
                if current_feedback>0:
                    if current_feedback>threshold0:  
                        direction = 0
                        patient_ready = True
                        print("patient is ready!")
                        break
                else:
                    if current_feedback<threshold1: 
                        direction = 1
                        patient_ready = True
                        print("patient is ready!")
                        break
            
            if patient_ready:
                for i in range (repetitions):
                    self.controller.motor_direction(direction)
                    self.controller.set_torque_mode(torque)
                    while True:
                        position_feedback=self.controller.Read_actual_position()
                        current_feedback = self.controller.Read_real_current()
                        print(position_feedback)
                        if position_feedback<=(-end_point):
                            self.controller.set_velocity_mode(0)
                            print(f"position: {position_feedback}, current: {current_feedback}")
                            if current_feedback<=(-threshold0):
                                print("direction changed")
                                direction ^= 1
                                end_point=temp+end_point
                                break

    def Read_position(self):
        position = self.controller.Read_actual_position()
        return position
    
    def Read_current(self):
        current = self.controller.Read_real_current()
        return current
    
    def Read_speed(self):
        speed = self.controller.Read_real_speed()
        return speed
    
    def stop_motor(self):
        self.controller.stop_driver()

            
            