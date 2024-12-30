#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# Define the default directory
dir=~
[ "$1" != "" ] && dir="$1"

# Check for custom Python executable via COLCON_PYTHON_EXECUTABLE environment variable
if [ -n "$COLCON_PYTHON_EXECUTABLE" ]; then
  if [ ! -f "$COLCON_PYTHON_EXECUTABLE" ]; then
    echo "error: COLCON_PYTHON_EXECUTABLE '$COLCON_PYTHON_EXECUTABLE' doesn't exist"
    exit 1
  fi
  _colcon_python_executable="$COLCON_PYTHON_EXECUTABLE"
else
  # Try the default Python executable known at configure time
  _colcon_python_executable="/usr/bin/python3"
  if [ ! -f "$_colcon_python_executable" ]; then
    # Fall back to python3 found via env
    if ! /usr/bin/env python3 --version > /dev/null 2>&1; then
      echo "error: unable to find python3 executable"
      exit 1
    fi
    _colcon_python_executable=$(which python3)
  fi
fi

# Navigate to the ROS 2 workspace
cd $dir/ros2_ws

# Build the workspace using colcon
colcon build

# Source the ROS 2 environment
source $dir/.bashrc

# Test 1: Run the ROS 2 launch file with countdown mode and start value set to 10
timeout 10 ros2 launch mypkg talk_listen2.launch.py mode:=countdown start_value:=10 > /tmp/mypkg_countdown.log

# Check the log file for the expected output (Listen: 10)
cat /tmp/mypkg_countdown.log | grep 'Listen: 10'
if [ $? -ne 0 ]; then
  echo "error: 'Listen: 10' not found in the countdown log output"
  exit 1
fi

# Test 2: Run the ROS 2 launch file with countup mode and start value set to 0
timeout 30 ros2 launch mypkg talk_listen2.launch.py mode:=countup start_value:=0 > /tmp/mypkg_countup.log

# Output the entire log to verify what is actually being logged
cat /tmp/mypkg_countup.log

# Check the log file for the expected output (Listen: 9)
cat /tmp/mypkg_countup.log | grep 'Listen: 9'

# Check if the expected output is found
if [ $? -ne 0 ]; then
  echo "error: 'Listen: 9' not found in the countup log output"
  exit 1
else
  echo "OK"
fi

