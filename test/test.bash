#!/bin/bash
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~ 
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# skytree_weather_publisher.py の起動
ros2 run mypkg skytree_weather_publisher &

# listener.py の起動
ros2 run mypkg listener &

# サブスクライバのログを確認する方法を変更
timeout 10 ros2 topic echo /weather_info | grep '東京スカイツリーの天気情報'

