from setuptools import find_packages, setup

package_name = 'video_stream_client'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='chen',
    maintainer_email='andreas.stavis@gmail.com',
    description='TCP streaming of video for ROS2 Humble and Pi5 since no one works',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
    'console_scripts': [
        'video_stream_client = video_stream_client.video_stream_client:main',
        'video_to_topic = video_stream_client.video_to_topic:main',
        'image_to_topic = video_stream_client.image_publisher:main',
        'excavator_controller = video_stream_client.excavator_controller:main',  # Add this line
    ],
    }


)
