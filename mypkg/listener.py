#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(Int16, "countup", self.cb, 10)

        self.sub

    def cb(self, msg):
        self.get_logger().info(f"Listen: {msg.data}")


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)

