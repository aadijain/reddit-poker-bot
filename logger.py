import logging
import logging.handlers

LOG_FILENAME = 'backup.out'

# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
log_formatter = logging.Formatter('%(asctime)s %(message)s')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1*1024*1024, backupCount=5)
handler.setFormatter(log_formatter)
my_logger.addHandler(handler)

# Log some messages
msg_old = ''
def log(msg):
    global msg_old
    if(str(msg) == str(msg_old)):
        my_logger.debug(msg)
        msg_old = msg