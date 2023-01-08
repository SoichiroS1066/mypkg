# mypkg
![test](https://github.com/ryuichiueda/robosys2022/actions/workflows/test.yml/badge.svg)

## はじめに
このソフトウェアは千葉工業大学未来先進工学部未来ロボティクス学科2年後期「ロボットシステム学」の講義内で使用したものです。

## リポジトリを使用する前の準備
ターミナルで以下を実行
`$ cd ~/ros2_ws/src`
<br>
`$ git clone https://github.com/SoichiroS1066/mypkg.git`
<br>
`$ cd ~/ros2_ws`
<br>
`$ colcon build`

## 「talker」 & 「listener」
## 機能
* talker.pyで1ずつ加算されるnをlistener.pyで表示する。

## 使用例
`$ cd ~/ros2_ws`
<br>
`$ ros2 launch mypkg talk_listen.launch.py`
<br>
`[INFO] [launch]: All log files can be found below /home/suzuki/.ros/log/2023-01-08-20-39-09-637178-DESKTOP-VKJQDU9-2787`
<br>
`[INFO] [launch]: Default logging verbosity is set to INFO`
<br>
`[INFO] [talker-1]: process started with pid [2797]`
<br>
`[INFO] [listener-2]: process started with pid [2798]`
<br>
`[listener-2] [INFO] [listener]: Listen: 0`
<br>
`[listener-2] [INFO] [listener]: Listen: 1`
<br>
`[listener-2] [INFO] [listener]: Listen: 3`
<br>
・・・

## 必要なソフトウェア
* Python 
  * テスト済み: 3.7 ～ 3.10

## テスト環境
* GitHub Actions
* Ubuntu 18.04
* Python 3.7 ～ 3.10


## ライセンス

* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

* © 2022 Soichiro Suzuki
