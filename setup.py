#!/usr/bin/env python3
from setuptools import setup

package_name = 'pl_nouns'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/data', ['data/rzecz_pol_compact.txt']),
        # You can include additional data files here as needed
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='TODO',
    maintainer_email='5305@pw.edu.pl',
    description='The pl_nouns package',
    license='TODO', # Update the license as appropriate
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Here you can add your Python executables
            # For example: 'executable_name = package_name.module_name:main'
        ],
    },
)