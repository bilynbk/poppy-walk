#~ import sensors 

import time


#############
# PARAMATERS
#############

### Robot config ###
FULL_POPPY_HUMANOID = True
robot_configuration_file = "/home/poppy/poppy.json" #Needed only if FULL_POPPY_HUMANOID is False

HAS_IMU = False
imu_model = "razor"

HAS_FOOT_SENSORS = False
###

### Activated modules ###


HAS_FORWARD_KINEMATICS = False
HAS_INVERSE_KINEMATICS = False

USE_ZMP = False
USE_PHASE_DIAGRAM = False

up_foot_trajectory = "CPG" #CPG|play_move

DO_TORSO_STABILIZATION = False
torso_stabilization = "vertical"


###

#TODO conditional imports here


#TODO: when we have several functions of that type, create a utils scipt
def createPoppyCreature():
    poppy = None
    if FULL_POPPY_HUMANOID:
        from poppy_humanoid import PoppyHumanoid
        try:
            from poppy_humanoid import PoppyHumanoid
            poppy = PoppyHumanoid()
        except Exception,e:
            print "could not create poppy object"
            print e
    else:
        import pypot.robot 
        try:
            
            with open(robot_configuration_file) as f:
                poppy_config = json.load(f)  
            poppy = pypot.robot.from_config(poppy_config)
            poppy.start_sync()
        except Exception,e:
            print "could not create poppy object"
            print e
        
    return poppy
    


#############
## MAIN
#############

poppy = None #createPoppyCreature()


import Walker

walker = Walker.Walker(poppy)

walker.init()
walker.startWalk()

for i in range(0, 10):
    walker.oneStep()

walker.stopWalk()

walker.clean()


if not FULL_POPPY_HUMANOID:
    poppy.stop_sync()
    poppy.close()





