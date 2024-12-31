from setuptools import setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
         ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),  # launchディレクトリを追加
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Soichiro Suzuki',
    maintainer_email='s21c1066jy@s.chibakoudai.jp',
    description='Countdown timer package',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',      # オリジナルのtalker
            'listener = mypkg.listener:main',  # オリジナルのlistener
            'talker2 = mypkg.talker2:main',    # 新しいtalker2
            'listener2 = mypkg.listener2:main', # 新しいlistener2
            'counter_processor = mypkg.counter_processor:main',  # 新しい統合ノード
            'counter_processor_sub1 = mypkg.counter_processor_sub1:main'  # 新しいサブスクライバノード
        ],
    },
)

