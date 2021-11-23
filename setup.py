
from setuptools import setup, find_packages
import os
import os.path
import codecs


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

# # pip install fake-rpi
# if app.env == 'development':
#     import FakeRPi.GPIO as GPIO
# else:
#     import RPi.GPIO as GPIO

requirements = [
    'RPi.GPIO'
]

test_requirements = [
    'pytest-cov',
    'pytest-timeout',
    'pytest-integration',
    'flake8',
    'pep8-naming',
    'autopep8',
    'ptvsd==5.0.0a12',
    'yapf',
    'fake-rpi',
]

if __name__ == '__main__':
    setup(
        name='gpio_control_rig',
        version=get_version("src/gpio_control_rig/__init__.py"),
        license='None',
        package_dir={'': 'src'},
        packages=find_packages("src"),
        description='Raspberry Pi GPIO control rig'
    )
