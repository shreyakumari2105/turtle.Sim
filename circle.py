import rclpy
from rclpy.node import Node 
from geometry_msgs.msg import Twist
import time

def main():
    rclpy.init()

    node = Node('draw_circle')
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    msg = Twist()
    msg.linear.x = 2.0
    msg.angular.z = 1.0

    for i in range(100):
        pub.publish(msg)
        time.sleep(0.1)

    rclpy.shutdown()

if __name__ == '__main__':
    main()
