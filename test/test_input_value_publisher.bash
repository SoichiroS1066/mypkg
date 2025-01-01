#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# ROS 2 Humbleの環境を読み込む
source /opt/ros/humble/setup.bash

# コンテナ内で作業ディレクトリを指定
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

# サブスクライバをバックグラウンドで起動
ros2 run mypkg declare_number_sub > /tmp/input_value_output.log &

# 少し待つ
sleep 1

# 正しい入力（整数）をパブリッシュ
echo "15" | ros2 run mypkg input_value_publisher
sleep 1

# 正しい入力がパブリッシュされているか確認
grep "Received data: 15" /tmp/input_value_output.log
if [ $? -eq 0 ]; then
  echo "Correct input test: OK"
else
  echo "Correct input test: Failed"
fi

# ここでサブスクライバを停止して、次のテストに進む
kill %1
sleep 1

# 誤った入力（整数以外）をパブリッシュ
echo "abc" | ros2 run mypkg input_value_publisher
sleep 1

# 誤った入力がパブリッシュされていないことを確認
grep "Received data: abc" /tmp/input_value_output.log
if [ $? -eq 0 ]; then
  echo "Incorrect input test: Failed"
else
  echo "Incorrect input test: OK"
fi

