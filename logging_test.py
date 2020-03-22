import logging

# Create and config logger
LOG_FORMAT = "%(levelname)s - %(name)s - %(asctime)s - %(message)s"

logging.basicConfig(
    filename="logging_test.log", level=logging.DEBUG, format=LOG_FORMAT, filemode="w"
)

logger = logging.getLogger("logging_test")


# Test logging

logger.debug("testing debug")
logger.info("testing")
logger.warning("testing warning")
logger.error("testing error")
logger.critical("testing critical")
