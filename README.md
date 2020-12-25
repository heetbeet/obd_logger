Python logger to capture OBD2 metrics as a CSV flat file.

I copied this repo from https://github.com/roflson/pyobd and adapted it to run on a Raspberry PI B. Specifically I adapted the `obd_recorder.py` file with my specific needs. To configure it to your needs, I would suggest scratching around there. The original author did not use any sort of environment config so take it as is.

# Dependencies
- A car with an OBD2 port 😉
- OBD2 USB cable
- A raspberry Pi with Python 3.x installed.

# Getting started
```sh
# Copy the code to the home dir of your PI (configure the IP adr)
# This assumes that the pi is on your network 
PI_IP="192.168.8.119"
rsync -ra .../pyobd pi@:$PI_IP/home/pi/


# Plug the OBD2 cable into your car and test by running the following on the Pi.
# (for my specific car I had to start the engine first). 
# If this works it should produce a /home/pi/pyobd/logs directory that contains the CSV capture (see example_output/)
/home/pi/pyobd/obd_recorder.py

# If the above worked, configure the Pi to run the script on startup by adding the following line to /etc/rc.local
/home/pi/pyobd/obd_recorder.py >> /home/pi/obd.log 2>&1 &

# My procedure was to always start the car, then plug in the Pi power to start the logging. Your car might be different.
# Remeber to NOT leave the Pi plugged in for long time while the engine is off since it will eventually drain your battery 
```

# Resources
- This original repo: https://github.com/roflson/pyobd
- List of OBD2 tools: https://www.elmelectronics.com/help/obd/software/#Linux
