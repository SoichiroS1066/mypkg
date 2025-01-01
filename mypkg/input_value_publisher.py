#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16, String

class CounterPublisherNode(Node):
    def __init__(self):
        super().__init__('counter_publisher_node')
        self.int_publisher = self.create_publisher(Int16, 'input_data', 10)
        self.str_publisher = self.create_publisher(String, 'input_string', 10)

    def send_input(self, data, data_type):
        if data_type == "int":
            msg = Int16()
            msg.data = int(data)
            self.int_publisher.publish(msg)
        elif data_type == "str":
            msg = String()
            msg.data = data
            self.str_publisher.publish(msg)

def main():
    rclpy.init()
    publisher_node = CounterPublisherNode()

    user_input = input("入力してください: ")

    if user_input.strip().isdigit():
        publisher_node.send_input(user_input, "int")
    else:
        publisher_node.send_input(user_input, "str")

    rclpy.shutdown()

if __name__ == '__main__':
    main()

