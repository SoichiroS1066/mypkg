#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WeatherSubscriber(Node):
    def __init__(self):
        super().__init__('weather_subscriber')
        self.subscription = self.create_subscription(
            String,
            '/weather_info',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f"東京スカイツリーの天気情報: {msg.data}")

def main(args=None):
    rclpy.init(args=args)
    node = WeatherSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

