import os
from setuptools import setup
import setuptools
# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
setup(
    name = os.getcwd().split("/")[-1],
    version = "0.0.4",
    author = "Rajat Mishra",
    author_email = "andrewjcarter@gmail.com",
    description = ("An demonstration of how to create, document, and publish "
                                   "to the cheese shop a5 pypi.org."),
    license = "BSD",
    keywords = "efe",
    url = "http://packages.python.org/an_example_pypi_project",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
)
