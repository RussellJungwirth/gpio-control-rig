import os
import sys


def str_to_bool(value):
    return str(value).lower() not in ("", "f", "false", "n", "no", "0")


LOG_LEVEL = 'info'
DEBUG_FLAG = str_to_bool(os.getenv('DEBUG_FLAG', '0'))
ENVIRONMENT = os.getenv('ENVIRONMENT', 'prod').lower()


if ENVIRONMENT == 'dev':
    import fake_rpi
    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO  # Fake GPIO
