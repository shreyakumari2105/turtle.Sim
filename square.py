import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time

def main():
    rclpy.init()

    node = Node('draw_square')
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    time.sleep(1)

    for i in range(4):

        # Forward
        msg = Twist()
        msg.linear.x = 2.0

        for j in range(20):
            pub.publish(msg)
            time.sleep(0.1)

        # Turn 90 degrees
        msg = Twist()
        msg.angular.z = 1.57

        for j in range(10):
            pub.publish(msg)
            time.sleep(0.1)

    rclpy.shutdown()

if __name__ == '__main__':
    main()