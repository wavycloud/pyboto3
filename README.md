# pyboto3
Pythonic Interface for AWS boto3 that gives you autocomplete on all AWS services

This package will minimize the time you have to look for AWS documentation online. You shouldn't leave your coding environment.

# usage

python setup.py install

>>> from pyboto3 import S3

enjoy autocomplete and navigate to class to read documentation from S3 class code

# Contributing

We need your help! The code needs work and testing to make it friendly with python 3 and other systems. Feel free to test, commit and push changes!

## Testing

Currently the test is what generates the code from online documentation https://boto3.readthedocs.io/en/latest/reference/services/index.html
Currently testing is limited to the generation of the code, not the code functionality.

# Issues
The package have not been tested. Only code generation is tested. currently the generation is only tested on Windows 10 Python 2.7

# Todo
* This package have not been tested against AWS API, yet.
* Test code on Linux, Mac
* Test code on Python 3
