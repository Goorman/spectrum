#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
  name = "spectrum",
  version = "0.1",
  packages = find_packages(),
  install_requires = ['numpy>=1.8', 'scipy>0.13.3', 'matplotlib>1.3.1'],

  # metadata for upload to PyPI
  author = "ixaxaar",
  author_email = "root@ixaxaar.in",
  description = "Higher Order Spectrum Estimation toolkit",
  license = "MIT",
  keywords = "Higher Order Spectrum Estimation toolkit",
  url = "https://github.com/synergetics/spectrum",
)
