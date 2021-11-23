import os


def str_to_bool(value):
    return str(value).lower() not in ("", "f", "false", "n", "no", "0")

LOG_LEVEL = 'info'
DEBUG_FLAG = str_to_bool(os.getenv('DEBUG_FLAG', '0'))
