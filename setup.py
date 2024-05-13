from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='remlapreprocesspy',
    version='1.0.0',
    packages=find_packages(),
    install_requires=required_packages,
)
