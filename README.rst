lc8_download
============

Utility to download Landsat 8 imagery from Amazon servers.

It's quite similar to `landsat-util <https://github.com/developmentseed/landsat-util>`_,
but if you just need to download imagery and need the BQA band and metadata information,
it can fit better for you.

Installation
============

    pip install lc8_download

Usage
=====

You can use lc8_download command line interface or use it as a Python
library.

Command line interface
----------------------

    Usage: lc8_download [OPTIONS] <scene>

Options:

    -b                Bands to be downloaded. Use commas as delimiter. Example: '-b 2,3,4,BQA'
    --all             Download all bands and metadata
    --path            Directory where the files will be saved. Default: ~/landsat/
    --metadata        Download scene metadata file.
    --help            Show this message and exit.

For example:

    lc8_download LC80030172015001LGN00 -b 2,3,4,BQA --metadata --path lc8/

Download the bands 2, 3, 4 and BQA of the scene ``LC80030172015001LGN00``.
Also download the metadata file and save all the files in the folder ``lc8``.


Python Library
--------------

    >>> from lc8_download import lc8
    >>> scene = lc8.Downloader('LC80030172015001LGN00')
    >>> scene.download([2, 3, 4, 'BQA'], 'lc8/', True)

It will download the bands 2, 3, 4 and BQA and the metadata of the scene
``LC80030172015001LGN00`` and save all the files in the folder ``lc8``.

License
=======

GPLv3
