from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='mypkg',
            executable='nikkei_publisher',
            name='nikkei_publisher',
            output='log'),
        Node(
            package='mypkg',
            executable='nikkei_subscriber',
            name='nikkei_subscriber',
            output='log'),
    ])

