import struct

rated_torque = 1.27 # Kinco rated max output torque
target_torque = 0.00
torque_op = 0.00
Encoder_resolution = 10000
def get_checksum(registers):
    """Calculate the checksum value for a list of registers."""
    checksum = sum(registers)*(-1)%256
    return checksum

def rpm_to_kinco_val(rpm):
    DEC = rpm * 512 * Encoder_resolution / 1875  # Convert speed in rpm to decimal value of kinco
   
                                                 #Default max speed 50000 rpm
    return (int(DEC))  # Convert DEC to integer before passing to hex() function

def kinco_value_to_reg_value(data):
    first_byte = data & 255                 #Break up the data into separate bytes
    second_byte = (data >> 8) & 255
    third_byte = (data >> 16) & 255
    fourth_byte = (data >> 24) & 255
    return first_byte,second_byte,third_byte,fourth_byte

def rpss_to_kinco_val(rpss):           
    DEC = rpss * 65536 * Encoder_resolution / 1000 / 4000  # Convert acc & dec in rps/s to decimal value of kinco
                                                 
    return (int(DEC)) 
    
def angle_to_kinco_val(angle):
    DEC = angle/360 * Encoder_resolution    #Converts number of rotations to encoder counts
    
    return (int(DEC))

def target_torque_to_kinco_value(target_torque):                    #convert required o/p torque to kinco Value
    # torque_op = ( target_torque / rated_torque ) * 100
    torque_op = (rated_torque*target_torque)/100
    return torque_op
    
def calculate_checksum_for_feedback(hex_data):
    bytes_list = [int(hex_data[i:i+2], 16) for i in range(0, len(hex_data), 2)]     # Split the hex data into bytes
    bytes_list.pop()        # Remove the last byte
    checksum = sum(bytes_list)      # Calculate checksum

    # Take two's complement
    checksum = checksum & 0xFF  # Ensure checksum is within one byte
    checksum = (~checksum + 1) & 0xFF  # Take two's complement
    return checksum

def verify_feedback(data):
    recieved_checksum = data[-2:]
    calculate_checksum = calculate_checksum_for_feedback(data)
    recieved_checksum = int(recieved_checksum,16)
    if recieved_checksum==calculate_checksum:
        return True
    else:
        return False
    
def get_angular_position_feedback(byte_data,feedback):
    """sensor_count_hex = feedback[10:18]
    bytes_in_reverse_order = [sensor_count_hex[i:i+2] for i in range(0, len(sensor_count_hex), 2)][::-1]
    reversed_hex_data = "".join(bytes_in_reverse_order)
    sensor_count_int = int(reversed_hex_data,16)
    revolutions = sensor_count_int/Encoder_resolution
    degrees1 = (revolutions*360) """

    subset_bytes = byte_data[4:8]
    # print(subset_bytes)
    # hex_bytes = bytes(subset_bytes)
    # print(subset_bytes)
    sensor_count = struct.unpack('<i', subset_bytes)[0]
    # print(sensor_count)
    encoder_count = sensor_count>>8
    # print(encoder_count)
    # encoder_value = my_data & 0x0000FFFF
    # angle = (sensor_count*1875)/(512*Encoder_resolution)
    degrees2 = encoder_count*360/Encoder_resolution
    # print(degrees2)
    return int(round(degrees2,1))
    
def get_current_feedback(byte_data,feedback):
    """current_feedback_hex = feedback[10:18]
    bytes_in_reverse_order = [current_feedback_hex[i:i+2] for i in range(0, len(current_feedback_hex), 2)][::-1]
    reversed_hex_data = "".join(bytes_in_reverse_order)
    dec = int(reversed_hex_data,16)
    arms = dec/((2014*1.414)/30.3)
    arms = 10*arms
    if arms>100:
        arms = dec & 0x0000FFFF
        arms = -arms/((2014*1.414)/30.3)
"""
    subset_bytes = byte_data[4:8]
    # print(subset_bytes)
    hex_bytes = bytes(subset_bytes)
    signed_int = struct.unpack('<i', hex_bytes)[0]
    sensor_value = signed_int>>8
    arms = (sensor_value/((2014*1.414)/30.3))*100   #30.3
    return float(arms)
    
def get_speed_feedback(byte_data,feedback):
    """speed_feedback_hex = feedback[10:18]
    bytes_in_reverse_order = [speed_feedback_hex[i:i+2] for i in range(0, len(speed_feedback_hex), 2)][::-1]
    reversed_hex_data = "".join(bytes_in_reverse_order)
    speed = int(reversed_hex_data,16)
    rpm = (speed*1875)/(512*Encoder_resolution)"""

    subset_bytes = byte_data[4:8]
    # print(subset_bytes)
    hex_bytes = bytes(subset_bytes)
    speed = struct.unpack('<i', hex_bytes)[0]
    sensor_value = speed>>8
    rpm = (sensor_value*1875)/(512*Encoder_resolution)
    return int(rpm)