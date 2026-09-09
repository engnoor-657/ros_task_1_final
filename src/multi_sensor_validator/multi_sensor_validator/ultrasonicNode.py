import rclpy
from rcply.node import Node
from std_msgs.msg import Int32
from ultrasonic_sensor import Ultrasonic
import time
from Iultra import Iultra
class UltrasonicNode(Node):
    def __init__(self):
        super().__init__('ultrasonic_node')
        self.ultrasonic = Ultrasonic()
        self.publisher_ = self.create_publisher(Int32, ' /ultrasonic_range', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Ultrasonic Node has been started.')

    def timer_callback(self):
        reading = self.ultrasonic.get_reading()
        msg = Int32()
        msg.data = reading
        self.publisher_.publish(msg)
        self.get_logger().info(f'Ultrasonic: {reading} cm')

    def get_reading(self) -> int:
        import random
        min_range = 10
        max_range = 200  
        reading = random.randint(min_range, max_range)
        return reading

def main(args=None):
    rclpy.init(args=args)
    ultrasonic_node = UltrasonicNode()
    try:
        rclpy.spin(ultrasonic_node)
    except KeyboardInterrupt:
        pass
    finally:
        ultrasonic_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()