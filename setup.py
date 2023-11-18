#!_venv/bin/python3
from setuptools import setup, find_packages
import os
import os.path
import codecs
import sys


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

requirements = [
    'wheel',
    'RPi.GPIO',
    'gpiozero',
    'numpy<=1.21.4',
    'cython',
]

if __name__ == '__main__':
    test_release = False
    if "--test-release" in sys.argv:
        test_release = True
        sys.argv.remove("--test-release")

    final_requirements = []
    for req in requirements:
        if test_release and req == 'RPi.GPIO':
            final_requirements.append('fake-rpi')
        else:
            final_requirements.append(req)
    print(f"final requirements {final_requirements}")
    setup(
        name='gpio_control_rig',
        version=get_version("gpio_control_rig/__init__.py"),
        license='None',
        package_dir={'': 'src'},
        packages=find_packages("src"),
        description='Raspberry Pi GPIO control rig',
        install_requires=final_requirements,
    )
