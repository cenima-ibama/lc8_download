from click.testing import CliRunner

from os.path import exists, join
from os import remove, removedirs

from lc8_download.scripts.cli import cli


def test_cli_count():
    runner = CliRunner()
    scene = 'LC80030172015001LGN00'
    result = runner.invoke(cli, [scene, '-b', '11,BQA', '--path', 'tests/', '--metadata'])
    assert result.exit_code == 0

    filepath = join('tests', scene, scene + '_B11.TIF')
    assert exists(filepath)
    remove(filepath)

    filepath = join('tests', scene, scene + '_BQA.TIF')
    assert exists(filepath)
    remove(filepath)

    filepath = join('tests', scene, scene + '_MTL.txt')
    assert exists(filepath)
    remove(filepath)
    removedirs(join('tests', scene))
