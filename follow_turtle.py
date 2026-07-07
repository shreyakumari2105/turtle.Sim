import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from turtlesim.srv import Spawn
import math

class CircleFollower(Node):

    def __init__(self):
        super().__init__('circle_follower')

        self.leader_pose = None
        self.follower_pose = None
        self.path = []

        # Spawn turtle2
        client = self.create_client(Spawn, '/spawn')
        while not client.wait_for_service(timeout_sec=1.0):
            pass

        req = Spawn.Request()
        req.x = 3.0
        req.y = 5.5
        req.theta = 0.0
        req.name = "turtle2"

        future = client.call_async(req)
        rclpy.spin_until_future_complete(self, future)

        self.create_subscription(Pose,
                                 '/turtle1/pose',
                                 self.leader_callback,
                                 10)

        self.create_subscription(Pose,
                                 '/turtle2/pose',
                                 self.follower_callback,
                                 10)

        self.pub1 = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10)

        self.pub2 = self.create_publisher(
            Twist,
            '/turtle2/cmd_vel',
            10)

        self.timer = self.create_timer(0.05, self.move)

    def leader_callback(self,msg):
        self.leader_pose = msg
        self.path.append((msg.x,msg.y))

        if len(self.path) > 500:
            self.path.pop(0)

    def follower_callback(self,msg):
        self.follower_pose = msg

    def move(self):

        leader = Twist()
        leader.linear.x = 2.0
        leader.angular.z = 1.0
        self.pub1.publish(leader)

        if self.follower_pose is None:
            return

        if len(self.path) < 60:
            return

        target = self.path[-60]

        dx = target[0]-self.follower_pose.x
        dy = target[1]-self.follower_pose.y

        distance = math.sqrt(dx*dx+dy*dy)

        angle = math.atan2(dy,dx)

        error = angle-self.follower_pose.theta

        while error > math.pi:
            error -= 2*math.pi

        while error < -math.pi:
            error += 2*math.pi

        follower = Twist()

        follower.linear.x = min(2.5, distance)
        follower.angular.z = 6*error

        self.pub2.publish(follower)


def main():
    rclpy.init()

    node = CircleFollower()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()

if __name__ == '__main__':
    main()