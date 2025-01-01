#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# コンテナ内で作業ディレクトリを指定
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
# ROS 2のセットアップ
source /opt/ros/foxy/setup.bash

# パッケージのビルド
colcon build
source install/setup.bash

# サブスクライバをバックグラウンドで起動
ros2 run mypkg counter_processor_sub1 countdown > /tmp/counter_output.log &

# 少し待つ
sleep 1

# パブリッシャを実行し、カウントダウン用の初期値を入力
echo "10" | ros2 run mypkg input_value_publisher

# サブスクライバのログを確認してカウントダウンが正しく行われているかチェック
grep "Countdown output: 10" /tmp/counter_output.log
if [ $? -eq 0 ]; then
  echo "Countdown test: OK"
else
  echo "Countdown test: Failed"
fi

# サブスクライバをバックグラウンドで再起動し、カウントアップテストを開始
ros2 run mypkg counter_processor_sub1 countup > /tmp/counter_output.log &

# 少し待つ
sleep 1

# パブリッシャを実行し、カウントアップ用の初期値を入力
echo "0" | ros2 run mypkg input_value_publisher

# サブスクライバのログを確認してカウントアップが正しく行われているかチェック
grep "Countup output: 1" /tmp/counter_output.log
if [ $? -eq 0 ]; then
  echo "Countup test: OK"
else
  echo "Countup test: Failed"
fi

