#!/usr/bin/env python3
import rospy

rospy.init_node("rosparam exemplo")
rospy.set_param('rate/imu', 50)
while not rospy.is_shutdown():
    param = rospy.get_param('/rate/imu')
    rospy.loginfo(param)