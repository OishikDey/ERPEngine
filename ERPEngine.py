# EMMERGENCY RESCUE PROTOCOL (ERP) ENGINE
# Project by Oishik Dey 
# ENGI1020, Fall 2022
# This project will track any collusion occurred using
# 3-axis accelerometer (used to detect any collision motion i.e. crash, fall),
# sound (get the sound level of the accidental spot) &
# distance sensor (to get the range between device & object)
# and immediately trigger the emergency rescue protocol,
# which is a set of algorithms checking if the user/driver face serious casualties and
# trigger the alarm if any collusions get detected or it fails to detect life signs.


# Required module file importing
from engi1020.arduino.api import* #importing Arduino functions
from time import sleep #for delaying 
import logging #for debug logging
from datetime import datetime #to get the time & date of engine initiation
from EngineModule import* #self defined engine code functions


# Main engine code
oled_clear()
oled_print('ERPEngine ON')
logger.debug("Engine has started running")
logger.debug("Collecting data")
while True:
    sensor = sampleCollect()
    if (sensor[2] < 0.3 and sensor[3] > 400) or (sensor[4] < 3.0 and sensor[3] > 400) :
        oled_clear()
        print('COLLUISION DETECTED!!!')
        logger.warning('Colluision has been detected.')
        digital_write(4, True)
        logger.debug('LED is turned ON')
        if reset_engine() == False:
            logger.critical('No response. Alarm triggered.')
            print('EMERGENCY RESCUE PROTOCOL ACTIVATED')
            print('Press & hold button for 3 seconds to disarm')
            oled_clear()
            logger.debug('OLED Screen has been cleared')
            logger.debug('Messages are printed on OLED Screen')
            oled_print('Are you OK?')
            oled_print('Sending SOS...')
            SOS_alarm()
            logger.info('Alarm has been disarmed by pressing button & confirming vitals.')
            print('Disabled')
            oled_clear()
            logger.debug('Engine status has been printed on OLED Screen')
            oled_print('DISABLED!!!')
            oled_print('SEEK HELP')
            logger.warning('User has been advised to seek assistance externally')
            logger.debug("Resumed collecting data")
        else:
            logger.info('Button pressed. Engine has been reset.')
            oled_clear()
            logger.debug('OLED Screen has been cleared')
            print("Engine has been reset")
            oled_print("Engine reset")
            oled_print('ERPEngine ON')
            logger.debug('Engine status has been printed on OLED Screen')
            logger.debug("Resumed collecting data")

    sleep(0.1)
