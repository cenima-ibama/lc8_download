from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(name='lc8_download',
      version='0.0.1',
      description=u"Library to download Landsat 8 imagery from amazon servers",
      long_description=long_description,
      classifiers=[],
      keywords='',
      author=u"Wille Marcel",
      author_email='wille.marcel@hexgis.com',
      url='https://github.com/ibamacsr/lc8_download',
      license='GPLv3',
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
