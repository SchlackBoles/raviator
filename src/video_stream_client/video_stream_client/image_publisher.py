#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ImagePublisher(Node):
    def __init__(self):
        super().__init__('image_publisher')
        self.publisher_ = self.create_publisher(Image, 'camera/image', 10)
        self.timer_period = 10  # seconds
        self.timer = self.create_timer(self.timer_period, self.timer_callback)
        self.bridge = CvBridge()
        self.cap = cv2.VideoCapture('tcp://192.168.8.3:8000')
        self.get_logger().info('Image publisher node started...')

    def timer_callback(self):
        if not self.cap.isOpened():
            self.get_logger().error('Failed to open video stream')
            return

        ret, frame = self.cap.read()
        if not ret:
            self.get_logger().error('Failed to read frame from video stream')
            return

        image_message = self.bridge.cv2_to_imgmsg(frame, encoding="bgr8")
        self.publisher_.publish(image_message)
        self.get_logger().info('Published an image')

def main(args=None):
    rclpy.init(args=args)
    node = ImagePublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()


