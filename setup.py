from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='lc8_download',
      version='0.1.5',
      description="Library to download Landsat 8 imagery from Amazon servers",
      long_description=long_description,
      classifiers=[
          'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.4',
          'Topic :: Scientific/Engineering :: GIS',
          'Topic :: Utilities',
      ],
      keywords=['landsat', 'satellite imagery', 'gis'],
      author="Wille Marcel",
      author_email='wille@wille.blog.br',
      url='https://github.com/ibamacsr/lc8_download',
      license='GPLv3+',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'click',
          'requests',
          'homura'
      ],
      extras_require={
          'test': ['pytest'],
      },
      entry_points="""
      [console_scripts]
      lc8_download=lc8_download.scripts.cli:cli
      """
      )
