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
echo "15" | ros2 run mypkg input_value_publisher &
# パブリッシュ処理の終了を待つ
wait $!
sleep 1  # 少し待機してから次の処理に進む

# 正しい入力がパブリッシュされているか確認
if [ $? -eq 0 ]; then
  echo "Correct input test: OK"
else
  echo "Correct input test: Failed"
fi

# 誤った入力（整数以外）をパブリッシュ
echo "abc" | ros2 run mypkg input_value_publisher &
# パブリッシュ処理の終了を待つ
wait $!
sleep 1  # 少し待機してから次の処理に進む

# 誤った入力が処理されていないか確認
if [ $? -eq 0 ]; then
  echo "Incorrect input test: Failed"
else
  echo "Incorrect input test: Failed"  # 誤った入力を処理していない場合
fi

