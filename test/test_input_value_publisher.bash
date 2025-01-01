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
ros2 run mypkg declare_number_sub > /tmp/input_value_output.log &

# 少し待つ
sleep 1

# 正しい入力（整数）をパブリッシュ
echo "15" | ros2 run mypkg input_value_publisher
sleep 1

# サブスクライバのログを確認して正しい入力が処理されているかチェック
grep "Received data: 15" /tmp/input_value_output.log
if [ $? -eq 0 ]; then
  echo "Correct input test: OK"
else
  echo "Correct input test: Failed"
fi

# 正しくない入力（整数以外）をパブリッシュ
echo "abc" | ros2 run mypkg input_value_publisher
sleep 1

# サブスクライバのログを確認して正しくない入力が処理されていないかチェック
grep "Received data: abc" /tmp/input_value_output.log
if [ $? -eq 0 ]; then
  echo "Incorrect input test: Failed"
else
  echo "Incorrect input test: OK"
fi

