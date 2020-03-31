from urllib.request import urlretrieve
from bin import log
import configparser,os

conf = configparser.ConfigParser()
conf.read("./conf/test.conf", encoding='UTF-8')

IMG_PATH = conf.get('IMG', 'IMG_PATH')
IMG_URL = conf.get('IMG', 'IMG_URL')
IMGS_CODE = '3'
IMG_CODE = '1'
img_url = str(IMG_URL + IMGS_CODE + '/' + IMG_CODE + '.jpg')
imgs_dir = str(IMG_PATH + IMGS_CODE + '/')
os.makedirs(imgs_dir, exist_ok=True)

imgs_name = str(IMG_PATH + IMGS_CODE + '/' + IMG_CODE + '.jpg')
# img_url = "https://mtl.gzhuibei.com/images/img/3/1.jpg"
# imgs_dir = "D:/image/"

try:
    urlretrieve(img_url, imgs_name)
except IOError as e:
    log.write_error(e)
    log.write_error(img_url + " 1下载失败")
else:
    log.write_debug(img_url + " 下载成功")
    log.write_debug('下载路径' + imgs_dir)