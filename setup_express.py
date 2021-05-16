#!/usr/bin/env python

from __future__ import print_function
from setuptools import setup, find_packages
from glob import glob
# import guang as my_package
class my_package:
    pass


my_package.__name__ = 'manim_express'
my_package.__version__ = 0

with open(glob('requirements_express.txt')[0], encoding='utf-8') as f:
    all_reqs = f.read().split('\n')
install_requires = [x.strip() for x in all_reqs]

with open("README.md", "r", encoding='utf-8') as fr:
    long_description = fr.read()

setup(name=my_package.__name__,
      version=my_package.__version__,
      package_data={
          'mainm_express': [
              'version_config.yaml', 'Utils/date_data',
              'Voice/pinyin_to_phone.txt'
          ],
      },
      description=" ML/DL tools function library",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="K.y",
      author_email="beidongjiedeguang@gmail.com",
      url="https://github.com/beidongjiedeguang/mainm_express",
      license="MIT",
      install_requires=install_requires,
      classifiers=[
          'Operating System :: OS Independent',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Artificial Intelligence',
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
      ],
      keywords=[
          'Deep Learning', 'Machine Learning', 'Neural Networks',
          'Natural Language Processing', 'Computer Vision'
      ],

      packages=find_packages())

# setup(
#     setup_requires=['pbr'],
#     pbr=True,
# )
