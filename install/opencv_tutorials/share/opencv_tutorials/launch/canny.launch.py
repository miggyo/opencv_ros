import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description(): 
    prarm_dir = LaunchConfiguration(
        'param_dir',
        default=os.path.join(
        get_package_share_directory('opencv_tutorials'),
        'param',
        'filter.yaml')
        )
    
    return LaunchDescription(
        [
            DeclareLaunchArgument(
            'param_dir',
            default_value=prarm_dir
            ),

            Node(
                package='opencv_tutorials',
                executable='canny_publisher',
                name='canny_publisher',
                parameters=[prarm_dir],
                output='screen'),
    ])