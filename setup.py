from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in super_rides/__init__.py
from super_rides import __version__ as version

setup(
	name="super_rides",
	version=version,
	description="An app to manage vehicle renting",
	author="Arnold",
	author_email="arnoldsimony41@outlook.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
