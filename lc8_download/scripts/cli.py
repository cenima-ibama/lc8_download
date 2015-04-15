import click

from lc8_download.lc8 import Downloader


@click.command('lc8_download')
@click.argument('scene', type=str, metavar='<scene>')
@click.option('-b', type=str, help="""Bands to be downloaded. Use commas as
    delimiter. Example: '-b 2,3,4,BQA'""")
@click.option('--all', is_flag=True, help="Download all bands and metadata")
@click.option('path', '--path', default=None,
    type=click.Path(file_okay=False, writable=True),
    help="Directory where the files will be saved. Default: ~/landsat/")
@click.option('--metadata', is_flag=True, help="Download scene metadata file.")
def cli(scene, b, path, metadata, all):
    lc8 = Downloader(scene)

    if all:
        bands = list(range(1, 12)) + ['BQA']
        metadata = True
    else:
        bands = []
        for band in b.split(','):
            if band != 'BQA':
                band = int(band)
            bands.append(band)

    lc8.download(bands, path, metadata)
