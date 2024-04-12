import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts  # Import the service message type

class MyServiceServer(Node):
    def __init__(self):
        super().__init__('my_service_server')  # Name your node

        # Create the service
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.add_two_ints_callback)

    def add_two_ints_callback(self, request, response):
        # This function will be called whenever the service is requested
        response.sum = request.a + request.b
        self.get_logger().info(f"Received a service request: {request.a} + {request.b}")
        return response

def main(args=None):
    rclpy.init(args=args)
    my_service_server = MyServiceServer()
    rclpy.spin(my_service_server)  # Keep the node running until shutdown
    rclpy.shutdown()

if __name__ == '__main__':
    main()
