from pytest import raises

from lc8_download.lc8 import Downloader
from lc8_download.lc8 import WrongSceneNameError, InvalidBandError
from lc8_download.lc8 import RemoteFileDoesntExist


def test_baseurl():
    scene = Downloader('LC80030172015001LGN00')
    assert scene.path == '003'
    assert scene.row == '017'


def test_scene_name_validation():

    with raises(WrongSceneNameError):
        Downloader('a')

    with raises(WrongSceneNameError):
        Downloader('LC80030172015001LGN0')

    with raises(WrongSceneNameError):
        Downloader('1230030172015001LGN00')

    with raises(WrongSceneNameError):
        Downloader('LC8003017201500HHH99')

    with raises(RemoteFileDoesntExist):
        Downloader('LC89990172015001LGN00')


def test_bands_validation():
    scene = Downloader('LC80030172015001LGN00')

    with raises(InvalidBandError):
        scene.download([12])

    with raises(InvalidBandError):
        scene.download([0])

    with raises(InvalidBandError):
        scene.download(['BAQ'])