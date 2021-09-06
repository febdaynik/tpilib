from setuptools import setup
from io import open

version = "0.1.2"

long_description = "Python module for edu-tpi.donstu"

setup(
	name="tpilib",
	version=version,

	author="Feb",
	author_email="kmoloz@mail.ru",

	description = long_description,
	long_description=long_description,

	url = "https://github.com/febdaynik/tpilib",

	packages=["tpilib"],
	install_reqires=["requests"],
)

