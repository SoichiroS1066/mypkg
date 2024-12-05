#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

echo "Loading .bashrc from $dir"
source $dir/.bashrc
echo "Changing directory to $dir/ros2_ws"
cd $dir/ros2_ws
echo "Building workspace with colcon"
colcon build
echo "Sourcing .bashrc again"
source $dir/.bashrc
echo "Running ROS 2 launch"
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

echo "Checking logs for 'Listen: 10'"
cat /tmp/mypkg.log | grep 'Listen: 10'

