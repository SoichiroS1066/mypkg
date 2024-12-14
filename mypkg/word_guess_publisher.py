#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import random

class WordGuessPublisher(Node):
    def __init__(self):
        super().__init__('word_guess_publisher')
        self.publisher_ = self.create_publisher(String, 'game_word', 10)
        self.words = ['apple', 'banana', 'cherry', 'date', 'fig', 'grape']
        self.timer = self.create_timer(10.0, self.publish_word)
        self.get_logger().info('WordGuessPublisher initialized.')

    def publish_word(self):
        word = random.choice(self.words)
        self.publisher_.publish(String(data=word))
        self.get_logger().info(f'Published word: {word}')

def main():
    rclpy.init()
    node = WordGuessPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()

