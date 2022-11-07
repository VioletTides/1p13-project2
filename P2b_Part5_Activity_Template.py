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


#---------------------------------------------------------------------------------
# STUDENT CODE BEGINS
#---------------------------------------------------------------------------------

#insert the recorded values for each channel on the ADC, then run this module.
ch0_low = 
ch0_high = 
ch1_low = 
ch1_high = 
ch2_low = 
ch2_high =

arm.match_movements(ch0_low, ch0_high, ch1_low, ch1_high, ch2_low, ch2_high)

#---------------------------------------------------------------------------------
# STUDENT CODE ENDS
#---------------------------------------------------------------------------------
