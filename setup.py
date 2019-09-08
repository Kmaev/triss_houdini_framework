import os
import re
from setuptools import setup, find_packages

root = os.path.dirname(__file__)
init = os.path.join(root, 'src', 'triss', '__init__.py')

with open(init, 'r') as f:
    version = re.match(r'__version__ = \'([\d\.]+)\'', f.read()).group(1)

setup(
    name='triss',
    version=version,
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
