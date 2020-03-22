import logging

# Create and config logger
LOG_FORMAT = "%(asctime)s - [%(levelname)s] - <%(name)s> - %(message)s"

"""logging.basicConfig(
    filename="logging_test.log", level=logging.DEBUG, format=LOG_FORMAT, filemode="w"
)

# logger = logging.getLogger("logging_test")
logger = logging.getLogger(__name__)"""

# -------------------------------------------------------------------------------#
# Advanced setup

# Set name of logger
logger = logging.getLogger(__name__)

# Set level of logger
logger.setLevel(logging.DEBUG)

# Set format for log message
formatter = logging.Formatter(LOG_FORMAT)

# Create a file handler and specify log file
file_handler = logging.FileHandler("logging_test_adv.log")

# Apply format to file handler
file_handler.setFormatter(formatter)

# Create a stream handler to enable cosole logging
stream_handler = logging.StreamHandler()

# Apply format to stream handler
stream_handler.setFormatter(formatter)

# Add file handler to logger
logger.addHandler(file_handler)

# Add stream handler to logger
logger.addHandler(stream_handler)


# Test logging

logger.debug("testing debug")
logger.info("testing info")
logger.warning("testing warning")
logger.error("testing error")
logger.critical("testing critical")
