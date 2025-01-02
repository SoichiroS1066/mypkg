#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class response_node(Node):
    def __init__(self):
        super().__init__('response_node')
        self.str_subscriber = self.create_subscription(String, 'input_string', self.listener_callback, 10)
        self.get_logger().info("Response Node is running...")

    def listener_callback(self, msg):
        user_input = msg.data
        response = self.generate_response(user_input)
        self.get_logger().info(f"Received: {user_input}")
        self.get_logger().info(f"Response: {response}")

    def generate_response(self, user_input):
        # 挨拶に対する処理
        if user_input == "おはようございます":
            return "おはようございます"
        elif user_input == "こんにちは":
            return "こんにちは"
        elif user_input == "こんばんは":
            return "こんばんは"
        elif user_input == "こんにちは!":
            return "こんにちは!"

        # 記号に関する処理
        elif user_input.startswith("(") and user_input.endswith(")"):
            return user_input

        # 文末に記号がついている場合
        elif user_input.endswith("！"):
            return user_input

        # その他の入力
        return user_input

def main():
    rclpy.init()
    response_node = ResponseNode()

    rclpy.spin(response_node)

    rclpy.shutdown()

if __name__ == '__main__':
    main()

