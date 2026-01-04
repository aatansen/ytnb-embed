from ytnb_embed.logger import logger
from ytnb_embed.custom_exception import InvalidURLException

# logger.info("This is a test log message from test.py")

try:
    raise InvalidURLException()
except Exception as e:
    logger.error(f"Caught an exception: {e}")