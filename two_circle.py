import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist


class TwoTurtles(Node):

    def __init__(self):
        super().__init__('two_turtles_circle')

        self.pub1 = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.pub2 = self.create_publisher(Twist, '/turtle2/cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.move_turtles)

    def move_turtles(self):
        msg1 = Twist()
        msg2 = Twist()

        # Turtle 1 (Clockwise)
        msg1.linear.x = 2.0
        msg1.angular.z = 1.0

        # Turtle 2 (Anti-clockwise)
        msg2.linear.x = 2.0
        msg2.angular.z = -1.0

        self.pub1.publish(msg1)
        self.pub2.publish(msg2)


def main(args=None):
    rclpy.init(args=args)
    node = TwoTurtles()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()