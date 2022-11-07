'''
P2b Demo (Part 4 - User Controlled Q-Arm)
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
Given Demo

This program allows user to control the Q-Arm rotations by using EMG/Potentiometer data.

The current program runs such that:

if both read less 0
    -Do nothing
else if left greater than 0.4, right less than 0.4
    -Rotate base



'''
def mapping():
    item_dropped = False

    old_reading = potentiometer.left()

    while not item_dropped:

        if potentiometer.left() > 0.4:
            new_reading = potentiometer.left()
            delta = new_reading - old_reading
            increment = 348*delta
            arm.rotate_base(increment)
            time.sleep(0.2)
            print(potentiometer.left(),potentiometer.right())
            old_reading = new_reading
           
        elif (potentiometer.right() > 0.4):
            arm.control_gripper(-45)
            time.sleep(2)
            item_dropped = True


while True:
    print(potentiometer.left(),potentiometer.right())
    if potentiometer.left()==0  and potentiometer.right()==0: #if both are turned all the way clockwize
        time.sleep(1)

    elif potentiometer.left()>0.4  and potentiometer.right()<0.4: #Mapping base rotation. Check aganist old value. 
        mapping()


'''
Run this file and control the Q-arm with the potentiometers.

Add ONE more else if statement to control the wrist.

'''
### Write your code below this line to control the wrist. 


###   Ensure the elif statement is properly indented!


    


















