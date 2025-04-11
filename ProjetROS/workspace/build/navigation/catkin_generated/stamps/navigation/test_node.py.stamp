#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('test_node', anonymous=True)
    rate = rospy.Rate(1)  # 1 Hz

    count = 0
    while not rospy.is_shutdown():
        message = f"Yo ROS, je suis vivant 😎 {count}"
        rospy.loginfo(message)
        pub.publish(message)
        count += 1
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
