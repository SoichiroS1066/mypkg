#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

source /opt/ros/humble/setup.bash

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source install/setup.bash

# 正しい整数値（5）でカウントアップ
echo "5" | ros2 run mypkg input_value_publisher
sleep 2  # 2秒待ってカウントアップの結果を確認
echo "5" | ros2 run mypkg counter_processor countdown
sleep 3  # 少し長めに待つ（データの受信が遅れる場合があるため）

# カウントアップ結果の確認
if grep -q "Countdown output" /tmp/test_result.log; then
    echo "Test Passed for Countup" > /tmp/test_result.log
else
    echo "Test Failed for Countup" > /tmp/test_result.log
fi

# 正しい整数値（5）でカウントダウン
echo "5" | ros2 run mypkg input_value_publisher
sleep 2  # 2秒待ってカウントダウンの結果を確認
echo "5" | ros2 run mypkg counter_processor countdown
sleep 3  # 少し長めに待つ（データの受信が遅れる場合があるため）

# カウントダウン結果の確認
if grep -q "Countdown output" /tmp/test_result.log; then
    echo "Test Passed for Countdown" >> /tmp/test_result.log
else
    echo "Test Failed for Countdown" >> /tmp/test_result.log
fi

# 誤った入力（文字列）でカウントアップ
echo "abc" | ros2 run mypkg input_value_publisher
sleep 2  # 2秒待って文字列の入力に対するエラーハンドリングを確認
echo "abc" | ros2 run mypkg counter_processor countup
sleep 2  # 2秒待って文字列に対するカウントアップの結果を確認

# 無効な入力の確認
if grep -q "Invalid mode specified" /tmp/test_result.log; then
    echo "Test Passed for Invalid Input" >> /tmp/test_result.log
else
    echo "Test Failed for Invalid Input" >> /tmp/test_result.log
fi

# テスト結果の確認
if grep -q "Test Passed" /tmp/test_result.log; then
    echo "OK"
else
    echo "Test Failed"
fi

