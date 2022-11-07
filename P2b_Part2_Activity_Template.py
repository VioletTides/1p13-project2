'''
P2b Activity (Part 2 - Create a function to pick up an item, then determine drop-off coordinates for the item)
- Commands are meant to be typed in the Python Shell
'''
## Please DO NOT change the naming convention within this template. Some changes may
## lead to your program not functioning as intended.

ip_address = '172.18.126.253' # Enter your IP Address here
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
define a pick_up() function to pick up an item and return arm to home position
'''
## Write code below this line
#Initial (0.362, 0.362, 0.067)
def pick_up():
    arm.home()
    time.sleep(2)
    arm.move_arm(0.345, 0.412, 0.072)
    time.sleep(2)
    arm.control_gripper(30)
    time.sleep(2)
    arm.move_arm(0.4064, 0.0, 0.4826)
    time.sleep(2)
    arm.control_gripper(-30)



pick_up()
arm.terminate_arm()
'''
Determine xyz coordinates of the drop-off platform
1. Run the module in the Python Shell
2. Move Qarm to drop off item, typing commands in the Python Shell
3. Write down the three drop-off locations (xyz coordinates) for future use
'''
## All commands for finding the drop off location should be typed directly in the Python Shell
## DO NOT WRITE any code below this line


