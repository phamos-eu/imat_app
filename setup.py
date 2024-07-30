from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in imat_app/__init__.py
from imat_app import __version__ as version

setup(
	name="imat_app",
	version=version,
	description="test",
	author="furqan@gmail.com",
	author_email="furqan@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
