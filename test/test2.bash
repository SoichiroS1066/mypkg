#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# Define the default directory
dir=~
[ "$1" != "" ] && dir="$1"

# Navigate to the ROS 2 workspace
cd $dir/ros2_ws

# Build the workspace using colcon
colcon build

# Source the ROS 2 environment
source $dir/.bashrc

# Run the ROS 2 launch file with countup mode and start value set to 0
timeout 10 ros2 launch mypkg talk_listen2.launch.py mode:=countup start_value:=0 > /tmp/mypkg.log

# Check the log file for the expected output (Listen: 10)
cat /tmp/mypkg.log | grep 'Listen: 10'

