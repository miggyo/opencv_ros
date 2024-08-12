import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

class CannyPublisher(Node):
    def __init__(self):
        super().__init__('canny_publisher')
        self.subscription = self.create_subscription(
            Image,
            '/camera',
            self.listener_callback,
            10)
        
        self.publisher = self.create_publisher(
            Image,
            '/canny_edges',
            10)
        
        self.cv_bridge = CvBridge()

    def listener_callback(self, msg):
        frame = self.cv_bridge.imgmsg_to_cv2(msg, "bgr8")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 100, 200)
        edges_msg = self.cv_bridge.cv2_to_imgmsg(edges, "mono8")
        

        self.publisher.publish(edges_msg)

def main(args=None):
    rclpy.init(args=args)
    node = CannyPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
