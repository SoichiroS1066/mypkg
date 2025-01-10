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
        self.publisher_ = self.create_publisher(String, '/weather_info', 1)
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        weather_info = self.get_fujisan_weather()
        msg = String()
        msg.data = weather_info
        self.publisher_.publish(msg)

    def get_fujisan_weather(self):
        api_key = "5af6a18eb5ee42eeb5a73906251101"  # WeatherAPIキー
        lat = 35.3606  # 富士山の緯度
        lon = 138.7274  # 富士山の経度
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={lat},{lon}"

        try:
            response = requests.get(url)
            data = response.json()
            if response.status_code == 200:
                weather_description = data['current']['condition']['text']
                temp = data['current']['temp_c']
                humidity = data['current']['humidity']
                wind_speed = data['current']['wind_kph']
                icon = data['current']['condition']['icon']

                weather_description_jp = self.translate_weather_description(weather_description)    # 天気の説明を日本語に変換
                visibility_rating = self.evaluate_visibility(icon)  # 見晴らしの評価

                weather_info = (
                    f"富士山山頂: 天気: {weather_description_jp}, "
                    f"気温: {temp}°C, 湿度: {humidity}%, 風速: {wind_speed} km/h, "
                    f"見晴らし: {visibility_rating}\n"
                )
                
                # 各合目の標高設定（単位: メートル）
                altitudes = {
                    "1合目": 1000,
                    "2合目": 1200,
                    "3合目": 1500,
                    "4合目": 1800,
                    "5合目吉田口": 2300,
                    "5合目富士宮口": 2400,
                    "5合目須走口": 2000,
                    "5合目御殿場口": 1450,  # 新5合目
                    "6合目": 2500,
                    "7合目": 2800,
                    "8合目": 3100,
                    "9合目": 3400,
                    "10合目": 3700
                }

                # 各合目の気温を補正して追加
                for location, altitude in altitudes.items():
                    adjusted_temp = self.adjust_temperature_for_altitude(temp, altitude)  # 気温補正
                    weather_info += f"  {location}: 補正後気温: {adjusted_temp}°C\n"

                return weather_info
            else:
                return "Error: Unable to fetch weather data"
        except Exception as e:
            return f"Error: {str(e)}"

    def translate_weather_description(self, description):   # 英語の天気説明を日本語に翻訳
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

    def evaluate_visibility(self, icon):    # 天気に応じて見晴らしを評価
        visibility_map = {
            "clear_sky": "非常に良好",  # 快晴
            "few_clouds": "良好",      # 少し曇り
            "scattered_clouds": "やや良好",  # 雲が散らばっている
            "broken_clouds": "曇り",   # 曇り
            "shower_rain": "非常に不良",  # 小雨
            "rain": "非常に不良",      # 雨
            "thunderstorm": "雷雨",    # 雷雨
            "snow": "非常に不良",      # 雪
            "mist": "不明",            # 霧
        }
        return visibility_map.get(icon, "不明")

    def adjust_temperature_for_altitude(self, temp, altitude):
        # 標高1000mごとに気温は6.5°C下がるが、1合目など低い標高では補正を緩やかに
        temperature_drop_per_km = 6.5  # 1kmあたりの気温低下（摂氏）
        
        # 標高1000m未満では気温低下を緩やかに
        if altitude < 2000:
            temperature_drop_per_km = 5.0  # 低い標高では緩やかに（例: 5°C/km）
        
        temp_drop = (altitude / 1000) * temperature_drop_per_km
        return round(temp - temp_drop, 2)

def main(args=None):
    rclpy.init(args=args)
    node = WeatherPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

