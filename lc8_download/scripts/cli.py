# Skeleton of a CLI

import click

from lc8_download.lc8_download import Downloader


@click.command('lc8_download')
@click.argument('scene', type=str, metavar='<scene>')
@click.option('-b', type=str)
@click.option('--metadata', is_flag=True)
def cli(scene, b, metadata):
    lc8 = Downloader(scene)
    bands = []
    for band in b.split(','):
        if band != 'BQA':
            band = int(band)
        bands.append(band)

    lc8.download(bands, metadata=metadata)
