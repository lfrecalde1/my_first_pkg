#!/usr/bin/env python3

# Import libraries
import rclpy
from rclpy.node import Node
from example_interfaces.msg import String

class RobotNewsStationNode (Node):
    def __init__(self):
        super().__init__("robot_news_station")
        self.publishers_ = self.create_publisher(String, "robot_name", 10)
        self.get_logger().info("Robot Nes Station has been started")
        self.timer_ = self.create_timer(0.1, self.publish_news)
        self.conter_ = 0


    def publish_news(self):
        msg = String()
        self.conter_ = self.conter_ + 1 
        msg.data = "Fer " + str(self.conter_)
        self.get_logger().info("Publishing Message")
        self.publishers_.publish(msg)
    

# main Function
def main(args = None):
    rclpy.init(args= args)
    # Name of the node
    node = RobotNewsStationNode()

    # Print message through Ros2
    rclpy.spin(node)
    # Do something here
    rclpy.shutdown()

if __name__ == "__main__":
    main()