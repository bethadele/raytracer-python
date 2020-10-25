# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='Ray Tracer Python',
    version='0.1.0',
    description='Python implementation of Ray Tracer Challenge',
    long_description=readme,
    author='Beth Adele Long',
    author_email='irongoddess@gmail.com',
    url='https://github.com/bethadele/raytracer_python',
    # packages=find_packages(exclude=('tests', 'docs'))
    packages=['raytracer',],
)
