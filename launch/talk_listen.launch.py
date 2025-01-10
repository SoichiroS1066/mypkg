#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="mypkg",  # パッケージ名
            executable="skytree_weather_publisher",  # パブリッシャの実行ファイル名
            name="weather_publisher_node",  # パブリッシャのノード名
            output="screen"  # 標準出力を画面に表示
        ),
        Node(
            package="mypkg",  # パッケージ名
            executable="listener",  # サブスクライバの実行ファイル名
            name="listener_node",  # サブスクライバのノード名
            output="screen"  # 標準出力を画面に表示
        )
    ])

