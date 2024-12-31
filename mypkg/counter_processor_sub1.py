#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class CounterProcessorSub1Node(Node):
    def __init__(self):
        super().__init__('counter_processor_sub1_node')

        # サブスクライバを作成（processed_data トピック）
        self.subscription = self.create_subscription(
            Int16,
            'processed_data',
            self.listener_callback,
            10
        )

        # パブリッシャーを作成（2倍にしたデータを送信）
        self.processed_pub = self.create_publisher(Int16, 'processed_data_doubled', 10)

    def listener_callback(self, msg):
        """受け取ったデータを2倍にして送信"""
        doubled_value = msg.data * 2
        self.get_logger().info(f"Received: {msg.data}, Doubled: {doubled_value}")
        
        # 2倍にしたデータを別のトピックに送信
        doubled_msg = Int16()
        doubled_msg.data = doubled_value
        self.processed_pub.publish(doubled_msg)

def main():
    rclpy.init()
    node = CounterProcessorSub1Node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

