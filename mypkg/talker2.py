import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Timer(Node):
    def __init__(self):
        super().__init__('timer')
        self.pub = self.create_publisher(Int16, 'countup', 10)
        
        # 引数を取得
        mode = self.declare_parameter('mode', 'countup').value
        start_value = self.declare_parameter('start_value', 10).value

        self.mode = mode
        self.value = start_value

        # タイマーを1秒ごとに設定
        self.timer = self.create_timer(1.0, self.cb)

    def cb(self):
        msg = Int16()

        if self.mode == 'countdown':
            # カウントダウン
            msg.data = self.value
            self.value -= 1  # 1秒ごとに減少
            self.get_logger().info(f"Countdown: {msg.data}")
            
            if self.value < 0:  # 0未満に達したら停止
                self.get_logger().info("Countdown finished.")
                self.timer.cancel()  # タイマーを停止
        else:
            # カウントアップ
            msg.data = self.value
            self.value += 1  # 1秒ごとに増加
            self.get_logger().info(f"Countup: {msg.data}")

        self.pub.publish(msg)

def main():
    rclpy.init()

    node = Timer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
