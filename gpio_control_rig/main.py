import logging
from . import config  # , utils, reader, writer


logger = logging.getLogger(__name__)


def main():
    """
    Primary entrypoint for
    """
    print("run package from main")

    logger = logging.getLogger(__name__)
    logger.setLevel(config.LOG_LEVEL)
    logger.info("start package from main")

    logger.info("end package from main")
