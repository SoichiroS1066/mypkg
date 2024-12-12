import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class DeclareNumberPublisher(Node):
    def __init__(self):
        super().__init__('declare_number_pub')
        self.player_a_pub = self.create_publisher(String, 'player_a_turn', 10)
        self.player_b_pub = self.create_publisher(String, 'player_b_turn', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.current_number = 1
        self.turn = 'A'  # プレイヤーAから開始

    def timer_callback(self):
        msg = String()
        if self.turn == 'A':
            msg.data = f"Player A: {self.current_number}"
            self.player_a_pub.publish(msg)
            self.turn = 'B'
        else:
            msg.data = f"Player B: {self.current_number}"
            self.player_b_pub.publish(msg)
            self.turn = 'A'

        self.current_number += 1
        if self.current_number > 10:
            self.get_logger().info("Game Over!")
            rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    publisher_node = DeclareNumberPublisher()
    rclpy.spin(publisher_node)
    publisher_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

