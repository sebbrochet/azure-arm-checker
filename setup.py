#!/usr/bin/env python

import os
import sys

from distutils.core import setup

setup(name='aa-checker',
      version="0.0.1",
      description='A quick and dirty tool to check if all parameters or variables used in an Azure ARM template have been defined',
      long_description='This command-line tool lets you check your Azure ARM templates for some basic errors/warnings before deploying them on Azure',
      author="sebbrochet",
      author_email='contact@sebbrochet.com',
      url='https://github.com/sebbrochet/azure-arm-checker',
      platforms=['linux'],
      license='MIT License',
      scripts=['bin/aa-checker'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python',
          'Topic :: Software Development :: Quality Assurance',
          ],
      )
