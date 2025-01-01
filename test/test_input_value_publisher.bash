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
echo "abc" | ros2 run mypkg input_value_publisher
sleep 1

# 誤った入力がパブリッシュされていないことを確認
if [ $? -eq 1 ]; then  # 失敗コード 1 の場合
  echo "Incorrect input test: OK"  # 誤った入力の失敗を確認したので OK
else
  echo "Incorrect input test: Failed"
fi

