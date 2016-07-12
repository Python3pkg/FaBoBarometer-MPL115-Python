# coding: utf-8
## @package FaBoBarometer_MPL115
#  This is a library for the FaBo Barometer I2C Brick.
#
#  http://fabo.io/204.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>


import FaBoBarometer_MPL115
import time
import sys

mpl115 = FaBoBarometer_MPL115.MPL115()

try:
    while True:
        data  = mpl115.readData()
        a_hpa = mpl115.readHpa(212.0)

        print "hpa  = ", data['hpa']
        print "temp = ", data['temp']
        print "hpa_aizu = ", a_hpa
        print
        time.sleep(1)

except KeyboardInterrupt:
    sys.exit()
