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
      namespace_packages=['uvc'],
      include_package_data=True,
      zip_safe=False,
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      install_requires=[
          'uvclight',
          'grokcore.layout',
          'setuptools',
      ],
      entry_points={
      }
      )
