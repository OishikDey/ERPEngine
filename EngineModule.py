# Emmergency Rescue Protocol Engine
# Project by Oishik Dey 
# This is a module file for the engine code functions

from engi1020.arduino.api import* #importing Arduino functions
from time import sleep #for delaying 
import logging #for debug logging
from datetime import datetime #to get the date of engine initiation

#report logfile setup
now = datetime.now()
starttime = now.strftime("%Y-%m-%d %H %M %S")
logging.basicConfig(filename=f'Report {starttime}.log',
                    format='%(asctime)s %(levelname)s : %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

def sampleCollect(): #Collecting sensor data from 3-axis accelerometer, sound and distance sensor
    x = three_axis_get_accelX()
    y = three_axis_get_accelY()
    z = three_axis_get_accelZ()
    sound = analog_read(2)
    distance = ultra_get_centimeters(3)
    logger.info(f'X: {x}, Y: {y}, Z: {z}, Sound: {sound}, Range: {distance}')
    return [x, y, z, sound, distance]

def SOS_alarm(button = False): #Trigger alarm on meeting certain criterias
    press = [False, False, False]
    logger.debug('Checking button state')
    logger.debug('Buzzer has started ringing')
    while press[2] == False:
        buzzer_note(5, 1200, 1)
        for i in range(3):
            press[i] = digital_read(6)
            sleep(1)
    logger.warning('Button is pressed.')
    buzzer_stop(5)
    logger.debug('Buzzer has been stopped & OLED Screen has been cleared')
    oled_clear()
    logger.info('User is asked to place finger on the heart rate sensor')
    print('Place your finger onto the heart rate sensor')
    oled_print('Checking vitals...')
    heart_rate_start_monitor(2)
    logger.debug('Heart rate sensor has started monitoring')
    check_vitals()
    
def check_vitals(): #Read the heart rate sensor to detect any life signs
    time_counter = 0
    timeout = False
    logger.debug('Reading Heart Rate Sensor')
    vital = heart_rate_get_rate(2)
    while vital <= 2:
        vital = heart_rate_get_rate(2)
        time_counter += 1
        sleep(1)
        if time_counter == 15:
            logger.info('Time limit for sensor reading has been reached.')
            timeout = True
            break
        else:
            continue
    if timeout == True:
        logger.critical('Heart sensor detects no life. Triggering Alarm.')
        print('No life has been detected!!!!')
        print('Press and hold the button again to disable alarm')
        oled_clear()
        oled_print('No signs detected')
        SOS_alarm()
    else:
        buzzer_note(5, 600, 0.1)
        logger.info(f'BPM : {vital}')
        print('Vitals confirmed')
        logger.info('Heart Sensor detects life.')

def reset_engine(button = False): #Reset the engine if any false detection occurs 
    logger.warning('Trigger Termination has been requested to user.')
    print('Press the button within 2 seconds')
    oled_print("It looks like you've been on an accident")
    sleep(2)
    logger.debug('Checking button state')
    button = digital_read(6)
    digital_write(4, False)
    logger.debug('LED is turned OFF')
    if button == True:
        return True
    else:

        return False
