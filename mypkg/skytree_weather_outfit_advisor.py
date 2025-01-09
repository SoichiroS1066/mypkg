import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class WeatherSubscriber(Node):
    def __init__(self):
        super().__init__('weather_subscriber')
        self.subscription = self.create_subscription(
            String,
            '/weather_info',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        # メッセージを解析
        weather_info = msg.data
        self.get_logger().info('Received weather info: "%s"' % weather_info)
        
        # 服装提案を行う
        outfit_suggestion = self.generate_outfit_suggestion(weather_info)
        self.get_logger().info('服装提案: "%s"' % outfit_suggestion)

    def generate_outfit_suggestion(self, weather_info):
        # メッセージ解析
        temp = self.extract_temperature(weather_info)
        weather_description = self.extract_weather_description(weather_info)
        wind_speed = self.extract_wind_speed(weather_info)
        humidity = self.extract_humidity(weather_info)
        
        # 服装提案
        outfit = []
        
        # 気温に基づく提案
        if temp < 0:
            outfit.append("厚手のコート")
        elif 0 <= temp < 10:
            outfit.append("薄手のコート、ジャケット")
        elif 10 <= temp < 25:
            outfit.append("セーター、長袖シャツ")
        else:
            outfit.append("半袖シャツ、軽装")

        # 天気に基づく提案
        if "rain" in weather_description or "thunderstorm" in weather_description:
            outfit.append("レインコートや傘")

        # 風速に基づく提案
        if wind_speed > 10:
            outfit.append("風を通さないジャケット")

        # 湿度に基づく提案
        if humidity > 80:
            outfit.append("通気性の良い服装")
        
        return "、".join(outfit) if outfit else "普段通りの服装"

    def extract_temperature(self, weather_info):
        # 気温を抽出（例: "気温: 5.0°C" から 5.0 を取得）
        temp_str = self.extract_info(weather_info, "気温:")
        try:
            temp = float(temp_str.replace("°C", ""))
            return temp
        except ValueError:
            return 0.0

    def extract_weather_description(self, weather_info):
        # 天気の説明を抽出（例: "天気: 快晴" から "快晴" を取得）
        return self.extract_info(weather_info, "天気:")

    def extract_wind_speed(self, weather_info):
        # 風速を抽出（例: "風速: 5 m/s" から 5 を取得）
        wind_speed_str = self.extract_info(weather_info, "風速:")
        try:
            wind_speed = float(wind_speed_str.split()[0])
            return wind_speed
        except ValueError:
            return 0.0

    def extract_humidity(self, weather_info):
        # 湿度を抽出（例: "湿度: 60%" から 60 を取得）
        humidity_str = self.extract_info(weather_info, "湿度:")
        try:
            humidity = int(humidity_str.replace("%", ""))
            return humidity
        except ValueError:
            return 0

    def extract_info(self, weather_info, key):
        # 指定したキーに対応する情報を抽出
        start = weather_info.find(key)
        if start != -1:
            start += len(key)
            end = weather_info.find(",", start)
            if end == -1:
                end = len(weather_info)
            return weather_info[start:end].strip()
        return ""

def main(args=None):
    rclpy.init(args=args)
    node = WeatherSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

