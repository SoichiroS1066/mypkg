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

