from setuptools import setup

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='cbpi4-PCF8574-GPIO',
      version='0.0.1',
      description='CraftBeerPi Plugin',
      author='',
      author_email='',
      url='',
      include_package_data=True,
      package_data={
        # If any package contains *.txt or *.rst files, include them:
      '': ['*.txt', '*.rst', '*.yaml'],
      'cbpi4-PCF8574-GPIO': ['*','*.txt', '*.rst', '*.yaml']},
      packages=['cbpi4-PCF8574-GPIO'],
      install_requires=[
      'cbpi>=4.0.0.33',
      'smbus2',
      'pcf8574-io'
      ],
      long_description=long_description,
      long_description_content_type='text/markdown'
     )