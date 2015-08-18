from pytest import raises

from os.path import isfile, getsize, expanduser
from os import remove
from shutil import rmtree

from lc8_download.lc8 import SceneInfo, DownloaderBase, AmazonS3Downloader, GoogleDownloader, Downloader
from lc8_download.lc8 import WrongSceneNameError, InvalidBandError, DownloaderErrors
from lc8_download.lc8 import RemoteFileDoesntExist

def test_sceneInfo_validation():
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


def test_googleDownloader_name_validation():
    with raises(WrongSceneNameError):
        GoogleDownloader(SceneInfo('L882290692015208LGN01'))

    with raises(RemoteFileDoesntExist):
        GoogleDownloader(SceneInfo('LC82290695555208LGN01'))

    assert GoogleDownloader(SceneInfo('LT50010191998164PAC00'))

def test_amazonS3Downloader_name_validation():
    with raises(WrongSceneNameError):
        AmazonS3Downloader(SceneInfo('L882290692015208LGN01'))

    with raises(RemoteFileDoesntExist):
        AmazonS3Downloader(SceneInfo('LC89990172015001LGN00'))

    assert AmazonS3Downloader(SceneInfo('LC80030172015001LGN00'))

def  test_AmazonS3Downloader_bands_validation():
    donwloader = AmazonS3Downloader(SceneInfo('LC80030172015001LGN00'))
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

    download = scene.download([11], 'tests/')
    assert len(download) == 1
    assert isfile(download[0][0])
    assert getsize(download[0][0]) == download[0][1]
    rmtree('tests/LC80030172015001LGN00/')
