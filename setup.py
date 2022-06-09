from setuptools import setup

setup(
    name='disentpy',
    version='0.0.1',
    description='Disent API caller',
    url='git@github.com:rfschubert/ptolemaios-sdk-package.git',
    author='Niels lauritzen',
    author_email='niels.lauritzen@disent.com',
    license='unlicense',
    packages=['disent'],
    install_requires=['requests'],
    zip_safe=False
)