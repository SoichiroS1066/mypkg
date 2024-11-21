import rclpy
from rclpy.node import Node
from person_msgs.msg import Person

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Person, "person", 10)
n = 0

def cb():
    global n
    msg = Person()
    msg.name = "鈴木聡一郎"
    msg.age = n
    pub.publish(msg)
    rclpy.logging.get_logger("talker").info(f"Published: {msg.name}, {msg.age}")  # 修正
    n += 1

def main():
    node.create_timer(0.5, cb)
    rclpy.logging.get_logger("talker").info("Talker node started...")  # 修正
    rclpy.spin(node)

if __name__ == '__main__':
    main()

