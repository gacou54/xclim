#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""
import subprocess

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


NAME = "xclim"
DESCRIPTION = "Derived climate variables built with xarray."
URL = "https://github.com/Ouranosinc/xclim"
AUTHOR = "Travis Logan"
AUTHOR_EMAIL = "logan.travis@ouranos.ca"
REQUIRES_PYTHON = ">=3.5.0"
VERSION = "0.10.8-beta"
LICENSE = "Apache Software License 2.0"
REQUIREMENTS = [
    "scipy>=1.2",
    "numpy>=1.15",
    "pandas>=0.23",
    "cftime>=1.0.3",
    "netCDF4>=1.4",
    "dask[complete]",
    "bottleneck>=1.2.1",
    "xarray>=0.12.0",
    "pyproj>=1.9.5.1",
    "pint>=0.8",
    "boltons>=18.0",
]
DOCS_REQUIREMENTS = ["sphinx", "guzzle-sphinx-theme", "nbsphinx", "pandoc", "ipython"]
KEYWORDS = "xclim climate climatology netcdf gridded analysis"

FLAKE8_COMMAND = ['./venv/bin/flake8', 'xclim', 'tests']
BLACK_COMMAND = ['./venv/bin/black', '--check', 'xclim', 'tests']
TESTS_COMMAND = ['./venv/bin/python', '-m', 'pytest']

with open("README.rst") as readme_file:
    README = readme_file.read()

with open("HISTORY.rst") as history_file:
    HISTORY = history_file.read()

with open("requirements.txt") as dev_requirements_file:
    DEV_REQUIREMENTS = dev_requirements_file.readlines()


def _run_command(command):
    try:
        subprocess.check_call(command)

    except subprocess.CalledProcessError as error:
        print('Command failed with exit code', error.returncode)
        exit(error.returncode)


class Tests(TestCommand):
    description = 'run tests'
    user_options = []

    def run_tests(self):
        _run_command(TESTS_COMMAND)


class LintTests(TestCommand):
    description = 'run linters'
    user_options = []

    def run_tests(self):
        _run_command(FLAKE8_COMMAND)
        _run_command(BLACK_COMMAND)


class AllTests(TestCommand):
    description = 'run tests and linters'
    user_options = []

    def run_tests(self):
        _run_command(TESTS_COMMAND)
        _run_command(FLAKE8_COMMAND)
        _run_command(BLACK_COMMAND)


setup(
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Scientific/Engineering :: Atmospheric Science",
    ],
    description=DESCRIPTION,
    python_requires=REQUIRES_PYTHON,
    install_requires=REQUIREMENTS,
    license=LICENSE,
    long_description=README + "\n\n" + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=KEYWORDS,
    name=NAME,
    packages=find_packages(),
    cmdclass={
        'lint': LintTests,
        'test': Tests,
        'check': AllTests
    },
    extras_require={
        "docs": DOCS_REQUIREMENTS,
        "dev": REQUIREMENTS
    },
    url=URL,
    version=VERSION,
    zip_safe=False,
)
