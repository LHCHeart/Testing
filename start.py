import configparser, os
from bin import db, content, image


# 读取配置文件
conf = configparser.ConfigParser()
conf.read("./conf/test.conf",encoding='UTF-8')
LOG_FILE = conf.get("LOG", "LOG_FILE")

# f=open(LOG_FILE, "r+")
# f.truncate()

# con = content.get_content('28')
# db.insert_img(con, '28')

IMGS_CODE_START = 2751
IMGS_CODE_END = 10000
# for imgs in ('1578','1664','1811','1822'):
for imgs in range(IMGS_CODE_START,IMGS_CODE_END+1):
    IMGS_CODE = str(imgs)
    con = content.get_content(IMGS_CODE)
    db.insert_img(con,IMGS_CODE)
    IMG_CODE_SUM = int(con[3])+1
    for img in range(1,IMG_CODE_SUM):
        IMG_CODE = str(img)
        image.download_image(IMGS_CODE, IMG_CODE)

db.close()


