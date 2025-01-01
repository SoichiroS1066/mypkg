#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class CounterProcessorSub1Node(Node):
    def __init__(self):
        super().__init__('counter_processor_sub1_node')

        # サブスクライバを作成（input_data トピック）
        self.subscription = self.create_subscription(
            Int16,
            'input_data',
            self.listener_callback,
            10
        )

        # 初期値を保持する変数
        self.start_value = None
        self.mode = None  # モードを設定する変数

        # コマンドライン引数でモードを設定
        import sys
        if len(sys.argv) > 1:
            self.mode = sys.argv[1].lower()  # 引数でモードを設定 (countup または countdown)

        if self.mode not in ["countup", "countdown"]:
            self.get_logger().error("Invalid mode specified. Use 'countup' or 'countdown'.")
            rclpy.shutdown()

        # タイマーを作成（1秒ごとにカウントアップまたはカウントダウンを実行）
        self.timer = self.create_timer(1.0, self.timer_callback)

    def listener_callback(self, msg):
        """受け取った初期値を設定"""
        self.start_value = msg.data
        self.get_logger().info(f"Received initial value: {self.start_value}")

    def timer_callback(self):
        """カウントアップまたはカウントダウンを実行"""
        if self.start_value is not None:
            if self.mode == "countup":
                self.start_value += 1
                self.get_logger().info(f"Countup output: {self.start_value}")
            elif self.mode == "countdown":
                self.start_value -= 1
                self.get_logger().info(f"Countdown output: {self.start_value}")

                # カウントダウンが0になった場合、終了メッセージを表示
                if self.start_value == 0:
                    self.get_logger().info("Countdown complete. Stopping...")
                    self.timer.cancel()  # タイマーを停止
        else:
            self.get_logger().info("Waiting for initial value...")

def main():
    rclpy.init()
    node = CounterProcessorSub1Node()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()

