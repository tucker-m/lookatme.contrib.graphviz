"""
Setup for lookatme.contrib.graphviz
"""


from setuptools import setup, find_namespace_packages
import os


setup(
    name="lookatme.contrib.graphviz",
    version="0.0.1-rc1",
    description="Renders ASCII art of Graphviz Dot graphs",
    author="Tucker McKnight",
    author_email="",
    python_requires=">=3.5",
    packages=find_namespace_packages(include=["lookatme.*"]),
)
