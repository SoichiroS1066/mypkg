#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="mypkg",
            executable="talker",
            name="talker_node"
        ),
        Node(
            package="mypkg",
            executable="listener",
            name="listener_node"
        )
    ])

