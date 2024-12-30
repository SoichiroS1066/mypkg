# mypkg
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test.yml/badge.svg)
<img src="https://img.shields.io/badge/ROS%202-00A1A7.svg?logo=ros&logoColor=white&style=for-the-badge" alt="ROS 2">
<img src="https://img.shields.io/badge/-Python-yellow.svg?logo=python&style=for-the-badge">


こちらは、千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているROS2のパッケージのリポジトリです。

# リポジトリの概要
talker.py, listener.py
* クラスやメソッドを用いて、publisherとsubscriberを実装

talk_listen.launch.py
* talker.py と listener.py の launchファイル

# リポジトリの使用方法

ターミナルで以下のコマンドを実行する
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/SoichiroS1066/mypkg.git
$ cd ~/ros2_ws/
$ colcon build
```

# talker と listener

## 機能

talker.py で１ずつ加算したnをpublishし、listener.py でnをsubscribeする

## 使用方法
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

## talker2 とlistener2
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test2.yml/badge.svg)


# テスト環境
* Ubuntu 24.04.1 LTS
* Python 3.7 ~ 3.10

# LICENSE

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
* © 2024 Soichiro Suzuki
