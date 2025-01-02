#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String
import sys

class counter_processor_node(Node):
    def __init__(self):
        super().__init__('counter_processor_node')

        self.subscription_int = self.create_subscription(
            Int16,
            'input_data',
            self.listener_callback_int,
            10
        )

        self.subscription_str = self.create_subscription(
            String,
            'input_string',
            self.listener_callback_str,
            10
        )

        self.start_value = None
        self.mode = None

        if len(sys.argv) > 1:
            self.mode = sys.argv[1].lower()

        if self.mode not in ["countup", "countdown"]:
            self.get_logger().error("Invalid mode specified. Use 'countup' or 'countdown'.")
            rclpy.shutdown()

        self.timer = self.create_timer(1.0, self.timer_callback)

    def listener_callback_int(self, msg):
        self.start_value = msg.data
        self.get_logger().info(f"Received initial value: {self.start_value}")

    def listener_callback_str(self, msg):
        self.get_logger().error(f"Invalid input received: {msg.data}. Expected an integer.")

    def timer_callback(self):
        if self.start_value is not None:
            if self.mode == "countup":
                self.start_value += 1
                self.get_logger().info(f"Countup output: {self.start_value}")
            elif self.mode == "countdown":
                self.start_value -= 1
                self.get_logger().info(f"Countdown output: {self.start_value}")

                if self.start_value == 0:
                    self.get_logger().info("Countdown complete. Stopping...")
                    self.timer.cancel()
        else:
            self.get_logger().info("Waiting for initial value...")

def main():
    rclpy.init()
    node = CounterProcessorNode()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Keyboard interrupt received, shutting down...")
    finally:
        node.get_logger().info("Shutting down node.")
        rclpy.shutdown()

if __name__ == '__main__':
    main()

