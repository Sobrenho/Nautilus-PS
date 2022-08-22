#!/usr/bin/env python3

import rospy
from broadcasterTF import Broadcaster

if __name__ == '__main__':
    try:
        a = Broadcaster("jupiter")
        a.startBroadcast(1,1)      
    except rospy.ROSInterruptException :
        pass