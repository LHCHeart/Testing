import configparser
import os
from urllib.request import urlretrieve
from bin import log

# 读取配置文件
conf = configparser.ConfigParser()
conf.read("./conf/test.conf", encoding='UTF-8')

IMG_PATH = conf.get('IMG', 'IMG_PATH')
IMG_URL = conf.get('IMG', 'IMG_URL')


def download_image(IMGS_CODE, IMG_CODE):
    img_url = str(IMG_URL + IMGS_CODE + '/' + IMG_CODE + '.jpg')
    imgs_dir = str(IMG_PATH + IMGS_CODE+ '/')
    img_name = str(imgs_dir + IMG_CODE + '.jpg')
    os.makedirs(imgs_dir, exist_ok=True)
    try:
        urlretrieve(img_url, img_name)
        log.write_debug(img_url + " 下载成功")
        log.write_debug('文件下载路径：' + img_name)
    except:
        log.write_error(img_url + " 下载失败")
