#!/usr/bin/env python3

import rospy
from broadcasterTF import Broadcaster

if __name__ == '__main__':
    try:
        a = Broadcaster("earth")
        a.startBroadcast(0,0)
        
    except rospy.ROSInterruptException :
        pass