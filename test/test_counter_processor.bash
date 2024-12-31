#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# 作業ディレクトリを指定（引数があればそれを使用）
dir=~
[ "$1" != "" ] && dir="$1"

# ROS 2 ワークスペースに移動
cd $dir/ros2_ws

# パッケージのビルド
colcon build

# ROS 2 環境をソース
source $dir/ros2_ws/install/setup.bash

# ノードの実行
timeout 10 ros2 run mypkg counter_processor &

# 1秒後に 'input_data' トピックにメッセージを送信（countupモード）
ros2 topic pub /input_data std_msgs/String "data: 'countup'" &

# 1秒後に開始値を変更
sleep 1
ros2 topic pub /input_data std_msgs/String "data: '20'" &

# 2秒後に 'countdown' モードに切り替え
sleep 2
ros2 topic pub /input_data std_msgs/String "data: 'countdown'" &

# ノードがログを出力しているか確認
timeout 10 tail -f /tmp/mypkg.log | grep "Generated"

