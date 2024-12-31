#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'mode', default_value='countup', description='countup or countdown'
        ),
        DeclareLaunchArgument(
            'start_value', default_value='10', description='Starting value for countdown'
        ),
        Node(
            package="mypkg",
            executable="counter_processor",  # counter_processor ノードを実行
            name="counter_processor_node",
            output="screen",
            parameters=[{
                'mode': LaunchConfiguration('mode'),
                'start_value': LaunchConfiguration('start_value')
            }]
        )
    ])
