#!/usr/bin/env python3

import rospy
from math import sqrt
from geometry_msgs.msg import Twist
from std_msgs.msg import Float64


class Listener():
    def __init__(self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('topico1', Twist, self.callback)
        self.resultado = rospy.Publisher('topico2', Float64, queue_size=10)


    def callback(self, msg):
        
        velAng_x, velAng_y, velAng_z = msg.angular.x, msg.angular.y, msg.angular.x
        modVelocidadeAngular = Float64()
        modVelocidadeAngular.data = sqrt(velAng_x**2 +  velAng_y**2 +  velAng_z**2)

        velLin_x, velLin_y, velLin_z = msg.linear.x, msg.linear.y, msg.linear.z
        modVelocidadeLinear = Float64()
        modVelocidadeLinear.data = sqrt(velLin_x**2 +  velLin_y**2 +  velLin_z**2)
        

        rospy.loginfo('Velocidade Angular')
        rospy.loginfo(modVelocidadeAngular)
        self.resultado.publish(modVelocidadeAngular)


        rospy.loginfo('Velocidade Linear')
        rospy.loginfo(modVelocidadeLinear)
        self.resultado.publish(modVelocidadeLinear)

if __name__ == '__main__':
    l = Listener()
    rospy.spin()
    

        