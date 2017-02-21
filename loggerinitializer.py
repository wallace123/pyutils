""" Logging function """
import logging


def initialize_logger(log_file):
    """ Sets logging level as info, messages go to file and
        stdout except for debug messages
    """
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    shandler = logging.StreamHandler()
    shandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(levelname)s - [%(filename)s.%(funcName)s] -- %(message)s')
    shandler.setFormatter(formatter)
    logger.addHandler(shandler)

    fhandler = logging.FileHandler(log_file, 'w', encoding=None, delay='true')
    fhandler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s - [%(filename)s.%(funcName)s] -- %(message)s')
    fhandler.setFormatter(formatter)
    logger.addHandler(fhandler)
