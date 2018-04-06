import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="{{ cookiecutter.python_module_name }}",
    description="{{ cookiecutter.description }}",
    author="{{ cookiecutter.author_name }}",
    packages=find_packages(exclude=['data', 'figures', 'output', 'notebooks']),
    long_description=read('README.md'),
)
