import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from arm_interfaces.msg import SensorData
from arm_interfaces.msg import AppParams,MotorCmd,SensorData
import tkinter as tk
from tkinter import ttk
import threading

class MyNode(Node):
    def __init__(self):
        super().__init__('my_node')
        self.publisher = self.create_publisher(String, 'topic', 10)
        self.sensor_data_sub = self.create_subscription(SensorData,'/sensor/data',self.sensor_data_callback,10)
        self.motor_cmd_pub = self.create_publisher(MotorCmd,'/motor/cmd_data',10)
        self.app_mode_pub = self.create_publisher(String,'/app_mode',10)
        self.app_param_pub = self.create_publisher(AppParams,'/apps/params',10)
        self.sensor_data = None
        self.button_pressed = False
        
    def sensor_data_callback(self, msg):
        self.sensor_data = msg

class MyGUI:
    def __init__(self, root, node):
        self.root = root
        self.node = node
        self.dropdown_var = tk.StringVar(root)
        
        self.create_widgets()

    def create_widgets(self):
        # Dropdown Menu
        options = ["1:Assistive Mode", "2:Passive Mode", "3:Resistive Mode"]
        self.dropdown_var.set(options[0])
        dropdown_menu = tk.OptionMenu(self.root, self.dropdown_var, *options, command=self.on_select)
        dropdown_menu.grid(row=0, column=3, padx=10, pady=10)

        #****************************** Entry widgets ******************************
        #===========================================================================
        # Entry 1 : For repetitions
        label1 = tk.Label(self.root, text="Repetitions:")
        label1.grid(row=0, column=0, padx=10, pady=5)

        self.spinbox1 = tk.Spinbox(self.root, from_=0, to=100)
        self.spinbox1.grid(row=0, column=1, padx=10, pady=5)

        # Entry 2 : For Start point
        label2 = tk.Label(self.root, text="Start point:")
        label2.grid(row=1, column=0, padx=10, pady=5)

        self.entry_start_point = tk.IntVar()
        # entry_variable.set(self.update_position())

        self.read_start_point = tk.Entry(self.root,textvariable=self.entry_start_point)
        self.read_start_point.grid(row=1, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.root, text="update", command=self.update_start_position)
        submit_button.grid(row=1,column=2)

        # Entry 3 : For End Point
        label3 = tk.Label(self.root, text="End point:")
        label3.grid(row=2, column=0, padx=10, pady=5)

        self.entry_end_point = tk.IntVar()
        # entry_variable.set(self.update_position())

        self.read_end_point = tk.Entry(self.root,textvariable=self.entry_end_point)
        self.read_end_point.grid(row=2, column=1, padx=10, pady=5)

        submit_button = tk.Button(self.root, text="update", command=self.update_end_position)
        submit_button.grid(row=2,column=2)

        # Entry 4 : For Motion Speed
        label4 = tk.Label(self.root, text="Motion Speed:")
        label4.grid(row=3, column=0, padx=10, pady=5)

        self.spinbox4 = tk.Spinbox(self.root, from_=0, to=3000)
        self.spinbox4.grid(row=3, column=1, padx=10, pady=5)

        # Entry 5 : For Effore/Torque
        label4 = tk.Label(self.root, text="Effort:")
        label4.grid(row=4, column=0, padx=10, pady=5)

        self.spinbox5 = tk.Spinbox(self.root, from_=0, to=3000)
        self.spinbox5.grid(row=4, column=1, padx=10, pady=5)

        # =======================Button Widgets======================= 
        # Run Motor
        self.publish_button = ttk.Button(self.root, text="Run Motor", command=self.submit_action)
        self.publish_button.grid(row=5,column=1)

        # Stop Motor
        stop_button = tk.Button(self.root, text="Stop Motor", command=self.Stop_motor)
        stop_button.grid(row=5,column=0)

        # ========================Sensor Label======================
        # sensor data label
        self.sensor_label = ttk.Label(self.root, text="Sensor Data: ")
        self.sensor_label.grid(row=5,column=4)

        self.update_sensor_data()

    def publish_message(self):
        msg = String()
        msg.data = "Hello ROS2!"
        self.node.publisher.publish(msg)

    def submit_action(self):
        # self.get_values()
        app_param = AppParams()
        app_param.start = float(self.read_start_point.get())
        app_param.end = float(self.read_end_point.get())
        app_param.repeat = int(self.spinbox1.get())
        app_param.speed = int(self.spinbox4.get())
        self.torque = int(self.spinbox5.get())
        self.selected_value = self.dropdown_var.get()
        app_mode = String()
        app_mode.data = self.selected_value
        self.node.app_mode_pub.publish(app_mode)
        self.node.app_param_pub.publish(app_param)

    def update_sensor_data(self):
        if self.node.sensor_data:
            self.sensor_label.config(text=f"Sensor Data: Current: {self.node.sensor_data.current}")
        self.root.after(100, self.update_sensor_data)

    def update_start_position(self):
        self.entry_start_point.set(self.node.sensor_data.position)

    def update_end_position(self):
        # position = self.Read_position()
        self.entry_end_point.set(self.node.sensor_data.position)
        
    def on_select(self,event): 
        print("You Selected:", event)

    def Stop_motor(self):
        # self.stop_motor()
        self.motor_cmd = MotorCmd()
        self.motor_cmd.cmd = 6
        self.motor_cmd.data = 0.0           
        self.node.motor_cmd_pub.publish(self.motor_cmd)
        self.node.button_pressed = True

def main():
    rclpy.init()
    node = MyNode()
    threading.Thread(target=run_gui, args=(node,)).start()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

def run_gui(node):
    root = tk.Tk()
    root.title('ROS2 with Tkinter')
    root.geometry("600x300+10+10")
    my_gui = MyGUI(root, node)
    my_gui.Stop_motor()
    root.mainloop()

if __name__ == '__main__':
    main()
