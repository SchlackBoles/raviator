#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from std_msgs.msg import String  # Assuming simple string commands for control
from cv_bridge import CvBridge

from ultralytics import YOLO  # Make sure to have YOLOv8 correctly installed

class ExcavatorController(Node):
    def __init__(self):
        super().__init__('excavator_controller')
        self.subscription = self.create_subscription(
            Image,
            'camera/image',
            self.image_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'excavator/control', 10)
        self.bridge = CvBridge()
        self.model = YOLO('yolov8n.pt')  # Load your YOLO model
        self.get_logger().info('Excavator controller node has started.')

    def image_callback(self, msg):
        cv_image = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        results = self.model(cv_image)  # Run YOLO inference
        control_command = self.process_results(results)
        self.publisher_.publish(control_command)
        self.get_logger().info('Published control command')

    def process_results(self, results, cv_image):
    # Process the inference results
        for result in results.xyxy[0]:  # Loop through detections
            if result[5] == 'fire hydrant':  # Use your object's class index here
                # Save the image with annotations for validation
                save_path = '/home/chen/Desktop/dev_ws/data'  # Absolute path to the data directory
                timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
                annotated_image = results.render()[0]  # Render detections on image
                cv2.imwrite(f"{save_path}/{timestamp}.jpg", annotated_image)
                # If the object is detected, return "move"
                return String(data="move")

        # If the object is not detected, return "stop"
        return String(data="stop")


def main(args=None):
    rclpy.init(args=args)
    controller_node = ExcavatorController()
    try:
        rclpy.spin(controller_node)
    except KeyboardInterrupt:
        pass
    finally:
        controller_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
