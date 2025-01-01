# mypkg
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test_input_value_publisher.yml/badge.svg)
<img src="https://img.shields.io/badge/ROS%202-00A1A7.svg?logo=ros&logoColor=white&style=for-the-badge" alt="ROS 2">
<img src="https://img.shields.io/badge/-Python-yellow.svg?logo=python&style=for-the-badge">


こちらは、千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているROS2のパッケージのリポジトリです。

# リポジトリの概要
*talker.py, listener.py*
- クラスやメソッドを用いて、publisherとsubscriberを実装

*talk_listen.launch.py*
- talker.py と listener.py の launchファイル

*input_value_publisher.py*
- ユーザから入力された整数をinput_dataというトピックにpublish

*counter_processor.py*
- テスト用スクリプト(publisherから受信した数字を開始値としてカウントダウンとカウントアップ)

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

# input_value_publisher

## ⚙️ 機能
- ROS 2のノード`counter_publisher_node`を作成し、ユーザーから入力された整数を`input_data`というトピックにpublishする
- publish後、プログラムを終了する
- 入力が整数でない場合はエラーメッセージを表示し、プログラムを終了する

## 📝使い方
先述したinput_value_publisher.pyを実行する
```
$ cd ~/ros2_ws/
$ ros2 run mypkg input_value_publisher
数字を入力してください:                 # 数字を入力しEnterを押すとpublishされる
```   

実行例
```
$ ros2 run mypkg input_value_publisher
数字を入力してください: 0
```

## 💬ノードとトピック
*ノード*   
`CounterPublisherNode`   
- Nodeクラスを継承し、`counter_publisher_node`という名前で初期化される
   - メソッド：引数で受け取ったdataを`Int16型`のメッセージにセットし、`/input_data`トピックに送信する
    
*トピック*   
`/input_data`(`Int16型`) 
- ユーザーが入力した整数をこのトピックを通じて発行し、subscriberへ送る


# 🌍テスト環境
- Ubuntu 22.04 LTS
- Python 3.10~12.3
- ROS2 humble

# 📄LICENSE

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
- © 2024 Soichiro Suzuki
