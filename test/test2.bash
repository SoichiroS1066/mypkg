#!/bin/bash
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

timeout 30 ros2 launch mypkg talk_listen2.launch.py &

sleep 10

ros2 topic echo /weather_info | grep -m 1 '東京スカイツリーの天気情報' &

pid=$!

sleep 20
if ps -p $pid > /dev/null; then
    kill $pid
    echo "OK"
else
    echo "Error: 天気情報の受信に失敗しました"
    exit 1
fi

