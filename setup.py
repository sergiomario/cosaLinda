#!/usr/bin/env python
# encoding: utf-8

from setuptools import setup

try:
    with open('README.rst') as f:
        long_description = f.read()
except IOError:
    long_description = ''

setup(
    name='cosaLinda',
    version='127.0.0.1',
    url='https://github.com/sergiomario/cosaLinda',
    license='MIT',
    description=u'Tradução do módulo "this" do python para PT-BR-Manezes (Português brasileiro Florianopolitano)',
    long_description=long_description,
    author='Mário Sérgio',
    author_email='sergio.mario_q@hotmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['cosaLinda'],
    install_requires=['setuptools'],
)
