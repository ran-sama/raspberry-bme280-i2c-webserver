# raspberry-bme280-i2c-webserver
Read from a BME280 and plot the data to display on a webserver.

![alt text](https://raw.githubusercontent.com/ran-sama/bme280_i2c_raspberry_webserver/master/climate.png)

## Download dependencies, create a database and run the logger
```
wget https://bitbucket.org/MattHawkinsUK/rpispy-misc/raw/master/python/bme280.py
sudo apt install rrdtool
sudo apt install python-rrdtool
rrdtool create climate_data.rrd --step 60 DS:temperature:GAUGE:600:0:40 DS:humidity:GAUGE:600:0:100 DS:pressure:GAUGE:600:800:1200 RRA:MAX:0.5:1:1080
sudo python background_logger.py
python -m SimpleHTTPServer
```
![alt text](https://raw.githubusercontent.com/ran-sama/bme280_i2c_raspberry_webserver/master/device_photo.jpg)

## Weekly Database example
```
rrdtool create climate_data.rrd --step 600 DS:temperature:GAUGE:1800:0:40 DS:humidity:GAUGE:1800:0:100 DS:pressure:GAUGE:1800:800:1200 RRA:MAX:0.5:1:1008
```
## Guide to create own databases
https://apfelboymchen.net/gnu/rrd/create/

## License
Licensed under the WTFPL license.
