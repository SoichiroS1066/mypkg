#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String

class CounterProcessorNode(Node):
    def __init__(self):
        super().__init__('counter_processor_node')

        # モードと初期値のパラメータを取得
        self.mode = self.declare_parameter('mode', 'countup').value
        self.start_value = self.declare_parameter('start_value', 10).value

        self.get_logger().info(f"Processor mode: {self.mode}, Start value: {self.start_value}")

        # カウント変数を初期化
        self.value = self.start_value

        # パブリッシャーを作成（成果物用のトピック）
        self.processed_pub = self.create_publisher(Int16, 'processed_data', 10)

        # サブスクライバを作成（入力データのトピック）
        self.input_sub = self.create_subscription(
            String,
            'input_data',
            self.input_callback,
            10
        )

        # 内部タイマーで生成を行う
        self.timer = self.create_timer(1.0, self.generate_data)

    def input_callback(self, msg):
        """サブスクライバのコールバック関数: 新しいモードまたは開始値の受け取り"""
        if msg.data == 'countup':
            self.mode = 'countup'
        elif msg.data == 'countdown':
            self.mode = 'countdown'
        else:
            try:
                # メッセージが整数であれば開始値を更新
                new_value = int(msg.data)
                self.start_value = new_value
                self.value = new_value  # 新しい値をカウントの開始値として設定
                self.get_logger().info(f"Updated start value to: {new_value}")
            except ValueError:
                self.get_logger().warn(f"Invalid input: {msg.data}, expected integer for start value.")

    def generate_data(self):
        """データ生成部分: countup または countdown"""
        msg = Int16()
        if self.mode == 'countdown':
            msg.data = self.value
            self.value -= 1  # 1秒ごとに減少
            self.get_logger().info(f"Generated (Countdown): {msg.data}")
            if self.value < 0:  # 0未満に達したら停止
                self.get_logger().info("Countdown finished.")
                self.timer.cancel()
        else:
            msg.data = self.value
            self.value += 1  # 1秒ごとに増加
            self.get_logger().info(f"Generated (Countup): {msg.data}")

        # 生成されたデータをそのまま processed_data トピックに配信
        self.processed_pub.publish(msg)

def main():
    rclpy.init()
    node = CounterProcessorNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

