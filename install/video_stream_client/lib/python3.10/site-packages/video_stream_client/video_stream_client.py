#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
import subprocess

class VideoStreamClient(Node):
    def __init__(self):
        super().__init__('video_stream_client')
        self.get_logger().info('Starting video stream client...')
        self.stream_command = ['ffplay', 'tcp://192.168.8.3:8000', '-fflags', 'nobuffer', '-flags', 'low_delay', '-framedrop']
        self.start_stream()

    def start_stream(self):
        try:
            subprocess.run(self.stream_command)
        except Exception as e:
            self.get_logger().error(f'Failed to start video stream: {str(e)}')

def main(args=None):
    rclpy.init(args=args)
    node = VideoStreamClient()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
