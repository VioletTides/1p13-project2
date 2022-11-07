'''
P2b Activity (Part 3 - Pick up and stack)
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
Paste pick_up() function from Activity 2 here
'''
## Write code below this line
arm.terminate_arm()
arm.home()


pick_up_location = [0.362, 0.362, 0.117]
drop_off_location = [0.038, -0.536, 0.073]

def pick_up():
    time.sleep(2) 
    arm.move_arm(pick_up_location[0],pick_up_location[1],pick_up_location[2])
    time.sleep(2)
    arm.control_gripper(20)
    time.sleep(2)
    arm.move_arm(0.4064, 0.0, 0.4826)
    time.sleep(2)

    
for i in range(3):
    pick_up_location[2] = pick_up_location[2] - (i)*(0.02)
    drop_off_location[2] = drop_off_location[2] + (i)*(0.02)
    
    pick_up()
    arm.move_arm(drop_off_location[0],drop_off_location[1],drop_off_location[2])
    time.sleep(3)
    arm.control_gripper(-20)
    time.sleep(2)
    arm.move_arm(0.4064, 0.0, 0.4826)

arm.terminate_arm()
'''
Run the module.
In the shell, call on the pick_up() function and the Q_arm functions to stack all items at a single drop-off location.
    - Give all group members equal opportunities to gain experience and confidence with the Q-Arm
'''
## Write code below this line

    

