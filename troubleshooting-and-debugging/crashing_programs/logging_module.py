import logging

logging.basicConfig(filename="app.log", format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logging.error('This is an error with a custom format')
logging.warning('This is a warning message')
logging.error('This is an error message')

logging.debug('This is a debug message')
