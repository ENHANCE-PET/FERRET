# setup.py for ferretz
from setuptools import setup, find_packages

setup(
    name='ferretz',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': ['ferretz=ferretz.ferretz:main'],
    },
    # other metadata and requirements
)
