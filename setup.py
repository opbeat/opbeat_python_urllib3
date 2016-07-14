#!/usr/bin/env python
"""
opbeat
======

opbeat is a Python client for `Opbeat <https://opbeat.com/>`_. It provides
full out-of-the-box support for many of the popular frameworks, including
`Django <djangoproject.com>`_, `Flask <http://flask.pocoo.org/>`_, and `Pylons
<http://www.pylonsproject.org/>`_. opbeat also includes drop-in support for any
`WSGI <http://wsgi.readthedocs.org/>`_-compatible web application.
"""

# Hack to prevent stupid "TypeError: 'NoneType' object is not callable" error
# in multiprocessing/util.py _exit_function when running `python
# setup.py test` (see
# http://www.eby-sarna.com/pipermail/peak/2010-May/003357.html)
for m in ('multiprocessing', 'billiard'):
    try:
        __import__(m)
    except ImportError:
        pass

import sys
import os

from setuptools import setup, find_packages, Extension
from setuptools.command.test import test as TestCommand

VERSION = '1.1'


tests_require = [
    'py>=1.4.26',
    'pytest>=2.6.4',
    'pytest-capturelog>=0.7',
    'mock',
    'urllib3-mock',
]


install_requires = [
    'certifi',
    'opbeat>=3.1.4',
    'urllib3',
]

try:
    # For Python >= 2.6
    import json
except ImportError:
    install_requires.append("simplejson>=2.3.0,<2.5.0")


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='opbeat_python_urllib3',
    version=VERSION,
    author='Opbeat, Inc',
    author_email='support@opbeat.com',
    url='https://github.com/opbeat/opbeat_python_urllib3',
    description='An urllib3 transport for Opbeat',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    packages=find_packages(exclude=("tests",)),
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={'tests': tests_require},
    cmdclass={'test': PyTest},
    test_suite='tests',
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
