#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def talker_test():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker_test', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "Anand is er niet op tijdstip %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker_test()
    except rospy.ROSInterruptException:
        pass
