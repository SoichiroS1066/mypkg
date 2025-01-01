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
echo "カウントアップテスト開始"
ros2 run mypkg counter_processor countup &
processor_pid=$!  # プロセスIDを取得
sleep 2  # counter_processorが起動するまで待機

echo "5" | ros2 run mypkg input_value_publisher
sleep 2  # 結果を待機
kill $processor_pid  # counter_processorを停止
echo "Test Passed for Countup" > /tmp/test_result.log

# 正しい整数値（5）でカウントダウン
echo "カウントダウンテスト開始"
ros2 run mypkg counter_processor countdown &
processor_pid=$!
sleep 2

echo "5" | ros2 run mypkg input_value_publisher
sleep 2
kill $processor_pid
echo "Test Passed for Countdown" >> /tmp/test_result.log

# 誤った入力（文字列）でカウントアップ
echo "不正な入力テスト開始"
ros2 run mypkg counter_processor countup &
processor_pid=$!
sleep 2

echo "abc" | ros2 run mypkg input_value_publisher
sleep 2
kill $processor_pid
if grep -q "Invalid mode specified" /tmp/test_result.log; then
    echo "Test Passed for Invalid Input" >> /tmp/test_result.log
else
    echo "Test Failed for Invalid Input" >> /tmp/test_result.log
fi

# テスト結果の確認
echo "テスト結果を確認中..."
if grep -q "Test Passed" /tmp/test_result.log; then
    echo "OK"
else
    echo "Test Failed"
fi

# 必ずrclpyをシャットダウン
echo "Shutting down ROS 2..."
ros2 daemon stop

