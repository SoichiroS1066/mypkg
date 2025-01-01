#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# ディレクトリの設定（引数がある場合はそのディレクトリ）
dir=~
[ "$1" != "" ] && dir="$1"

# ROS2環境のセットアップ
cd $dir/ros2_ws
source /opt/ros/foxy/setup.bash
source $dir/ros2_ws/install/setup.bash

# テスト: 正しい入力（数字のみ）
echo "Testing with valid input (0)"
output=$(ros2 run mypkg input_value_publisher 0)
if [[ "$output" == *"[INFO] [counter_publisher_node]"* ]]; then
    echo "Valid input test passed: OK"
else
    echo "Valid input test failed"
    exit 1
fi

# テスト: 正しくない入力（数字以外）
echo "Testing with invalid input (non-numeric)"
output=$(ros2 run mypkg input_value_publisher "invalid")
if [[ "$output" == *"[INFO] [counter_publisher_node]"* ]]; then
    echo "Invalid input test failed"
    exit 1
else
    echo "Invalid input test passed: OK"
fi

# テストが正常に終了した場合、OK を表示
echo "All tests completed successfully: OK"

