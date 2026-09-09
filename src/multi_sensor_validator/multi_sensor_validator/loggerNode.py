import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from std_msgs.msg import Int32

class logger:
    def log(self, message: str):
        self.get_logger().info(message)

class LoggerNode(Node, logger):
    def __init__(self):
        super().__init__('logger_node')
        self.ultrasonic_range = None
        self.infrared_range = None
        self.ultrasonic_subscriber = self.create_subscription(Int32, '/ultrasonic_range', self.ultrasonic_callback, 10)
        self.infrared_subscriber = self.create_subscription(Int32, '/infrared_range', self.infrared_callback, 10)
        self.get_logger().info('Logger Node has been started.')
        self.validation_subscriber = self.create_subscription(String, '/validation_result', self.validation_callback, 10)

    def ultrasonic_callback(self, msg):
        self.ultrasonic_range = msg.data

    def infrared_callback(self, msg):
        self.infrared_range = msg.data

    def validation_callback(self, msg):
        validation_result = msg.data
        if validation_result == "Sensor readings consistent":
            log_message = f'Ultrasonic: {self.ultrasonic_range} cm, Infrared: {self.infrared_range} cm, Result: {validation_result}'
            self.log(log_message)
        else:
            log_message = f'Ultrasonic: {self.ultrasonic_range} cm, Infrared: {self.infrared_range} cm, Result: {validation_result}'
            self.log(log_message)

    def timer_callback(self):
        pass

    
def main(args=None):
    rclpy.init(args=args)
    logger_node = LoggerNode()
    try:
        rclpy.spin(logger_node)
    except KeyboardInterrupt:
        pass
    finally:
        logger_node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()