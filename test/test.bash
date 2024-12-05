#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd /root/ros2_ws  # 修正: 正しいパスに変更
colcon build
source /root/.bashrc  # 修正: 正しいパスに変更
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

cat /tmp/mypkg.log | grep 'Listen: 10'

