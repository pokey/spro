#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'sigopt>=2.9.0',
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='spro',
    version='0.1.0',
    description="Optimize your espresso brewing.",
    long_description=readme + '\n\n' + history,
    author="Pokey Rule",
    author_email='pokey.rule@gmail.com',
    url='https://github.com/pokey/spro',
    packages=[
        'spro',
    ],
    package_dir={'spro':
                 'spro'},
    entry_points={
        'console_scripts': [
            'spro=spro.cli:cli'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='spro',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
