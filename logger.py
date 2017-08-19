import logging
import logging.handlers

LOG_FILENAME = 'bot.log'
DUMP_FILENAME = 'data.out'

# Set up a specific logger
my_logger = logging.getLogger('MyLogger')
log_formatter = logging.Formatter('%(asctime)s %(message)s')
my_logger.setLevel(logging.DEBUG)

# Add the log message handler to the logger
handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1*1024*1024, backupCount=5)
handler.setFormatter(log_formatter)
my_logger.addHandler(handler)

# Set up a specific dumper
my_dumper = logging.getLogger('MyDumper')
dump_formatter = logging.Formatter('%(message)s')
my_dumper.setLevel(logging.DEBUG)

# Add the dump message handler to the dumper
handler2 = logging.handlers.RotatingFileHandler(DUMP_FILENAME, maxBytes=1*1024*1024, backupCount=3)
handler2.setFormatter(dump_formatter)
my_dumper.addHandler(handler2)

# Log some messages
def log(msg, C_ID=None):
    if(C_ID):
        my_logger.debug(C_ID)
    my_logger.debug(msg)

# Dump Data
def dump(var):
    my_dumper.debug(var)