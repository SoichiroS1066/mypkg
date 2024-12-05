import rclpy  # ROS 2のクライアントのためのライブラリ
from rclpy.node import Node  # ノードを実装するためのNodeクラス
from std_msgs.msg import Int16  # 通信の型（16ビットの符号付き整数）

class Listener(Node):  # Nodeというクラスの機能を受け継いだクラスになる
    def __init__(self):
        super().__init__("listener")  # Nodeのオブジェクトとしての初期化
        self.sub = self.create_subscription(Int16, "countup", self.cb, 10)
        # ↑ サブスクリプションを作成。トピック "countup" を購読。
        #    コールバック関数 `cb` を指定。
        self.sub  # サブスクリプションを保持（ガベージコレクション防止）

    def cb(self, msg):  # メッセージを受け取ったときに呼ばれるコールバック
        self.get_logger().info(f"Listen: {msg.data}")  # 受信したデータをログに出力


def main():
    rclpy.init()
    node = Listener()  # Listenerのオブジェクトを作成
    rclpy.spin(node)  # ↑あとは__init__が呼ばれてすべてが動き出す

