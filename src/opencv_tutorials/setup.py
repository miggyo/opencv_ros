from setuptools import find_packages, setup
import glob
import os

package_name = 'opencv_tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch',glob.glob(os.path.join('launch', '*.launch.py'))),
        ('share/' + package_name + '/param',glob.glob(os.path.join('param', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='min',
    maintainer_email='6648kmk@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'img_publisher = opencv_tutorials.img_publisher:main',
            'canny_publisher = opencv_tutorials.canny_publisher:main',
            'optical_flow = opencv_tutorials.optical_flow:main',
            'img_control = opencv_tutorials.img_control:main',
            'cartoon = opencv_tutorials.cartoon:main',
        ],
    },
)
