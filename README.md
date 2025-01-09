# mypkg
[![License: BSD 3-Clause](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
![test](https://github.com/SoichiroS1066/mypkg/actions/workflows/test_counter_processor.yml/badge.svg)
<img src="https://img.shields.io/badge/ROS%202-00A1A7.svg?logo=ros&logoColor=white&style=for-the-badge" alt="ROS 2">
<img src="https://img.shields.io/badge/-Python-yellow.svg?logo=python&style=for-the-badge">


こちらは, 千葉工業大学先進工学部未来ロボティクス学科2年後期のロボットシステム学の講義で扱っているROS2のパッケージのリポジトリです。

# リポジトリの使用方法

ターミナルで以下のコマンドを実行する
```
$ cd ~/ros2_ws/src/
$ git clone https://github.com/SoichiroS1066/mypkg.git
$ cd ~/ros2_ws/
$ colcon build
```

# input_value_publisher

## 機能
- 東京スカイツリーの天気情報（天気, 気温, 湿度, 風速, 見晴らし評価）を含んだトピックをパブリッシュする

## 前提条件
*ROS 2*:
- このパッケージはROS 2環境で実行されるため, ROS 2がインストールされていないと実行できません。   
*Python requestsパッケージ*（`pip install requests`または`sudo apt-get install python3-requests`でインストール）:
- プログラム内でrequestsライブラリを使用し外部のOpenWeatherMap APIにアクセスしています。   
- requestsがインストールされていない場合, APIから天気情報を取得できません。   
*OpenWeatherMap APIキー*（公式サイトで取得）:
- OpenWeatherMap APIにアクセスするには, 個々のユーザーがAPIキーを取得する必要があります。
- APIキーをプログラム内で使用して天気情報を取得するため, 使用する場合は自分のAPIキーを設定してください。
```
def get_weather_info(self):
        api_key = "948ca567d0432133fbe253ca65c9d5fc"        # この行の""間に取得したAPIキーを上書き
```

## 実行方法
weather_publisher.pyを実行する
```
$ ros2 run mypkg weather_publisher.py
``` 

トピックで公開されているメッセージの確認方法
```
$ ros2 topic echo /weather_info
```
```
data: '東京スカイツリー: 天気: 快晴, 気温: 5.84°C, 湿度: 46%, 風速: 4.12 m/s, 見晴らし: 良好'
---
data: '東京スカイツリー: 天気: 快晴, 気温: 5.84°C, 湿度: 46%, 風速: 4.12 m/s, 見晴らし: 良好'
---
...
```

## ノード
- ノード名: `weather_publisher`
- 役割: 天気情報を取得し, 定期的にその情報をROS 2トピックにパブリッシュするノード
- 主な機能:
    - 天気情報の取得: OpenWeatherMap APIを使用して、東京スカイツリーの位置（緯度35.710063、経度139.8107）における天気情報を取得
    - 天気情報のフォーマット: 天気, 気温, 湿度, 風速, 見晴らし評価
    - パブリッシュ: 10秒ごとに天気情報をROS 2のトピックに送信

## トピック
トピック名: `/weather_info`
- メッセージ型: `std_msgs.msg.String`
- 役割: 天気情報を含む文字列メッセージを受け取るトピック
- 内容:
    - 天気（日本語で）
    - 気温（°C）
    - 湿度（%）
    - 風速（m/s）
    - 見晴らしの評価（天気に基づく）
## 注意点
- OpenWeatherMap APIは1分毎のアクセス回数に制限があります。

# テスト環境
- *Ubuntu 22.04 LTS*
- *Python 3.10*
- *ROS2 humble*

# LICENSE

- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- このパッケージ内の一部は，下記のスライド（CC-BY-SA 4.0 by Ryuichi Ueda）のものを，本人の許可を得て自身の著作としたものです．
    - [ryuichiueda/my_slides robosys_2024](https://github.com/ryuichiueda/my_slides/tree/master/robosys_2024)
- © 2025 Soichiro Suzuki
