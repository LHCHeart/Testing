import re
import configparser
from bs4 import BeautifulSoup
from bin import log
from urllib.request import urlopen
import urllib.error


conf = configparser.ConfigParser()
conf.read("./conf/test.conf", encoding='UTF-8')

IMGS_URL = conf.get('IMG', 'IMGS_URL')


def get_content(IMGS_CODE):
    url = IMGS_URL + str(IMGS_CODE) + '.html'
    #print(url)
    try:
        html_content = urlopen(url).read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            log.write_error(e.code)
        if hasattr(e, "reason"):
            log.write_error(e.reason)
        con_error = ['-','-','-','-','-','-','-','-']
        return con_error

    soup = BeautifulSoup(html_content, 'html.parser')
    try:
        title = str(soup.title)
    except:
        title = "<title>----</title>"

    text = soup.text
    try:
        con01 = re.search("发行机构.*", text).group()
    except:
        con01 = "发行机构：----"
    try:
        con02 = re.search("期刊编号.*图片数量", text).group()
    except:
        con02 = "期刊编号：----图片数量"
    con03 = re.search("图片数量.*", text).group()
    try:
        con04 = re.search("分 辨 率.*", text).group()
    except:
        con04 = "分 辨 率：----"
    con05 = re.search("模特姓名.*", text).group()
    try:
        con06 = re.search("发行时间.*", text).group()
    except:
        con06 = "发行时间：----"
    try:
        con07 = re.search("补充说明.*", text).group()
    except:
        con07 = "补充说明：----"
    con = [title[7:-8],con01[6:],con02[6:-4],con03[6:-2],con04[7:],con05[6:],con06[6:],con07[6:]]
    #print(con)
    return con


    # titles = re.search("<title>.*</title>", html).group()
    # title = titles[7:-8]
    # orgs = re.search("<p>发行机构.*?</p>", html).group()
    # org = orgs[3:-4]
    # vols = re.search("<p>期刊编号.*?</p>", html).group()
    # vol = vols[3:-4]
    # content = {'Title': title,'Vol': vol, 'Org':org}
