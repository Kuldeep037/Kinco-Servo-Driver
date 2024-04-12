import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
import threading
import time


class SensorController(Node):
    def __init__(self):
        super().__init__('sensor_controller')
        self.sensor_data = {'value': 0}
        self.sensor_data_lock = threading.Lock()

        # ROS 2 Publisher
        self.sensor_publisher = self.create_publisher(Int32, 'sensor_data', 10)

        # ROS 2 Subscriber
        self.sensor_subscriber = self.create_subscription(
            Int32,
            'sensor_command',
            self.sensor_command_callback,
            10)

    def sensor_command_callback(self, msg):
        # Callback for processing sensor commands received from another node
        with self.sensor_data_lock:
            self.sensor_data['value'] = msg.data
        self.get_logger().info('Received sensor command: %d' % msg.data)

    def update_sensor_data(self):
        while True:
            # Simulate updating sensor data
            with self.sensor_data_lock:
                # Publish sensor data
                msg = Int32()
                msg.data = self.sensor_data['value']
                self.sensor_publisher.publish(msg)
                self.get_logger().info('Publishing sensor data: %d' % msg.data)
            time.sleep(1)  # Adjust the update interval as needed

    def access_sensor_data(self):
        while True:
            # Access sensor data
            with self.sensor_data_lock:
                self.get_logger().info('Accessing sensor data: %d' % self.sensor_data['value'])
            time.sleep(2)  # Adjust the access interval as needed

    def other_task(self):
        while True:
            # Simulate performing some other task
            self.get_logger().info('Performing some other task')
            time.sleep(3)  # Adjust the task interval as needed

    def run(self):
        # Create threads for each function
        update_sensor_thread = threading.Thread(target=self.update_sensor_data)
        access_sensor_thread = threading.Thread(target=self.access_sensor_data)
        other_task_thread = threading.Thread(target=self.other_task)

        # Start all threads
        update_sensor_thread.start()
        access_sensor_thread.start()
        other_task_thread.start()

        # Spin ROS 2 node to handle callbacks
        rclpy.spin(self)

        # Join all threads to main thread
        update_sensor_thread.join()
        access_sensor_thread.join()
        other_task_thread.join()


def main():
    rclpy.init()
    sensor_controller = SensorController()
    sensor_controller.run()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
