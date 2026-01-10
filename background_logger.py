# -*- coding: utf-8 -*-
import sys
import time
import bme280
import rrdtool

def writeTmp():
    ret = rrdtool.graph("/media/kingdian/graph1.png",
                  '--color', 'CANVAS#000000',
                  '--color', 'FONT#07FFFE',
                  '--color', 'BACK#000000',
                  '--color', 'MGRID#0066FF',
                  '--right-axis', '1:0',
                  '--right-axis-format', '%2.1lf',
                  '--imgformat', 'PNG',
                  '--width', '790',
                  '--height', '300',
                  '--start', "-64800",
                  '--end', "now",
                  '--vertical-label', '°Celsius',
                  '--title', 'BME280_sensor_temp',
                  #'--lower-limit', '0',
                  'DEF:temperature=/media/kingdian/climate_data.rrd:temperature:MAX',
                  'LINE1:temperature#8700af:temperature')

def writeHumPrs():
    ret = rrdtool.graph("/media/kingdian/graph2.png",
                  '--color', 'CANVAS#000000',
                  '--color', 'FONT#07FFFE',
                  '--color', 'BACK#000000',
                  '--color', 'MGRID#0066FF',
                  '--right-axis', '1:950',
                  '--right-axis-format', '%4.0lf',
                  '--imgformat', 'PNG',
                  '--width', '790',
                  '--height', '300',
                  '--start', "-64800",
                  '--end', "now",
                  '--vertical-label', 'rel.% \ hPa',
                  '--title', 'BME280_sensor_prhm',
                  'DEF:humidity=/media/kingdian/climate_data.rrd:humidity:MAX',
                  'DEF:pressure=/media/kingdian/climate_data.rrd:pressure:MAX',
                  "CDEF:scaled_pressure=pressure,950,-",
                  'LINE1:humidity#ffff87:humidity',
                  'LINE2:scaled_pressure#ffaf00:pressure')

while True:
    temperature,pressure,humidity = bme280.readBME280All()
    temperature -= 1.65
    pressure += 13.3
    humidity += 6.4
    ret = rrdtool.update('/media/kingdian/climate_data.rrd','N:' + `temperature` + ':' + `humidity` + ':' + `pressure`)
    print "Temperature : ", temperature, "°C ---", " Pressure : ", pressure, "hPa ---", " Humidity : ", humidity
    sys.stdout.flush()
    writeTmp()
    writeHumPrs()
    time.sleep(60)
