#!/bin/bash
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc

# talk_listen.launch.py の起動（タイムアウトを設定）
timeout 30 ros2 launch mypkg talk_listen.launch.py &

# パブリッシャが起動するのを待機
sleep 10

# ros2 topic echo をバックグラウンドで実行
ros2 topic echo /weather_info | grep -m 1 '東京スカイツリーの天気情報' &

# echo のプロセス ID を取得
pid=$!

# タイムアウトを設定（20秒後にプロセスがまだ動いていれば終了）
sleep 20
if ps -p $pid > /dev/null; then
    # プロセスがまだ動いていれば終了
    kill $pid
    echo "OK"
else
    echo "Error: 天気情報の受信に失敗しました"
    exit 1
fi

