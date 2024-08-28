import logging

__logging_format = "%(levelname)s:%(asctime)s  %(message)s"
__datefmt = "%Y/%m/%d %H:%M:%S"

VERBOSE = 15
logging.addLevelName(VERBOSE, "VERBOSE")


def __set_logging_level(level):
    if level == "debug":
        return logging.DEBUG
    else:
        return logging.INFO


def set_logger(logging_level: str):
    logging_level = __set_logging_level(logging_level)
    logging.basicConfig(level=logging_level, format=__logging_format, datefmt=__datefmt)


def info(msg: str):
    logging.info(msg)


def debug(msg: str):
    logging.debug(msg)


def error(msg: str):
    logging.error(msg)


def warning(msg: str):
    logging.warning(msg)
