# pyboto3 interface stubs
Pythonic Interface for AWS boto3 that gives you autocomplete on all AWS services

The code is not to be imported. you can only use it as a typehint for autocomplete in pycharm.

This package will minimize the time you have to look for AWS documentation online. You shouldn't leave your coding environment.

# Screenshots
## Ctrl+Space

![Ctrl+Space Autocomplete Image](https://github.com/gehadshaat/pyboto3/blob/master/img/autocomplete.png)

## Ctrl+Q

![Ctrl+Q Documentation](https://github.com/gehadshaat/pyboto3/blob/master/img/documentation.png)

# Installation
```
pip install pyboto3
```

# Usage
```python
import boto3
s3 = boto3.client('s3')
""" :type : pyboto3.s3 """
# s3. -> will give you autocomplete for s3 methods in pycharm
```
enjoy autocomplete and navigate to class to read documentation from S3 class code

# Update services to latest version
* Clone repo
* Install virtual environment 
```
cd <repo source>
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
* Run boto3_interface_generator
```
cd pyboto3
python boto3_interface_generator.py
```
* Add new & modified files to git 
# Release Instructions
```
python setup.py sdist
twine upload dist/*
```

# Contributing

We need your help! The code needs work and testing to make it friendly with python 3 and other systems. Feel free to test, commit and push changes!

# Issues
The package have been tested on Python 2.7 only


