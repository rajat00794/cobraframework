from setuptools import setup
import os
import setuptools


setuptools.setup(
    name=os.getcwd().split("/")[-1],
    version="0.0.1",
    author="Rajat Mishra",
    author_email="author@example.com",
    description="A small example package",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.6",
)
