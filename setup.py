#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import re


version_raw = open('chest/_version.py').read()
version_regex = r"^__version__ = ['\"]([^'\"]*)['\"]"
version_result = re.search(version_regex, version_raw, re.M)
if version_result:
    version_string = version_result.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(name='chest',
      version=version_string,
      description='Simple on-disk dictionary',
      url='http://github.com/mrocklin/chest/',
      author='https://raw.github.com/mrocklin/chest/master/AUTHORS.md',
      maintainer='Matthew Rocklin',
      maintainer_email='mrocklin@gmail.com',
      license='BSD',
      keywords='dictionary out-of-core',
      install_requires=list(open('requirements.txt').read().strip()
                            .split('\n')),
      packages=['chest'],
      long_description=(open('README.rst').read() if exists('README.rst')
                        else ''),
      zip_safe=False)
