from setuptools import setup, find_packages
from erpnext.__version__ import __version__
import os

with open("requirements.txt", "r") as f:
	install_requires = f.readlines()

setup(
    name='erpnext',
    version=__version__,
    description='Open Source ERP',
    author='Web Notes Technologies',
    author_email='info@erpnext.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=install_requires
)
