# mypkg
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test.yml/badge.svg)
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
$ ros2 launch mypkg talk_listen2.launch.py mode:=countdown start_value:=10
```   
   
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

## ノードとトピック
*ノード*   
`/talker_node`   
- このノードは、指定されたモードに応じてカウントアップまたはカウントダウンを行い、その結果をパブリッシュします。   
- 引数で指定されたmodeに基づき、値は増加または減少します。   
- タイマーを使用して、1秒ごとに値を更新し、指定されたトピック（/countupまたは/countdown）にデータをパブリッシュします。   
   
`/listener_node`   
- このノードは、/countupまたは/countdownトピックからデータを受信し、その内容をログに出力します。   
- リスニングするトピックに応じて、受信したデータを「Listen: {data}」という形式で表示します。   
   
*トピック*   
`/countup` (タイプ: std_msgs/msg/Int16)   
- カウントアップ用のトピックです。このトピックでは、数値が増加するデータがパブリッシュされます。

`/countdown` (タイプ: std_msgs/msg/Int16)   
- カウントダウン用のトピックです。このトピックでは、数値が減少するデータがパブリッシュされます。  

*パラメータ*   
`mode`  
- モードを指定するパラメータです（デフォルトはcountup）

`start_value`   
- カウントダウンの開始値（デフォルトは10）

# 🌍テスト環境
* Ubuntu 24.04.1 LTS
* Python 3.7 ~ 3.10

# 📄LICENSE

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
* © 2024 Soichiro Suzuki
