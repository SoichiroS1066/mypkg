# mypkg
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test_counter_processor.yml/badge.svg)
<img src="https://img.shields.io/badge/ROS%202-00A1A7.svg?logo=ros&logoColor=white&style=for-the-badge" alt="ROS 2">
<img src="https://img.shields.io/badge/-Python-yellow.svg?logo=python&style=for-the-badge">


こちらは、千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているROS2のパッケージのリポジトリです。

# リポジトリの使用方法

ターミナルで以下のコマンドを実行する
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/SoichiroS1066/mypkg.git
$ cd ~/ros2_ws/
$ colcon build

# input_value_publisher

## 機能
- ROS 2のノード`counter_publisher_node`を作成し, ユーザーから入力された整数, 文字及び記号を`input_data`というトピックにpublishする
- publish後, プログラムを終了する

## 実行方法
先述したinput_value_publisher.pyを実行する
```
$ cd ~/ros2_ws/
$ ros2 run mypkg input_value_publisher
入力してください:
```   
※ 入力は数字, 文字, 記号に対応


## ノードとトピック
*ノード*   
`counter_publisher_node`   
- メソッド：受け取ったdataを`int 型`または`str 型`のメッセージとして, 2つの異なる`input_data`トピックへ送信する
    
*トピック*   
`input_data`(int 型)
- トピックタイプ:`std_msgs/msg/Int16`
- ユーザーが入力した整数をこのトピックを通じて発行し, subscriberへ送る
- 数値計算などの数値に基づいた処理を行う他のノードと連携する際に役立つ   
例：ロボットのセンサー値, 制御信号
   
`input_data`(str 型)
- トピックタイプ：`std_msgs/msg/String`
- ユーザーが入力したデータが整数でない場合, このトピックを通じて発行しsubscriberへ送る
- ユーザーが入力したメッセージやコマンドを他のノードに伝える際に役立つ   
例：ロボットに対する指示, 状態メッセージ


# テスト環境
- *Ubuntu 22.04 LTS*
- *Python 3.10*
- *ROS2 humble*

# LICENSE

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージ内の `talker.py`, `listener.py`, `talk_listen.launch.py` は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
- © 2025 Soichiro Suzuki
