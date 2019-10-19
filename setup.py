import versioneer
from setuptools import find_packages, setup

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name='tivo',
    description='Python module for controlling a TiVo DVR',
    license='MIT',
    keywords='tivo',
    author='mattjgalloway, jed-frey',
    author_email='matt@galloway.me.uk',
    url='https://github.com/jed-frey/python-tivo',
    packages=find_packages()
)
