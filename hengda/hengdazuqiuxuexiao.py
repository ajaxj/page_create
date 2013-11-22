# -*- coding:utf-8 -*-
import urllib2
from BeautifulSoup import BeautifulSoup
import gzip
from cStringIO import StringIO

class Henghazuqiuxuexiao:
    url_index = "http://we.sportscn.com/guangzhouhengda/index1.html?1"

    def readgzip(self,url):
        request = urllib2.Request(url)
        request.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(request)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
        else:
            data = response.read()
        return data


    def readpage260(self):
        _path =  r'%s/'%("e:/guangzhouhengda/xuexiao")
        try:
            html = self.readgzip(self.url_index)
            soup = BeautifulSoup(html)
            #取出文字列表
            ul = soup.find("ul",{'class':'ask'})
            li_list = ul.findAll("li")
            for li in li_list:
                _url = li.find("a").get("href")
                _filename = _url.split("viewnews-")[1]
                _html =  self.readgzip(_url)
                fileHandle = open(_path + _filename,"w")
                fileHandle.write(_html)
                fileHandle.close()

        except Exception,e:
            print e


if __name__ == '__main__':
    obj = Henghazuqiuxuexiao()
    obj.readpage260()
