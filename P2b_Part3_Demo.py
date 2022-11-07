'''
Student: follow the instructions below
- Copy the TA's code to complete the demonstrations
'''
## Please DO NOT change the naming convention within this template. Some changes may
## lead to your program not functioning as intended.

ip_address = '172.17.46.238' # Enter your IP Address here
project_identifier = 'P2A' # Enter the project identifier i.e. P2A or P2B
#--------------------------------------------------------------------------------
import sys
sys.path.append('../')
from Common.hardware_project_library import *

hardware = True
QLabs = configure_environment(project_identifier, ip_address, hardware).QLabs
arm = qarm(project_identifier,ip_address,QLabs,hardware)
potentiometer = potentiometer_interface()

## *******************************************
## DO NOT EDIT ANY OF THE CODE ABOVE THIS LINE
## *******************************************

'''
DEMO #3 - Pick up and drop-off an item with the Q-arm

    Note that all locations are random

'''

pick_up_location = [0.537, 0.002, 0.072] #Random Pick Up Location
drop_off_location = [0.038, -0.536, 0.073] #Random Drop Off Location

def pick_up():
    time.sleep(2) 
    arm.move_arm(pick_up_location[0],pick_up_location[1],pick_up_location[2])
    time.sleep(2)
    arm.control_gripper(40)
    time.sleep(2)
    arm.move_arm(0.4064, 0.0, 0.4826)
    time.sleep(2)
    
pick_up() 

arm.move_arm(drop_off_location[0],drop_off_location[1],drop_off_location[2])
time.sleep(3)
arm.control_gripper(-40)
time.sleep(2)
arm.move_arm(0.4064, 0.0, 0.4826)

arm.terminate_arm()



    












