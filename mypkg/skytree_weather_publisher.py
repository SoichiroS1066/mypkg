#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2025 Soichiro Suzuki
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
import requests
from std_msgs.msg import String

class WeatherPublisher(Node):
    def __init__(self):
        super().__init__('weather_publisher')
        self.publisher_ = self.create_publisher(String, '/weather_info', 10)
        self.timer = self.create_timer(10.0, self.timer_callback)

    def timer_callback(self):
        weather_info = self.get_weather_info()
        msg = String()
        msg.data = weather_info
        self.publisher_.publish(msg)

    def get_weather_info(self):
        api_key = "948ca567d0432133fbe253ca65c9d5fc"
        lat = 35.710063  # 東京スカイツリーの緯度
        lon = 139.8107   # 東京スカイツリーの経度
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                weather_description = data['weather'][0]['description']
                temp = data['main']['temp']
                humidity = data['main']['humidity']
                wind_speed = data['wind']['speed']
                icon = data['weather'][0]['icon']

                # 天気の説明を日本語に変換
                weather_description_jp = self.translate_weather_description(weather_description)

                # 見晴らしの評価を追加
                visibility_rating = self.evaluate_visibility(icon)

                weather_info = (
                    f"東京スカイツリー: 天気: {weather_description_jp}, "
                    f"気温: {temp}°C, 湿度: {humidity}%, 風速: {wind_speed} m/s, "
                    f"見晴らし: {visibility_rating}"
                )
                return weather_info
            else:
                return "Error: Unable to fetch weather data"
        except Exception as e:
            return f"Error: {str(e)}"

    def translate_weather_description(self, description):
        # 英語の天気説明を日本語に翻訳
        weather_map = {
            "clear sky": "快晴",
            "few clouds": "晴れ",
            "scattered clouds": "雲が散らばっている",
            "broken clouds": "曇り",
            "shower rain": "にわか雨",
            "rain": "雨",
            "thunderstorm": "雷雨",
            "snow": "雪",
            "mist": "霧",
            "haze": "かすみ",
            "fog": "霧",
            "dust": "砂塵",
            "sand": "砂嵐",
            "ash": "灰",
            "squall": "突風",
            "tornado": "竜巻"
        }
        return weather_map.get(description, description)

    def evaluate_visibility(self, icon):
        # 天気に応じて見晴らしを評価
        visibility_map = {
            "01d": "非常に良好",  # 快晴（昼）
            "01n": "良好",       # 快晴（夜）
            "02d": "良好",       # 少し曇り（昼）
            "02n": "やや良好",   # 少し曇り（夜）
            "03d": "普通",       # 曇り（昼）
            "03n": "普通",       # 曇り（夜）
            "04d": "やや不良",   # 曇天（昼）
            "04n": "不良",       # 曇天（夜）
            "09d": "非常に不良", # 小雨（昼）
            "09n": "非常に不良", # 小雨（夜）
            "10d": "非常に不良", # 雨（昼）
            "10n": "非常に不良", # 雨（夜）
            "13d": "非常に不良", # 雪（昼）
            "13n": "非常に不良", # 雪（夜）
            "50d": "不明",       # 霧（昼）
            "50n": "不明",       # 霧（夜）
        }
        return visibility_map.get(icon, "不明")

def main(args=None):
    rclpy.init(args=args)
    node = WeatherPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

