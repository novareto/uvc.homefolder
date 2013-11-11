# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

version = '1.0'


setup(name='uvc.homefolder',
      version=version,
      description="Homefolder for UVCSite's members",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Christian Klinger',
      author_email='cklinger@novareto.de',
      url='http://www.novareto.de',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'grok',
          'grokcore.layout',
          'setuptools',
      ],
      entry_points={
      }
      )
