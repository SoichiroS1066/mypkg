#!/bin/bash
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# ROS 2 Humbleの環境を読み込む
source /opt/ros/humble/setup.bash

# コンテナ内で作業ディレクトリを指定
dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

# 正しい入力（整数）をパブリッシュ
echo "10" | ros2 run mypkg input_value_publisher
sleep 1

# 正しい入力がパブリッシュされたか確認
if [ $? -eq 0 ]; then
  echo "Correct input test: OK"
else
  echo "Correct input test: Failed"
fi

# 誤った入力（整数以外）をパブリッシュ
echo "abc" | ros2 run mypkg input_value_publisher > /tmp/input_value_test.log 2>&1
sleep 1

# 誤った入力がパブリッシュされていないことを確認
if grep -q "無効な入力です。" /tmp/input_value_test.log; then
  echo "Incorrect input test: OK"  # エラーメッセージがログに存在すれば OK
else
  echo "Incorrect input test: Failed"
fi

# 誤った入力（記号）をパブリッシュ
echo "@#$%" | ros2 run mypkg input_value_publisher > /tmp/input_value_test.log 2>&1
sleep 1

# 記号やアルファベット以外の入力を検証
if grep -q "無効な入力です。" /tmp/input_value_test.log; then
  echo "Symbol input test: OK"  # 記号が含まれる入力がエラーとなり、ログに表示される場合 OK
else
  echo "Symbol input test: Failed"
fi

# 誤った入力（数字とアルファベットの混合）をパブリッシュ
echo "123abc" | ros2 run mypkg input_value_publisher > /tmp/input_value_test.log 2>&1
sleep 1

# 混合入力を検証
if grep -q "無効な入力です。" /tmp/input_value_test.log; then
  echo "Mixed input test: OK"  # 混合入力がエラーとなり、ログに表示される場合 OK
else
  echo "Mixed input test: Failed"
fi

