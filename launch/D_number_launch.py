from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',  # パッケージ名
            executable='declare_number_pub',  # 実行ファイル名
            name='declare_number_pub',
            output='screen'
        ),
        Node(
            package='mypkg',  # パッケージ名
            executable='declare_number_sub',  # 実行ファイル名
            name='declare_number_sub',
            output='screen'
        ),
    ])

