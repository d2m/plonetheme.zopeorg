from setuptools import setup, find_packages
import os

version = '1.0-dev'

setup(name='plonetheme.zopeorg',
      version=version,
      description="zope.org Plone theme",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='Zope Foundation and Contributors',
      author_email='',
      url='http://svn.zope.org/plonetheme.zopeorg/trunk/',
      license='CC Attribution-NonCommercial-ShareALike license',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.Collage',
          'collective.collage.portlets',
          'collective.setuphandlertools',
          'archetypes.schemaextender',
          'collective.teaser',
      ],
      )
