import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from infrared_sensor import Infrared
import time
from Iinfrared import Iinfrared
from infrared_sensor import Infrared
class InfraredNode(Node):
    def __init__(self):
        super().__init__('infrared_node')
        self.infrared = Infrared()
        self.publisher_ = self.create_publisher(Int32, '/infrared_range', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Infrared Node has been started.')

    def timer_callback(self):
        reading = self.infrared.get_reading()
        msg = Int32()
        msg.data = reading
        self.publisher_.publish(msg)
        self.get_logger().info(f'Infrared: {reading} cm')


def main(args=None):
    rclpy.init(args=args)
    infrared_node = InfraredNode()
    try:
        rclpy.spin(infrared_node)
    except KeyboardInterrupt:
        pass
    finally:
        infrared_node.destroy_node()
        rclpy.shutdown()
    

if __name__ == '__main__':
    main()