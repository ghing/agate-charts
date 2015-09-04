#!/usr/bin/env python

from setuptools import setup
import sys

install_requires = [
    'six==1.6.1',
    'python-dateutil>=2.2'
]

if sys.version_info == (2, 6):
    install_requires.append('ordereddict>=1.1')

setup(
    name='way',
    version='0.1.0',
    description='way is an exploratory charting library built on the agate data analysis library.',
    long_description=open('README').read(),
    author='Christopher Groskopf',
    author_email='staringmonkey@gmail.com',
    url='http://way.readthedocs.org/',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'way'
    ],
    install_requires=install_requires
)
