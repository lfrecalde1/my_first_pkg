#!/usr/bin/env python3

# Import libraries
import rclpy
from rclpy.node import Node
class MyNode (Node):
    def __init__(self):
        super().__init__("py_test")
        self.get_logger().info("Create Class Ros2")
        self.counter_ = 0
        self.create_timer(0.5, self.timer_callback)
    def timer_callback(self):
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ = self.counter_+ 1
# main Function
def main(args = None):
    rclpy.init(args= args)
    # Name of the node
    node = MyNode()

    # Print message through Ros2
    rclpy.spin(node)
    # Do something here
    rclpy.shutdown()

if __name__ == "__main__":
    main()