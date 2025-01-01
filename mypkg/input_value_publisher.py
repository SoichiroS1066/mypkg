#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class CounterPublisherNode(Node):
    def __init__(self):
        super().__init__('counter_publisher_node')

        # パブリッシャを作成（input_data トピック）
        self.publisher = self.create_publisher(Int16, 'input_data', 10)

    def send_input(self, data):
        """入力された内容をサブスクライバへ送る"""
        msg = Int16()
        msg.data = data
        self.get_logger().info(f"[pub] Sending data: {msg.data}")
        self.publisher.publish(msg)

def main():
    rclpy.init()

    publisher_node = CounterPublisherNode()

    # 数字を入力として受け取る
    user_input = int(input("数字を入力してください: "))

    # ユーザーが入力した数字をパブリッシュ
    publisher_node.send_input(user_input)

    # ここでノードをシャットダウン
    rclpy.shutdown()

if __name__ == '__main__':
    main()

