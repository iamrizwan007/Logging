import logging
logger = logging.getLogger('module2logger')
logger.setLevel(logging.DEBUG)

fileHandler = logging.FileHandler('module2.log',mode='w')

fileHandler.setLevel(logging.ERROR)

formatter = logging.Formatter('%(asctime)s %(levelname)s %(name)s %(message)s',datefmt='%d/%m%Y %I:%M:%S %p')

fileHandler.setFormatter(formatter)

logger.addHandler(fileHandler)

logger.critical('module 2 critical message')
logger.error('module 2 error message')
logger.warning('module 2 warning message')
logger.info('module 2 info message')
logger.debug('module 2 debug message')