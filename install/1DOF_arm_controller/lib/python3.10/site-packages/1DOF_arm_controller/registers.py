    
class ServoFD124:
    motor_id = 0x01
    CONTROL_WORD = {
        "R/W": {
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        },
        "Address": [0x0040, 0x0060],
        "Value": {
            "Stop": 0x0006,
            "Start": 0x000F,
            "Reset": 0x0080,
            "QuickStop": 0x000B,
            "AbsolutePosition": {
                "Set1": 0x002F,
                "Set2": 0x003F
            },
            "RelativePosition": {
                "Set1": 0x004F,
                "Set2": 0x005F
            },
            "StartAbsolutePosition": [0x003F,0x0010],
            "Homing": {
                "Set1": 0x000F,
                "Set2": 0x001F
            }
        }
    }

    STATUS = {"R/W": {
        "R": 0x0040
        }, "Address": [0x0041, 0x0060]}

    OPMODE = {
        "R/W": {
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        },
        "Address": [0x60, 0x60],
        "Value": {
            "Position": 0x0001,
            "Velocity": 0x0003,
            "Torque": 0x0004,
            "Home": 0x0006,
        }
    }

    VelocityDirection = {
        "R/W": {
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        },
        "Address": [0x007E, 0x0060],
        "Value": {
            "CCW": 0,
            "CW": 1
        }
    }
    

    ProfileSpeed_PC = {"R/W":  { ## FOR POSITION CONTROL
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        }, "Address": [0x81, 0x60]}

   # VelocityFeedback = {"R/W": "R", "Register": 0x3B00, "read_length": 2}

    PositionCommand = { "R/W":{
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        }, "Address": [0x7A, 0x60]}

    TargetSpeed_VC = {"R/W":  { ## FOR VELOCITY CONTROL
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        }, "Address": [0xFF, 0x60]}

  #  PositionFeedback = {"R/W": "R", "Register": 0x3700, "read_length": 2}

    ProfileAcceleration = {"R/W":  { ## default:610.352 rps/s
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        }, "Address": [0x83, 0x60]}

    TorqueCommand = { "R/W":{
            "W_1by": 0x002F,
            "W_2by": 0x002B,
            "W_4by": 0x0023
        }, "Address": [0x71, 0x60]}
    
    Feedback = {"R/W":  { ## FOR feedback values speed, current, position
            "R": 0x0040
        }, "Address":{
                "Real_speed": [0x6C, 0x60],
                "Real_current": [0x78, 0x60],
                "Pos_Actual": [0x63, 0x60]
        } }
    MotorDirection = {"R/W":  { ## FOR feedback values speed, current, position
                "W_1by": 0x002F,
                "W_2by": 0x002B,
                "W_4by": 0x0023
        }, "Address":[0x7E,0x60],
            "Value":{
                 "CCW":0x00,
                 "CW":0x01
        }
                
        } 