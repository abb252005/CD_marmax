#!/usr/bin/env python3
import rospy
from turtlesim.srv import Spawn, Kill
def setup_turtles():
    rospy.init_node('turtle_spawner')
    rospy.wait_for_service('kill')
    rospy.wait_for_service('spawn')
    spawner = rospy.ServiceProxy('spawn', Spawn)
    killer = rospy.ServiceProxy('kill', Kill)
    try: killer('turtle1')
    except: pass

    spawner(1.65, 3.75, -1.175, "t0")
    spawner(4.3, 5.5, 1, "t1")
    spawner(6.5, 6.6, 0.37, "t3")
    spawner(9.5, 6.6, 0.37, "t32")

if __name__ == '__main__':
    setup_turtles()