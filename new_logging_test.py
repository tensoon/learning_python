import time
import re
import os
import stat
import logging
import logging.handlers as handlers


class SizedTimedRotatingFileHandler(handlers.TimedRotatingFileHandler):
    """
    Handler for logging to a set of files, which switches from one file
    to the next when the current file reaches a certain size, or at certain
    timed intervals
    """

    def __init__(
        self,
        filename,
        maxBytes=0,
        backupCount=0,
        encoding=None,
        delay=0,
        when="h",
        interval=1,
        utc=False,
    ):
        handlers.TimedRotatingFileHandler.__init__(
            self, filename, when, interval, backupCount, encoding, delay, utc
        )
        self.maxBytes = maxBytes

    def shouldRollover(self, record):
        """
        Determine if rollover should occur.

        Basically, see if the supplied record would cause the file to exceed
        the size limit we have.
        """
        if self.stream is None:  # delay was set...
            self.stream = self._open()
        if self.maxBytes > 0:  # are we rolling over?
            msg = "%s\n" % self.format(record)
            # due to non-posix-compliant Windows feature
            self.stream.seek(0, 2)
            if self.stream.tell() + len(msg) >= self.maxBytes:
                return 1
        t = int(time.time())
        if t >= self.rolloverAt:
            return 1
        return 0


def demo_SizedTimedRotatingFileHandler():
    log_filename = "log_rotate"
    logger = logging.getLogger("MyLogger")
    logger.setLevel(logging.DEBUG)
    handler = SizedTimedRotatingFileHandler(
        log_filename,
        maxBytes=100,
        backupCount=5,
        when="s",
        interval=10,
        # encoding="bz2",  # uncomment for bz2 compression
    )
    logger.addHandler(handler)
    for i in range(10000):
        time.sleep(0.1)
        logger.debug("i=%d" % i)


demo_SizedTimedRotatingFileHandler()
