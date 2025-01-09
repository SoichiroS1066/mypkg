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

# サブスクライバが天気情報を受け取ったか確認
timeout 10 grep '東京スカイツリーの天気情報' /tmp/mypkg.log


