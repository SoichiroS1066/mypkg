from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'mypkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py'))  # launch/*.pyを追加
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Soichiro Suzuki',
    maintainer_email='s21c1066jy@s.chibakoudai.jp',
    description='a package for practice',
    license='BSD-3-Clause',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = mypkg.talker:main',  # 既存のエントリポイント
            'listener = mypkg.listener:main',  # 既存のエントリポイント
            'declare_number_pub = mypkg.declare_number_pub:main',  # 新しいエントリポイント
            'declare_number_sub = mypkg.declare_number_sub:main',  # 新しいエントリポイント
        ],
    },
)

