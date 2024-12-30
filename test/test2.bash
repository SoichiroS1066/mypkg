#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# Define the default directory
dir=~
[ "$1" != "" ] && dir="$1"

# Navigate to the ROS workspace
cd $dir/ros2_ws

# Build the workspace using colcon
colcon build

# Source the ROS 2 environment
source $dir/.bashrc

# Run the ROS 2 launch file with the specified parameters (countup mode and start value)
timeout 10 ros2 launch mypkg talk_listen2.launch.py mode:=countup start_value:=0 > /tmp/mypkg.log

# Check the log file for the expected output (Listen: 0, Listen: 1, etc.)
cat /tmp/mypkg.log | grep 'Listen: 0'
cat /tmp/mypkg.log | grep 'Listen: 1'
cat /tmp/mypkg.log | grep 'Listen: 2'
cat /tmp/mypkg.log | grep 'Listen: 3'
cat /tmp/mypkg.log | grep 'Listen: 4'
cat /tmp/mypkg.log | grep 'Listen: 5'
cat /tmp/mypkg.log | grep 'Listen: 6'
cat /tmp/mypkg.log | grep 'Listen: 7'
cat /tmp/mypkg.log | grep 'Listen: 8'
cat /tmp/mypkg.log | grep 'Listen: 9'
cat /tmp/mypkg.log | grep 'Listen: 10'

