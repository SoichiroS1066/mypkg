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
if [ $? -ne 0 ]; then
  echo "Build failed"
  exit 1
fi

# Source the ROS 2 environment
source $dir/.bashrc

# Test for countdown mode
echo "Testing countdown mode with start_value 10"
timeout 10 ros2 launch mypkg talk_listen2.launch.py mode:=countdown start_value:=10 > /tmp/mypkg.log
if [ $? -ne 0 ]; then
  echo "Countdown test failed"
  exit 1
fi
echo "Countdown Mode Output:"
cat /tmp/mypkg.log | grep 'Listen: 10'
if [ $? -ne 0 ]; then
  echo "Countdown test output check failed"
  exit 1
fi

# Test for countup mode
echo "Testing countup mode with start_value 0"
timeout 10 ros2 launch mypkg talk_listen2.launch.py mode:=countup start_value:=0 > /tmp/mypkg.log
if [ $? -ne 0 ]; then
  echo "Countup test failed"
  exit 1
fi
echo "Countup Mode Output:"
cat /tmp/mypkg.log | grep 'Listen: 0'
if [ $? -ne 0 ]; then
  echo "Countup test output check failed"
  exit 1
fi

# If all tests pass, print OK
echo "OK"

