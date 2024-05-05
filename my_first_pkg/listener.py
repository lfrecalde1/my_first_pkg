#!/usr/bin/env python3

# Import libraries
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsListenerNode (Node):
    def __init__(self):
        super().__init__("Listener")
        self.subscriber_ = self.create_subscription(String, "/robot_name", self.callback_listener, 10)
        self.get_logger().info("Robot listener has been started")
    
    def callback_listener(self, msg):
        print(msg.data)

# main Function
def main(args = None):
    rclpy.init(args= args)
    # Name of the node
    node = RobotNewsListenerNode()

    # Print message through Ros2
    rclpy.spin(node)
    # Do something here
    rclpy.shutdown()

if __name__ == "__main__":
    main()