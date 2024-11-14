# mypkg
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test.yml/badge.svg)

こちらは、千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているROS2のパッケージのリポジトリです。

# リポジトリの概要

talker.py, listener.py

# リポジトリの使用方法

ターミナルで以下のコマンドを実行する
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/IkuoShige/mypkg.git
$ git clone https://github.com/IkuoShige/hit_and_blow_msgs.git
$ cd ~/ros2_ws/
$ colcon build
```

# talker と listener

## 機能

talker.py で１ずつ加算したnをpublishし、listener.py でnをsubscribeする

# LICENSE

* このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
* © 2024 Soichiro Suzuki
