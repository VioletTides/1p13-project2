'''
P2b Activity (Part 4- Controlling the Q-arm with user input)
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
Define lists of for your pick_up location
'''
## Write code below this line


'''
Paste your pick_up() and mapping() function below
'''
## Write code below this line
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
    
def mapping():
    item_dropped = False

    while (item_dropped == False):
        left_pot = potentiometer.left()
        right_pot = potentiometer.right()
                


'''
while True:
    print(potentiometer.left(),potentiometer.right())
    if potentiometer.left()==0  and potentiometer.right()==0: #if both are turned all the way clockwize
        time.sleep(1)

    elif potentiometer.left()>0.4  and potentiometer.right()<0.4: #Mapping base rotation. Check aganist old value. 
        mapping()
'''

'''
Within a while loop, create conditional statements for controlling item pick up and drop-off. 
'''
## Write your code below this line

def main():
    arm.home()
    time.sleep(2)
    x = 0.45 
    y = 0
    z = 0.162
    
    for i in range(0,4):
        arm.move_arm(x, y, z)
        time.sleep(2)
        arm.control_gripper(35)
        arm.move_arm(0.45, 0.3,0.162)
        time.sleep(2)
        arm.control_gripper(-35)
        z -= 0.035
        x += 0.01
        time.sleep(2)


main()




    




