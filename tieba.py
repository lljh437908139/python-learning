import re
from urllib.request import urlopen


def getPage(url):
    response = urlopen(url)
    return response.read().decode('UTF-8')


def parsePage(s):
    ret = com.finditer(s)
    for i in ret:
        ret = {
            'title': i.group('title')
        }
        yield ret


def main(num):
    url = ('https://tieba.baidu.com/f?kw=%%E6%%8A%%97%%E5%%8E%%8B%%E8%%83%%8C%%E9%%94%%85&ie=utf-8&pn=%s') % num
    response_html = getPage(url)
    ret = parsePage(response_html)
    print(ret)
    f = open("beiguokangya", "a", encoding="utf8")
    for obj in ret:
        print(obj)
        data = str(obj)
        f.write(data + "\n")
    f.close()


com = re.compile('<div class="t_con cleafix">.*?" target="_blank" class="j_th_tit ">(?P<title>.*?)</a>', re.S)

count = 0
for i in range(10):
    main(count)  # count = 0
    count += 50
