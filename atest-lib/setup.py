import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The list of requirements
requirements = (HERE / "requirements.txt").read_text(encoding="utf-8").split("\n")

setup(
    name="abstra",
    license="MIT",
    version="0.0.0",
    description="ALib",
    python_requires=">=3.8, <4",
    install_requires=requirements,
    packages=find_packages(exclude=["tests"]),
    long_description_content_type="text/markdown",
)
