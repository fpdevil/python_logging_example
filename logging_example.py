import os
import logging
import logging.config

# get and set the path for log file based on current path
path = os.path.dirname(os.path.realpath(__file__)) + '/logs/example.log'

# refer the configuration file and set the log file name and location
logging.config.fileConfig(fname='log.conf',
                          defaults={'logfilename': path},
                          disable_existing_loggers=False)

# Get the logger specified in the file
log = logging.getLogger('dev')

# log some messages...
log.debug('debug message')
log.info('info message')
log.warning('warn message')
log.error('error message')
log.critical('critical message')
