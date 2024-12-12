import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DeclareNumberSubscriber(Node):
    def __init__(self):
        super().__init__('declare_number_sub')
        self.create_subscription(String, 'player_a_turn', self.player_a_callback, 10)
        self.create_subscription(String, 'player_b_turn', self.player_b_callback, 10)
        self.player_a_passes = 0
        self.player_b_passes = 0

    def player_a_callback(self, msg):
        self.get_logger().info(f"Received from Player A: {msg.data}")
        if "pass" in msg.data.lower():
            self.player_a_passes += 1
            if self.player_a_passes > 3:
                self.get_logger().info("Player A cannot pass anymore.")
        else:
            # プレイヤーAが宣言した場合の処理
            pass

    def player_b_callback(self, msg):
        self.get_logger().info(f"Received from Player B: {msg.data}")
        if "pass" in msg.data.lower():
            self.player_b_passes += 1
            if self.player_b_passes > 3:
                self.get_logger().info("Player B cannot pass anymore.")
        else:
            # プレイヤーBが宣言した場合の処理
            pass

def main(args=None):
    rclpy.init(args=args)
    subscriber_node = DeclareNumberSubscriber()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

