import os,sys
from bin import db


def rename(name):
    newname = db.select_name(name)
    return newname


path = 'E:/Pictures/Rename/00001/'
old_names = os.listdir(path)
for old_name in old_names:
    new_name = rename(old_name)
    print(old_name)
    print(type(old_name))
    print(new_name)
    print(type(new_name))
    # o_name = path + old_name
    # n_name = path + new_name
    # rename(o_name,n_name)


def create_file(self,filename):
    """
    创建日志文件夹和日志文件
    :param filename:
    :return:
    """
    path = filename[0:filename.rfind("/")]
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename, mode="w", encoding="utf-8")
        fd.close()
    else:
        pass