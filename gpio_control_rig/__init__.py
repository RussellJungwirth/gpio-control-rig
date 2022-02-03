import os
import sys

__version__ = '0.0.1'

if os.getenv('ENVIRONMENT', 'prod').lower() == 'dev':
    print('environment set to DEV')
    import fake_rpi
    sys.modules['RPi'] = fake_rpi.RPi  # Fake RPi
    sys.modules['RPi.GPIO'] = fake_rpi.RPi.GPIO  # Fake GPIO
