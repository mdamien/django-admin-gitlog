# -*- coding: utf-8 -*-
import sys
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-admin-gitlog',
    version='0.1',
    description='Display a `git log` in your admin',
    long_description=README,
    url='http://github.com/mdamien/django-admin-gitlog',
    author='Damien MARIÉ',
    author_email='damien@dam.io',
    license='MIT',
    classifiers=(
        'Environment :: Web Environment',
        'Framework :: Django',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        # 'Programming Language :: Python :: 2', # TODO: verify python 2 compat
        'Programming Language :: Python :: 3',
    ),
    packages=find_packages(),
    include_package_data=True,
)
