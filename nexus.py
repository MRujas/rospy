#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)
    pub.publish(" Mensaje final %s" % rospy.get_time())

if __name__ == '__main__':
    rospy.init_node('mediador', anonymous=True)
    pub = rospy.Publisher('final', String, queue_size=10)
    sub = rospy.Subscriber('inicial', String, callback)
    rospy.loginfo("Inicializacion completa")
    rospy.spin()
