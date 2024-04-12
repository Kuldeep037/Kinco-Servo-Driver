import rclpy
from rclpy.node import Node
# from std_msgs.msg import String
from arm_interfaces.msg import SensorData

class MySubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber')
        self.subscription = self.create_subscription(SensorData, '/sensor/data', self.sensor_callback, 10)
        self.subscription  # prevent unused variable warning

    def sensor_callback(self, msg):
        self.current_feedback = msg.current
        self.position_feedback = msg.position
        self.velocity_feedback = msg.velocity
        return self.current_feedback, self.position_feedback, self.velocity_feedback
    
    def sensor_data(self):
        # current = self.current_feedback
        # position = self.position_feedback
        # velocity = self.position_feedback
        return self.current_feedback,self.position_feedback,self.position_feedback


def main(args=None):
    rclpy.init(args=args)

    node = MySubscriber()
    
    rclpy.spin(node)
    current,position,velocity = node.sensor_data()
    print(f"self.current_feedback: {current}")
    print(f"self.position_feedback: {position}")
    print(f"self.velocity_feedback: {velocity}")
    
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
