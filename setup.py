from setuptools import setup
import os
from glob import glob

package_name = 'mydogrobot_controll'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name, 'launch'),
         glob('launch/*.py')),  # launchファイルの指定

        (os.path.join('share', package_name, 'rviz'),
         glob('rviz/*')),  # rvizファイルの指定

        (os.path.join('share', package_name, 'urdf'),
         glob('./urdf/*')),  # urdfファイルの指定


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntupc',
    maintainer_email='iga_e39@yahoo.co.jp',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
