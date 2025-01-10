#!/bin/bash
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# talk_listen.launch.py の起動
ros2 launch mypkg talk_listen.launch.py &

# パブリッシャが起動するのを待機
sleep 10

# トピックから天気情報を受信しているか確認
timeout 30 ros2 topic echo /weather_info | grep -q '東京スカイツリーの天気情報'

# 結果を確認
if [ $? -eq 0 ]; then
    echo "OK"
else
    echo "Error: 天気情報の受信に失敗しました"
    exit 1
fi

