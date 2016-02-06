#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://github.com/rubenhortas
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@status:    Developing
@version:   alpha
@file:      setup.py
"""

from setuptools import setup

setup(name='pdfMetadata',
      version='1.0',
      description='Reads metadata from pdf files.',
      author='Ruben Hortas Astariz',
      author_email='rubenhortas at gmail.com',
      url='https://github.com/rubenhortas/pdfmetadata',
      install_requires=['PyPDF2'],
      dependency_links=['https://github.com/rubenhortas/pyCLI_Colors'],
      packages=[],
      )
