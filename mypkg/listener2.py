import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__('listener')

        # パラメータとして 'mode' を受け取り、対応するトピックを選択
        mode = self.declare_parameter('mode', 'countup').value

        if mode == 'countdown':
            topic_name = 'countdown'
        else:
            topic_name = 'countup'

        self.sub = self.create_subscription(Int16, topic_name, self.cb, 10)

    def cb(self, msg):
        self.get_logger().info(f'Listen: {msg.data}')

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

