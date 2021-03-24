from C12_GenericLogger import getCustomLogger
import logging
def f1():
 logger = getCustomLogger(logging.DEBUG)
 logger.critical('critical message')
 logger.error('error message')
 logger.warning('warning message')
 logger.info('info message')
 logger.debug('debug message')

def f2():
 logger = getCustomLogger(logging.ERROR)
 logger.critical('critical message')
 logger.error('error message')
 logger.warning('warning message')
 logger.info('info message')
 logger.debug('debug message')


f1()
f2()