ip_address = '172.17.160.87' # Enter your IP Address here
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
Determine xyz coordinates for the pick-up location
1. Run the module in the Python Shell
2. Move Qarm to pick up an ITEM, typing commands in the Python Shell
3. Write down item pick-up location xyz coordinates for future use
4. Repeat steps 2 and 3 to find and record the coordinates of the home position
'''

## All commands should be typed directly in the Python Shell
## DO NOT WRITE any code below this line



# IMPORTANT: Call function below before power off to return the arm in a safe position.
#arm.terminate_arm()




