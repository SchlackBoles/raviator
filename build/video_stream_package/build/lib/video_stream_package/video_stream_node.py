#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class VideoStreamNode(Node):
    def __init__(self):
        super().__init__('video_stream_node')
        self.publisher_ = self.create_publisher(Image, 'video_stream', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.cap = cv2.VideoCapture("http://192.168.8.3:8000/stream.mjpg")
        self.bridge = CvBridge()

    def timer_callback(self):
        ret, frame = self.cap.read()
        if ret:
            msg = self.bridge.cv2_to_imgmsg(frame, encoding='bgr8')
            self.publisher_.publish(msg)
        else:
            self.get_logger().error('Failed to capture frame')

def main(args=None):
    rclpy.init(args=args)
    video_stream_node = VideoStreamNode()
    rclpy.spin(video_stream_node)
    video_stream_node.cap.release()
    video_stream_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
