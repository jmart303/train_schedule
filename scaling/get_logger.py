import logging

logging.basicConfig(
	filename='my_log',
	datefmt='%Y-%d-%m %H:%m:%S',
	level=logging.INFO,
	format='%(asctime)s %(message)s'
)

logger = logging.getLogger()

logger.info('hello log')