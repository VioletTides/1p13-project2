'''
Student: follow the instructions below
- Run the module
- Type commands into the Python Shell as instructed
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
DEMO #2 - Pick up an item and return home
1. The following program follows the general workflow to:
    a. Start by going to the home position
    b. Go to a random location
    c. Close the grippers a specified amount to pick up an item
    e. Move to the home position
    f. Open the grippers
2. Run this code and type pick_up() into the shell to watch the function work. 
'''
def pick_up():
    arm.home()
    time.sleep(2)
    arm.move_arm(0.537, 0.002, 0.072) #This is a random pick up location
    time.sleep(2)
    arm.control_gripper(40)
    time.sleep(2)
    arm.move_arm(0.4064, 0.0, 0.4826)
    time.sleep(2)
    arm.control_gripper(-40)

pick_up()

## All commands should be typed directly in the Python Shell
## DO NOT WRITE any code below this line













