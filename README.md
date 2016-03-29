# Azure ARM templates checker

## Purpose
A quick and dirty tool to check if all parameters or variables used in the template have been defined.  

* Flag as *error* when a variable is used but not defined
* Flag as *error* when a parameter is used but not defined
* Flag as *warning* when a variable is defined but not used
* Flag as *warning* when a parameter is defined but not used

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
