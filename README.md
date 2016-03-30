# Azure ARM templates checker

[![Circle CI](https://circleci.com/gh/sebbrochet/azure-arm-checker.svg?style=svg)](https://circleci.com/gh/sebbrochet/azure-arm-checker)
[![Build Status](https://travis-ci.org/sebbrochet/azure-arm-checker.svg?branch=master)](https://travis-ci.org/sebbrochet/azure-arm-checker)

## Purpose
A quick and dirty tool to check if all parameters or variables used in the template have been defined.  

* Flag as *error* when a variable is used but not defined
* Flag as *error* when a parameter is used but not defined
* Flag as *warning* when a variable is defined but not used
* Flag as *warning* when a parameter is defined but not used

## Installation

* From source
  * `git clone https://github.com/sebbrochet/azure-arm-checker.git`
  * `cd azure-arm-checker`
  * `python setup.py install`

## Usage
```
usage: aa-checker [-h] template

Azure ARM template checker.

positional arguments:
  template    Template to check

optional arguments:
  -h, --help  show this help message and exit
```

## TODO
* Error management!
