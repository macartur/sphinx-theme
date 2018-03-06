#!/usr/bin/env python
import codecs
from setuptools import setup

# Base requirements
with open('requirements/base.txt') as f:
    install_reqs = [line for line in f.read().split('\n') if line]

# README into long description
with codecs.open('README.rst', encoding='utf-8') as f:
    readme = f.read()

setup(
    name='kytos_sphinx_theme',
    version='0.0.1',
    description=' Kytos Sphinx Theme',
    long_description=readme,
    install_requires=install_reqs,
    packages=['kytos_sphinx_theme'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'kytos = kytos_sphinx_theme'
        ]
    },
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
