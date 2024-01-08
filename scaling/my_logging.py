import logging


logging.basicConfig(
	filename="test.log",
	level=logging.INFO,
	format='%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s',
	datefmt='%Y-%m-%d %H:%m:%S'
)

logger = logging.getLogger()
logger.info('TEST PRINT')