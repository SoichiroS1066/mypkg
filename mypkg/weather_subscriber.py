import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import subprocess

class WeatherSubscriber(Node):
    def __init__(self):
        super().__init__('weather_subscriber')
        self.subscription = self.create_subscription(
            String,
            '/weather_info',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

        # アイコンコードと絵文字の対応マッピング
        self.icon_mapping = {
            '01d': '☀️',   # Clear sky (day)
            '01n': '🌑',   # Clear sky (night)
            '02d': '🌤️',   # Few clouds (day)
            '02n': '🌥️',   # Few clouds (night)
            '03d': '🌥️',   # Scattered clouds (day)
            '03n': '🌥️',   # Scattered clouds (night)
            '04d': '☁️',   # Broken clouds (day)
            '04n': '☁️',   # Broken clouds (night)
            '09d': '🌧️',   # Shower rain (day)
            '09n': '🌧️',   # Shower rain (night)
            '10d': '🌦️',   # Rain (day)
            '10n': '🌧️',   # Rain (night)
            '11d': '🌩️',   # Thunderstorm (day)
            '11n': '🌩️',   # Thunderstorm (night)
            '13d': '❄️',   # Snow (day)
            '13n': '❄️',   # Snow (night)
            '50d': '🌫️',   # Mist (day)
            '50n': '🌫️'    # Mist (night)
        }

        # 天気説明の英語から日本語への変換マッピング
        self.weather_description_mapping = {
            'clear sky': '快晴',
            'few clouds': '少し雲',
            'scattered clouds': '散発的な雲',
            'broken clouds': '曇り',
            'shower rain': 'シャワー雨',
            'rain': '雨',
            'thunderstorm': '雷雨',
            'snow': '雪',
            'mist': '霧'
        }

    def listener_callback(self, msg):
        # 受け取った天気情報を表示
        weather_info = msg.data
        weather_parts = weather_info.split(", ")
        
        # 文字列から情報を取り出して日本語に変換
        city = weather_parts[0].split(":")[0]
        weather_description = weather_parts[0].split(":")[1]
        temp = weather_parts[1].split("°C")[0]
        humidity = weather_parts[2].split(":")[1].strip() + "%"
        wind_speed = weather_parts[3].split(":")[1].strip() + " m/s"
        
        # 天気説明を日本語に変換
        weather_description_jp = self.weather_description_mapping.get(weather_description.strip(), weather_description.strip())

        # curl コマンドで wttr.in からアスキーアートを取得
        icon_code = self.get_weather_icon(city)
        icon_emoji = self.get_icon_emoji(icon_code)

        # 日本語で情報を表示（天気説明とアイコンを横並びに）
        self.get_logger().info(f"{city}の天気情報: 天気: {weather_description_jp} {icon_emoji}, 気温: {temp}°C, 湿度: {humidity}, 風速: {wind_speed}")

    def get_weather_icon(self, city):
        try:
            # wttr.in に接続して天気アスキーアートを取得
            result = subprocess.run(
                ['curl', f'wttr.in/{city}?format=%C'], 
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # 結果を取得して整形
            return result.stdout.strip()
        except Exception as e:
            return f"天気アイコンの取得に失敗: {str(e)}"

    def get_icon_emoji(self, icon_code):
        # アイコンコードを絵文字に変換
        return self.icon_mapping.get(icon_code, '❓')  # デフォルトは不明なアイコン

def main(args=None):
    rclpy.init(args=args)
    node = WeatherSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

