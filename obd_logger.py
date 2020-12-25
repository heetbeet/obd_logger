import obd
import time
import datetime
import traceback
import time
import logging
import os

print("**********************************")
print("Starting ", str(datetime.datetime.now()))
print("**********************************", flush=True)

# Redirect odb logger warnings and logger errors to actual python errors
class LevelRaiser(logging.Handler):

    def emit(self, record: logging.LogRecord):
        if record.levelno == logging.WARNING or record.levelno == logging.ERROR:
            raise ValueError(record.getMessage())

for key, value in obd.__dict__.items():
    if hasattr(value, "__name__") and isinstance(value.__name__, str):
        library_root_logger = logging.getLogger(value.__name__)
        library_root_logger.addHandler(LevelRaiser())

try:
    # auto-connects to USB or RF port
    connection = obd.OBD() 

    # find car's compatable commands
    supported_headers = [i for i in dir(obd.commands) if isinstance(getattr(obd.commands, i), obd.OBDCommand) and
                                                        connection.supports(getattr(obd.commands, i))]


    # read car's vitals line by line and write to csv
    localtime = time.localtime(time.time())
    os.mkdirs("/home/pi/logs", exist_ok=True)
    filename = "/home/pi/logs/carlogger-"+str(localtime[0])+"-"+str(localtime[1])+"-"+str(localtime[2])+"-"+str(localtime[3])+"-"+str(localtime[4])+"-"+str(localtime[5])+".csv"

    with open(filename, "a") as fw:
        fw.write(",".join(['TIME']+supported_headers) + "\n")

    while(True):
        vals = [str(datetime.datetime.now())]
        errs = 0
        for i in supported_headers:
            try:
                vals.append(str(connection.query(getattr(obd.commands, i)).value))
            except Exception as e:
                vals.append(str(e))
                errs += 1

        with open(filename, "a") as fw:
            fw.write('"' + ('","'.join([i.replace('"', "'") for i in vals])) + '"\n')

        # if half of the headers end in errors, then a restart error is probably needed
        if int(len(supported_headers)/2) <= errs:
            raise ValueError("Too many errors during readings")

finally:
    # Try to keep connection closed
    try:
        connection.close()
    except:
        pass