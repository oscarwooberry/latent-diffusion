from setuptools import setup, find_packages

setup(
    name='ldm',
    version='0.0.1',
    description='',
    packages=["ldm"],
    install_requires=[
        'torch',
        'numpy',
        'tqdm',
    ],
)