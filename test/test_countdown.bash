#!/bin/bash

# カウントダウンタイマーのテストスクリプト
source /opt/ros/humble/setup.bash
source ~/ros2_ws/install/setup.bash

# Launchファイルを起動
ros2 launch mypkg countdown_launch.py &
LAUNCH_PID=$!

# 少し待機してからトピックをチェック
sleep 5

# トピックの出力を取得して確認
topic_output=$(timeout 10 ros2 topic echo /countdown Int32)

if [[ "$topic_output" == *"data: 0"* ]]; then
    echo "テスト成功: カウントダウン動作確認完了。"
    kill $LAUNCH_PID
    exit 0
else
    echo "テスト失敗: カウントダウン動作確認失敗。"
    kill $LAUNCH_PID
    exit 1
fi

