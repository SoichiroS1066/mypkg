#!/bin/bash
# SPDX-FileCopyrightText: 2024 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

# 使用するディレクトリを設定
dir=~
[ "$1" != "" ] && dir="$1"   # 引数があったら、そちらをホームに変える。

# ディレクトリの権限確認
if [ ! -d "$dir/ros2_ws/src/mypkg" ]; then
    echo "Error: Directory $dir/ros2_ws/src/mypkg does not exist."
    exit 1
fi

# ディレクトリの権限が正しいか確認し、必要に応じて修正
if [ "$(stat -c "%U" $dir/ros2_ws/src/mypkg)" != "suzuki" ]; then
    echo "Changing ownership of $dir/ros2_ws/src/mypkg to user 'suzuki'..."
    sudo chown -R suzuki:suzuki $dir/ros2_ws/src/mypkg
fi

if [ ! -r "$dir/ros2_ws/src/mypkg" ] || [ ! -w "$dir/ros2_ws/src/mypkg" ]; then
    echo "Changing permissions to allow read/write access..."
    sudo chmod -R u+rwx $dir/ros2_ws/src/mypkg
fi

# 作業ディレクトリに移動
cd $dir/ros2_ws

# colconでビルド
colcon build

# .bashrcを再読み込み
source $dir/.bashrc

# ROS2ノードを起動し、ログを取得
timeout 10 ros2 launch mypkg talk_listen.launch.py > /tmp/mypkg.log

# ログファイルから特定の文字列を抽出
cat /tmp/mypkg.log | grep 'Listen: 10'

