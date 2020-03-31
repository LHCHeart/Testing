import os


# r+ :写入不清空,但会被替换，先read，再写入


def write(filename,content):
    wf = open(filename, 'w')
    wf.read()
    wf.write(content)
    wf.close()


def clean(filename):
    cf = open(filename, "r+")
    cf.truncate()
    cf.close()


def read(filename):
    rf = open(filename)
    num = len(rf.readlines())
    for i in range(num):
        rf.readline()
        print(rf)