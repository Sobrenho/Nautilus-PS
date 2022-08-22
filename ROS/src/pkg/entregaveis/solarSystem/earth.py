#!/usr/bin/env python3

import rospy
from broadcasterTF import Broadcaster

if __name__ == '__main__':
    try:
        a = Broadcaster("earth")
        a.startBroadcast(1,2)
        
    except rospy.ROSInterruptException :
        pass