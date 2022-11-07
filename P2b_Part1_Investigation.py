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
1. Run this program
2. In the python shell, try all functions in the Q-arm Movement section,
     controling the gripper section, q-arm position section and the terminate arm section.  
'''

## All commands should be typed directly in the Python Shell
## DO NOT WRITE any code below this line

# IMPORTANT: Call function below before power off to return the arm in a safe position.
#arm.terminate_arm()



