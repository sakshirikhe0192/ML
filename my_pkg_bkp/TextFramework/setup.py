from distutils.core import setup 
from setuptools import find_packages
print(find_packages())
setup(
    name='my_pkg',
    version='1.1',
    pkg=find_packages(),
)