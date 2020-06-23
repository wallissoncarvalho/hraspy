from setuptools import setup, find_packages
from versioneer import find_version

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='hraspy',
    description='Powerful controller to edit, perform and visualize outputs toward HEC-RAS model simulations',
    version=find_version('hraspy','__init__.py'),
    keywords='hec-ras floods calibration hydrodynamic',
    author='Wallisson Moreira de Carvalho',
    author_email='cmwallisson@gmail.com',
    license='BSD 3-Clause License',
    packages=find_packages(),
    classifiers=['Development Status :: 1 - Planning',
                 'Environment :: Console',
                 'Operating System :: OS Independent',
                 'Intended Audience :: Science/Research',
                 "Programming Language :: Python :: 3.6",
                 "Programming Language :: Python :: 3.7",
                 "Topic :: Scientific/Engineering",
                 ],
)
