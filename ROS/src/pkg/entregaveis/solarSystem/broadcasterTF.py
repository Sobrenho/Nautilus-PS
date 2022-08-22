#!/usr/bin/env python3

import rospy
import tf2_ros
import math
import geometry_msgs.msg


class Broadcaster:
  
    def __init__(self, node):
        rospy.init_node(node, anonymous=True)
        self.bc = tf2_ros.TransformBroadcaster()        
  
    def startBroadcast(self, planet_id, natSat_id):
        t = geometry_msgs.msg.TransformStamped()
        t2 = geometry_msgs.msg.TransformStamped()

        paramNatSat = rospy.get_param("/solarsystem/celestial_bodies/natural_satellites")[natSat_id]
        paramPlanet = rospy.get_param("/solarsystem/celestial_bodies/planets")[planet_id]

        t.header.frame_id = rospy.get_param("/solarsystem/celestial_bodies/stars")[0]["name"]
        t.child_frame_id  = paramPlanet["name"]

        t2.header.frame_id = paramPlanet["name"]
        t2.child_frame_id  = paramNatSat["name"]

        rate = rospy.Rate(rospy.get_param("/solarsystem/rate"))
        while not rospy.is_shutdown():
            theta = rospy.Time.now().to_sec() * math.pi

            #A velocidade da órbita é maior em corpos mais próximos do Sol
            t.header.stamp = rospy.Time.now()
            t.transform.translation.x = paramPlanet["orbit_radius"]*math.sin(theta/paramPlanet["orbit_radius"])
            t.transform.translation.y = paramPlanet["orbit_radius"]*math.cos(theta/paramPlanet["orbit_radius"]) 
            t.transform.translation.z = 0
            
            t.transform.rotation.x  = 0
            t.transform.rotation.y  = 0
            t.transform.rotation.z  = 0
            t.transform.rotation.w  = 1

            #A relação com o raio de órbita abaixo foi adicionada apenas para tornar o sistema mais assimétrico
            t2.header.stamp = rospy.Time.now()
            t2.transform.translation.x = math.sin((paramPlanet["orbit_radius"]/3.5)*theta)
            t2.transform.translation.y = math.cos((paramPlanet["orbit_radius"]/3.5)*theta) 
            t2.transform.translation.z = 0
            
            t2.transform.rotation.x  = 0
            t2.transform.rotation.y  = 0
            t2.transform.rotation.z  = 0
            t2.transform.rotation.w  = 1

            self.bc.sendTransform(t)
            self.bc.sendTransform(t2)
            rospy.loginfo(t)
            rospy.loginfo(t2)
            rate.sleep()

