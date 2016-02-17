from pytest import raises

from os.path import isfile, getsize
from shutil import rmtree

from lc8_download.lc8 import SceneInfo, DownloaderBase, AWSDownloader
from lc8_download.lc8 import GoogleDownloader, Downloader
from lc8_download.lc8 import WrongSceneNameError, InvalidBandError, DownloaderErrors
from lc8_download.lc8 import RemoteFileDoesntExist


def test_SceneInfo_validation():
    with raises(WrongSceneNameError):
        SceneInfo('a')

    with raises(WrongSceneNameError):
        SceneInfo('LC80030172015001LGN0')

    scene = SceneInfo('LC80030172015001LGN00')
    assert scene.path == '003'
    assert scene.row == '017'


def test_DownloaderBase_sceneInfoType():
    with raises(TypeError):
        DownloaderBase('LC80030172015001LGN00')

    download = DownloaderBase(SceneInfo('LC80030172015001LGN00'))
    assert type(download) is DownloaderBase


def test_GoogleDownloader_name_validation():
    with raises(WrongSceneNameError):
        GoogleDownloader(SceneInfo('L882290692015208LGN01'))

    with raises(RemoteFileDoesntExist):
        GoogleDownloader(SceneInfo('LC82290695555208LGN01'))

    assert GoogleDownloader(SceneInfo('LT50010191998164PAC00'))

def test_GoogleDownloader_bands_validation():
    base_path = 'tests/'
    downloader = GoogleDownloader(SceneInfo('LC82290692016035LGN00'))
    downloaded = downloader.download([10], base_path)
    assert len(downloaded) == 1
    assert downloaded[0][0] == '%sLC82290692016035LGN00/LC82290692016035LGN00_B10.TIF' % base_path
    remove(downloaded[0][0])

def test_AWSDownloader_name_validation():
    with raises(WrongSceneNameError):
        AWSDownloader(SceneInfo('L882290692015208LGN01'))

    with raises(RemoteFileDoesntExist):
        AWSDownloader(SceneInfo('LC89990172015001LGN00'))

    assert AWSDownloader(SceneInfo('LC80030172015001LGN00'))


def  test_AWSDownloader_bands_validation():
    donwloader = AWSDownloader(SceneInfo('LC80030172015001LGN00'))
    with raises(TypeError):
        donwloader.download(12)

    with raises(InvalidBandError):
        donwloader.download([12])

    with raises(InvalidBandError):
        donwloader.download([0])

    with raises(InvalidBandError):
        donwloader.download(['BAQ'])


def test_scene_name_validation():

    with raises(WrongSceneNameError):
        Downloader('a')

    with raises(WrongSceneNameError):
        Downloader('LC80030172015001LGN0')

    with raises(DownloaderErrors):
        Downloader('1230030172015001LGN00')

    with raises(DownloaderErrors):
        Downloader('LC89990172015001LGN00')

    Downloader('LC82290692015208LGN01')
    Downloader('LT50010191998164PAC00')
    Downloader('LE70490702013069SG100')


def test_bands_validation():
    scene = Downloader('LC80030172015001LGN00')

    with raises(InvalidBandError):
        scene.download([12])

    with raises(InvalidBandError):
        scene.download([0])

    with raises(InvalidBandError):
        scene.download(['BAQ'])

    download = scene.download([10], 'tests/')
    assert len(download) == 1
    assert isfile(download[0][0])
    assert getsize(download[0][0]) == download[0][1]
    assert 'tests/LC80030172015001LGN00/LC80030172015001LGN00_B10.TIF' == download[0][0]
    rmtree('tests/LC80030172015001LGN00/')
