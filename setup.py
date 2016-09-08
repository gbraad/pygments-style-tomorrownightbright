#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '0.2'
long_description = '\n'.join([
    open('README.rst').read(),
    ])

classifiers = [
    'Development Status :: 4 - Beta',
    'Environment :: Plugins',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setup(
    name='pygments-style-tomorrownightbright',
    version=version,
    description='Pygments version of the Tomorrow (night bright) theme.',
    long_description=long_description,
    classifiers=classifiers,
    keywords=['pygments', 'style', 'tomorrow', 'syntax highlighting'],
    author='Gerard Braad',
    author_email='me@gbraad.nl',
    url='https://github.com/gbraad/pygments-style-tomorrownightbright',
    license='MIT',
    packages=find_packages(),
    install_requires=['pygments >= 1.5'],
    entry_points="""
        [pygments.styles]
        tomorrownightbright=pygments_style_tomorrownightbright:TomorrowNightBrightStyle
    """,
    zip_safe=False,
)
