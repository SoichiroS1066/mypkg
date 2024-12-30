# mypkg
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test2.yml/badge.svg)
<img src="https://img.shields.io/badge/ROS%202-00A1A7.svg?logo=ros&logoColor=white&style=for-the-badge" alt="ROS 2">
<img src="https://img.shields.io/badge/-Python-yellow.svg?logo=python&style=for-the-badge">


こちらは、千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているROS2のパッケージのリポジトリです。

# リポジトリの概要
*talker.py, listener.py*
- クラスやメソッドを用いて、publisherとsubscriberを実装

*talk_listen.launch.py*
- talker.py と listener.py の launchファイル

*talker2.py, listener2.py*
- カウントアップとカウントダウン機能を実装

*talk_listen2.launch.py*
- talker2.py と listener2.py の launchファイル

# 📥リポジトリの使用方法

ターミナルで以下のコマンドを実行する
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/SoichiroS1066/mypkg.git
$ cd ~/ros2_ws/
$ colcon build
```

# talker と listener

## ⚙️ 機能

talker.py で１ずつ加算したnをpublishし、listener.py でnをsubscribeする

## 📝使い方
先述したlaunchファイルを実行する
```
$ cd ~/ros2_ws/
$ ros2 launch mypkg talk_listen.launch.py
```  
出力結果
```
[INFO] [launch]: All log files can be found below /home/suzuki/.ros/log/2024-12-12-14-34-57-897134-DESKTOP-VKJQDU9-106
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker-1]: process started with pid [111]
[INFO] [listener-2]: process started with pid [112]
[listener-2] [INFO] [1733981699.004403600] [listener]: Listen: 0
[listener-2] [INFO] [1733981699.490451900] [listener]: Listen: 1
[listener-2] [INFO] [1733981699.990581900] [listener]: Listen: 2
[listener-2] [INFO] [1733981700.489951100] [listener]: Listen: 3
...
...
```  

# talker2 とlistener2

## ⚙️ 機能
- talker2.py で１ずつ加算したnをpublishし、listener2.py でnをsubscribeする(カウントアップ)   
- talker2.py で１ずつ減算したnをpublishし、listener2.py でnをsubscribeする(カウントダウン)   

## 📝使い方
先述したlaunchファイルを実行する
```
$ cd ~/ros2_ws/
   
# カウントダウンの場合   
$ ros2 launch mypkg talk_listen2.launch.py mode:=countdown start_value:=10   
   
# カウントアップの場合   
$ ros2 launch mypkg talk_listen2.launch.py mode:=countup start_value:=0   
```   
※1. `mode:=` の後ろに`countdown`又は`countup`を入力しモードを設定する   
※2. `start_value:=`　の後ろの数字でカウントの開始タイミングを設定する   
   
カウントダウンの出力(例)
```
$ ros2 launch mypkg talk_listen2.launch.py mode:=countdown start_value:=10
[INFO] [launch]: All log files can be found below /home/suzuki/.ros/log/2024-12-31-02-53-06-543696-DESKTOP-VKJQDU9-892
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker2-1]: process started with pid [895]
[INFO] [listener2-2]: process started with pid [896]
[talker2-1] [INFO] [1735581187.877669900] [talker_node]: Countdown: 10
[listener2-2] [INFO] [1735581187.887264700] [listener_node]: Listen: 10
[talker2-1] [INFO] [1735581188.868084000] [talker_node]: Countdown: 9
[listener2-2] [INFO] [1735581188.871407800] [listener_node]: Listen: 9
[talker2-1] [INFO] [1735581189.868231300] [talker_node]: Countdown: 8
[listener2-2] [INFO] [1735581189.870746700] [listener_node]: Listen: 8
[talker2-1] [INFO] [1735581190.868418100] [talker_node]: Countdown: 7
[listener2-2] [INFO] [1735581190.871693900] [listener_node]: Listen: 7
...
...
...
[talker2-1] [INFO] [1735581194.868096300] [talker_node]: Countdown: 3
[listener2-2] [INFO] [1735581194.870532100] [listener_node]: Listen: 3
[talker2-1] [INFO] [1735581195.868101600] [talker_node]: Countdown: 2
[listener2-2] [INFO] [1735581195.871517800] [listener_node]: Listen: 2
[talker2-1] [INFO] [1735581196.868257300] [talker_node]: Countdown: 1
[listener2-2] [INFO] [1735581196.871847200] [listener_node]: Listen: 1
[talker2-1] [INFO] [1735581197.868351200] [talker_node]: Countdown: 0
[talker2-1] [INFO] [1735581197.869741800] [talker_node]: Countdown finished.
[listener2-2] [INFO] [1735581197.872502100] [listener_node]: Listen: 0
```
   
カウントアップの出力(例)   
```
$ ros2 launch mypkg talk_listen2.launch.py mode:=countup start_value:=0
[INFO] [launch]: All log files can be found below /home/suzuki/.ros/log/2024-12-31-05-05-03-245404-DESKTOP-VKJQDU9-1453
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [talker2-1]: process started with pid [1456]
[INFO] [listener2-2]: process started with pid [1457]
[talker2-1] [INFO] [1735589104.726828800] [talker_node]: Countup: 0
[listener2-2] [INFO] [1735589104.735680200] [listener_node]: Listen: 0
[talker2-1] [INFO] [1735589105.715204500] [talker_node]: Countup: 1
[listener2-2] [INFO] [1735589105.718284600] [listener_node]: Listen: 1
[talker2-1] [INFO] [1735589106.715367500] [talker_node]: Countup: 2
[listener2-2] [INFO] [1735589106.718504600] [listener_node]: Listen: 2
[talker2-1] [INFO] [1735589107.715251400] [talker_node]: Countup: 3
[listener2-2] [INFO] [1735589107.718213400] [listener_node]: Listen: 3
...
...
```   


## ノードとトピック
*ノード*   
`/talker_node`   
- 指定されたモードに応じてカウントアップまたはカウントダウンを行い、その結果をパブリッシュする   
- 引数で指定されたmodeに基づき、値は増加または減少します。   
- タイマーを使用して、1秒ごとに値を更新し、指定されたトピック（`/countup`または`/countdown`）にデータをパブリッシュする   
   
`/listener_node`   
- `/countup`または`/countdown`トピックからデータをサブスクライブし、その内容をログに出力する   
- リスニングするトピックに応じて、受信したデータを「Listen: {data}」という形式で出力する   
   
*トピック*   
`/countup` (タイプ: std_msgs/msg/Int16)   
- カウントアップ用のトピックで、数値が増加するデータがパブリッシュされる

`/countdown` (タイプ: std_msgs/msg/Int16)   
- カウントダウン用のトピックで、数値が減少するデータがパブリッシュされる   

*パラメータ*   
`mode`  
- モード（`countup`または`countdown`）を指定するパラメータ（デフォルトは`countup`）

`start_value`   
- カウントダウンの開始値（デフォルトは10）

# 🌍テスト環境
- Ubuntu 22.04 LTS
- Python 3.12.3
- ROS2 humble

# 📄LICENSE

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
- © 2024 Soichiro Suzuki
