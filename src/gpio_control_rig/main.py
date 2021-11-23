import logging
from . import config # , utils, reader, writer


logger = logging.getLogger(__name__)


def main():
    """
    Primary entrypoint for
    """
    print("run package from main")

    logger = logging.getLogger(__name__)
    logger.setLevel(config.LOG_LEVEL)
    logger.info(f"start package from main")

    logger.info(f"end package from main")
