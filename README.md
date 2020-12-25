Python logger to capture OBD2 metrics as a CSV flat file.

The main idea came from https://github.com/roflson/pyobd and https://github.com/AndrewCloete/pyobd. I tried to adapted the idea to a generic implementation in order to plug-and-play into most vehicles. To configure it to your needs, I would suggest scratching around there.

# Dependencies
- A car with an OBD2 port 😉
- OBD2 USB cable
- A raspberry Pi with Python 3.x installed
- https://github.com/brendan-w/python-OBD via `pip install obd`

# Getting started
```sh
# Install python3
sudo apt-get install python3 python3-pip
pip3 install obd

# Clone this repo into home ~/obd_logger
git clone https://github.com/heetbeet/obd_logger.git ~/obd_logger

# Run ~/obd_logger/obd_logger in your terminal to ensure that everythin is working

# If the above worked, configure the Pi to run the script on startup by adding the following line to /etc/rc.local
bash /home/pi/obd_logger/obd_logger >> /home/pi/logs/obd.log 2>&1 &
```

# My own additions
- VSCode via https://code.visualstudio.com/# ARM 32
- Always boot into HDMI mode: https://raspberrypi.stackexchange.com/a/56140


You should now be able to plug in OBD2 cable into your car and raspberry pi, and retrieve the logs afterwards in `~/logs`
