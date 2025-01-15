# mypkg
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/skytree_weather_test.yml/badge.svg)
<img src="https://img.shields.io/badge/ROS%202-00A1A7.svg?logo=ros&logoColor=white&style=for-the-badge" alt="ROS 2">
<img src="https://img.shields.io/badge/-Python-yellow.svg?logo=python&style=for-the-badge">

こちらは, 千葉工業大学先進工学部未来ロボティクス学科のロボットシステム学の講義で使用しているROS 2パッケージです.

# リポジトリの使用方法

ターミナルで以下のコマンドを実行します.
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/SoichiroS1066/mypkg.git
$ cd ~/ros2_ws/
$ colcon build
```

# skytree_weather_publisher

## 機能
- 東京スカイツリーの天気情報（天気, 気温, 湿度, 風速, 見晴らし評価）をパブリッシュする

## ノードとトピック

### ノード

### weather_publisher

- 役割: 天気情報を取得し, 定期的に情報を`weather_info`トピックへパブリッシュするノード
- 機能:
    - OpenWeatherMap API を使用して, 東京スカイツリー（緯度35.710139、経度139.810833）の天気情報を取得
    - 1秒ごとに天気情報をパブリッシュ

### トピック

### weather_info (std_msgs/msg/String)

- 役割: `weather_publisher`ノードが天気情報をパブリッシュするトピック
- 内容:
    - 天気（16段階）
    - 気温（°C）
    - 湿度（%）
    - 風速（m/s）
    - 見晴らしの評価（天気に基づく）

## 前提条件

### *python requests モジュール*
- APIから天気情報を取得する際に使用します.
- `pip install requests`または`sudo apt install python3-requests`でインストールしてください.
```
$ pip install requests
```
```
$ sudo apt install python3-requests
```

### *python-dotenv モジュール*
- `.env`ファイルからAPIキーを読み込む際に使用します.
- `pip install python-dotenv`または`sudo apt install python3-dotenv`でインストールしてください.
```
$ pip install python-dotenv
```
```
$ sudo apt install python3-dotenv
```

### *OpenWeatherMap APIキー* （公式サイトで取得）
- `skytree_weather_publisher.py`がOpenWeatherMap API へアクセスする際に使用します.

### *.env ファイルの作成*
- 取得したAPIキーを管理する際に使用します.
- 以下の手順で`skytree_weather_publisher.py`と同じディレクトリに`.env`を作成してください.
```
$ vi .env
```
記述する内容
```
OPENWEATHER_API_KEY=ここに取得したAPIキーを入力     # 例：OPENWEATHER_API_KEY=12345678910
```

## 実行方法
以下のコマンドで実行可能です.
```
$ ros2 run mypkg skytree_weather_publisher
``` 

トピックで公開されているメッセージの確認方法（別端末）
```
$ ros2 topic echo /weather_info
```
```
data: '東京スカイツリー: 天気: 晴れ, 気温: 10.36°C, 湿度: 26%, 風速: 2.06 m/s, 見晴らし: 良好'
---
data: '東京スカイツリー: 天気: 晴れ, 気温: 10.36°C, 湿度: 26%, 風速: 2.06 m/s, 見晴らし: 良好'
---
data: '東京スカイツリー: 天気: 晴れ, 気温: 10.36°C, 湿度: 26%, 風速: 2.06 m/s, 見晴らし: 良好'
---
```

# 参考リンク
- GeoHack - 東京スカイツリー
    - https://geohack.toolforge.org/geohack.php?language=ja&pagename=%E6%9D%B1%E4%BA%AC%E3%82%B9%E3%82%AB%E3%82%A4%E3%83%84%E3%83%AA%E3%83%BC&params=35_42_36.5_N_139_48_39_E_region:JP-13_type:landmark
- 天気予報をアプリに組み込もう！おすすめAPIランキング10
    - https://qiita.com/takuya77088/items/b3663f5d54d5f9501880
- OpenWeather の API を使ってみた
    - https://qiita.com/noritakaIzumi/items/34f16e383f59f9c5d8cf
- OpenWeatherMap
    - https://openweathermap.org/
- .envファイルで環境変数を設定する方法
    - https://qiita.com/k-suna/items/ef782da10e66f642ddbc

# 注意事項
以下はテスト用です
- listener.py
- talk_listen.launch.py

# テスト環境
- *Ubuntu 22.04 LTS*
- *ROS 2 Humble*

# LICENSE
- このソフトウェアパッケージは, 3条項BSDライセンスの下, 再頒布および使用が許可されます.
- このパッケージ内の一部は, 下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを, 本人の許可を得て自身の著作としたものです.
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
- © 2025 Soichiro Suzuki
