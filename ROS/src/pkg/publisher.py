#!/usr/bin/env python3

import rospy, random
from geometry_msgs.msg import Twist

class Talker:
    def __init__(self):
        rospy.init_node('talker', anonymous=True)
        self.pub = rospy.Publisher('topico1', Twist, queue_size=10)

    
    def startPublishing(self):
        rate = rospy.Rate(5) # 5Hz = 5 vezes por segundo  
        while not rospy.is_shutdown():
            vel = Twist()
            vel.angular.x = random.uniform(-5,10)
            vel.angular.y = random.uniform(-5,10)
            vel.angular.z = random.uniform(-5,10)

            vel.linear.x = random.uniform(-5,15)
            vel.linear.y = random.uniform(-5,15)
            vel.linear.z = random.uniform(-5,15)
            
            rospy.loginfo(vel) 
            self.pub.publish(vel) 
            rate.sleep() 


if __name__ == '__main__':
    try:
        t = Talker()
        t.startPublishing()
    except rospy.ROSInterruptException:
        pass