# mypkg
![test](https://github.com/ryuichiueda/robosys2022/actions/workflows/test.yml/badge.svg)

## 機能
* 数字をカウントしてトピック/countupを通じて送信する
  * メッセージの型は16ビット符号つき整数　(std)

## 起動の手順
(端末1) ~/ros2_ws/src/mypkg/mypkgにtalker.pyを書く
<br>
(端末1) talker.pyをビルド(`colcon build`)する
<br>
(端末1)$`ros2 run mypkg listener` と入力し、もう一つの端末を開く
<br>
これだけでは何も起きないので別でUbuntuを開き
<br>
(端末2)$`ros2 run mypkg talker` と入力する

## 使用例
(端末1)$`ros2 run mypkg listener`
<br>
(端末2)$`ros2 run mypkg talker`
<br>
(端末1)3.6.9 (default, Jun 29 2022, 11:45:57)
<br>
[GCC 8.4.0]
<br>
[INFO] [listener]: Listen: 0
<br>
[INFO] [listener]: Listen: 1
<br>
[INFO] [listener]: Listen: 2
<br>
[INFO] [listener]: Listen: 3
<br>
[INFO] [listener]: Listen: 4
<br>
[INFO] [listener]: Listen: 5
<br>
[INFO] [listener]: Listen: 6
<br>
[INFO] [listener]: Listen: 7
<br>
[INFO] [listener]: Listen: 8
<br>
[INFO] [listener]: Listen: 9
<br>
[INFO] [listener]: Listen: 10
<br>
[INFO] [listener]: Listen: 11
<br>
		:
<br>
		:

## 必要なソフトウェア
* Python 
  * テスト済み: 3.7 ～ 3.10

## テスト環境
* GitHub Actions

* Python 3.7 ～ 3.10


## ライセンス

* このパッケージのコードは，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです。
  * [ryuichiueda/my_slides robosys_2022](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2022)

* このソフトウェアパッケージは、3条項BSDライセンスの下、再頒布および使用が許可されます。

* © 2022 Soichiro Suzuki
