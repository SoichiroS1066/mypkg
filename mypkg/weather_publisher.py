import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class WeatherPublisher(Node):
    def __init__(self):
        super().__init__('weather_publisher')
        self.publisher_ = self.create_publisher(String, '/weather_info', 10)

        # 10秒ごとに天気情報を取得
        self.timer = self.create_timer(10.0, self.timer_callback)

    def timer_callback(self):
        # 天気情報を取得
        weather_info = self.get_weather_info()
        msg = String()
        msg.data = weather_info

        # メッセージをパブリッシュ（標準出力には表示しない）
        self.publisher_.publish(msg)

    def get_weather_info(self):
        api_key = "948ca567d0432133fbe253ca65c9d5fc"
        city = "Tokyo"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                # 必要な情報を取り出してフォーマット
                weather_description = data['weather'][0]['description']
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                icon = data['weather'][0]['icon']
                
                # 新たに追加された情報を含めたメッセージを作成
                weather_info = (
                    f"{city}: {weather_description}, {temp}, "
                    f"Humidity: {humidity}, Wind Speed: {wind_speed}, "
                    f"Weather Icon: {icon}"
                )
                return weather_info
            else:
                return "Error: Unable to fetch weather data"
        except Exception as e:
            return f"Error: {str(e)}"

def main(args=None):
    rclpy.init(args=args)
    node = WeatherPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

