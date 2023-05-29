import rclpy
from rclpy.node import Node
from std_msgs.msg import String

"""
导入消息类型
声明并创建发布者
编写发布逻辑
"""

class WriterNode(Node):

    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("Hello, i am writer %s" %name)
        self.pub_novel = self.create_publisher(String, "sexy_girl", 10)

        self.chapterCount = 0

        self.timer_period = 5
        self.timer = self.create_timer(self.timer_period, self.timer_callback)


        

    def timer_callback(self):
        msg = String()
        msg.data = "Chapter %d:%dth meet Miss Hu" % (self.chapterCount, self.chapterCount)

        self.pub_novel.publish(msg)
        self.get_logger().info("Li4 say %s" % msg.data)

        self.chapterCount += 1




def main(args=None):

    rclpy.init(args=args)
    li4_node = WriterNode("li4")
    # li4_node.get_logger().info("hello, i am writer li4")

    rclpy.spin(li4_node)
    rclpy.shutdown()