import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32,String
import time

class ValidatorNode(Node):
    def __init__(self):
        super().__init__('validator_node')
        self.ultrasonic_range = None
        self.infrared_range = None
        self.ultrasonic_subscriber = self.create_subscription(Int32, '/ultrasonic_range', self.ultrasonic_callback, 10)
        self.infrared_subscriber = self.create_subscription(Int32, '/infrared_range', self.infrared_callback, 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Validator Node has been started.')
        self.validation_publisher = self.create_publisher(String, '/validation_result', 10)
    def ultrasonic_callback(self, msg):
        self.ultrasonic_range = msg.data

    def infrared_callback(self, msg):
        self.infrared_range = msg.data

    def timer_callback(self):
        if self.ultrasonic_range is not None and self.infrared_range is not None:
            if abs(self.ultrasonic_range - self.infrared_range) <= 20:
                validation_result = "Sensor readings consistent"
            else:
                validation_result = "Sensor readings inconsistent"
            self.get_logger().info(f'Ultrasonic: {self.ultrasonic_range} cm, Infrared: {self.infrared_range} cm, Result: {validation_result}')
            msg = String()
            msg.data = validation_result
            self.validation_publisher.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    msg = String()
    validator_node = ValidatorNode(msg)
    try:
        rclpy.spin(validator_node)
    except KeyboardInterrupt:
        pass
    finally:
        validator_node.destroy_node()
        rclpy.shutdown()    

if __name__ == '__main__':
    main()