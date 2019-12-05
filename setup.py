#!/usr/bin/env python

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['pl_nouns'],
    package_dir={'': 'src'},
    package_data={'': ['data/rzecz_pol_compact.txt']}
)

setup(**setup_args)