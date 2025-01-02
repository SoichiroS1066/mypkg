#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy  # ROS 2のクライアントのためのライブラリ
from rclpy.node import Node  # ノードを実装するためのNodeクラス（クラスは第10回で）
from std_msgs.msg import Int16  # 通信の型（16ビットの符号付き整数）

### ヘッダの下にTalkerというクラスを作成 ###
class Talker(Node):  # Nodeというクラスの機能を受け継いだクラスになる
    def __init__(self):  # オブジェクトができたときに呼ばれる
        super().__init__("takler")  # Nodeのオブジェクトとしての初期化
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)
        self.n = 0
        # ↑ selfはオブジェクト自身のこと
        # ↑ オブジェクトにひとつパブリッシャと変数をもたせる。

    def cb(self):  # コールバックのメソッド
        msg = Int16()
        msg.data = self.n  # 属性には必ずselfをつける
        self.pub.publish(msg)
        self.n += 1


def main():
    rclpy.init()
    node = Talker()  # Talkerのオブジェクトを作成
    rclpy.spin(node)  # ↑あとは__init__が呼ばれてすべてが動き出す

