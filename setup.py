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
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Soichiro Suzuki',
    maintainer_email='s21c1066jy@s.chibakoudai.jp',
    description='Weather data publisher',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'skytree_weather_publisher = mypkg.skytree_weather_publisher:main',
            'skytree_weather_publisher2 = mypkg.skytree_weather_publisher2:main',
            'listener = mypkg.listener:main',
        ],
    },
)

