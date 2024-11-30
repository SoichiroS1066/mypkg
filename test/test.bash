#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"   # 引数があったら、そちらをホームに変える。

source $dir/.bashrc
cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Listen: 10'
