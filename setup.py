from setuptools import setup
from __init__ import __version__


setup(name='lscolumns',
      version=__version__,
      description='pretty-print columns of data',
      author='Ben Morris',
      author_email='ben@bendmorris.com',
      url='https://github.com/bendmorris/lscolumns',
      packages=['lscolumns'],
      package_dir={
                   'lscolumns':''
                   },
      )
