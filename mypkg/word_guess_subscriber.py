#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WordGuessSubscriber(Node):
    def __init__(self):
        super().__init__('word_guess_subscriber')
        self.subscription = self.create_subscription(
            String,
            'game_word',
            self.listener_callback,
            10
        )
        self.subscription  # prevent unused variable warning
        self.get_logger().info('WordGuessSubscriber initialized.')

    def listener_callback(self, msg):
        word = msg.data
        self.get_logger().info(f'Received word: {word}')
        if word.startswith('a'):
            self.get_logger().info(f'This word starts with "A": {word}')

def main():
    rclpy.init()
    node = WordGuessSubscriber()  # 修正: WordGuessPublisher ではなく WordGuessSubscriber を使う
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

