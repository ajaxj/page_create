# -*- coding:utf-8 -*-
import os
import urllib2
from BeautifulSoup import BeautifulSoup
import gzip
from template import createpage_template,create_index_nav
from cStringIO import StringIO

class Hengda:
    #广州恒大
    url_253 = "http://we.sportscn.com/category-253.html"
    url_254 = "http://we.sportscn.com/category-254.html"
    url_255 = "http://we.sportscn.com/category-255.html"
    url_256 = "http://we.sportscn.com/category-256.html"
    url_257 = "http://we.sportscn.com/category-257.html"
    url_258 = "http://we.sportscn.com/category-258.html"
    url_index = "http://we.sportscn.com/guangzhouhengda/index1.html"


    path_253 = r'%s/'%("e:/guangzhouhengda/guangzhouhengda")
    path_news_253 = r'%s/'%("e:/guangzhouhengda/guangzhouhengda/news")

    path_254 = r'%s/'%("e:/guangzhouhengda/hengdayaguan")
    path_news_254 = r'%s/'%("e:/guangzhouhengda/hengdayaguan/news")

    path_255 = r'%s/'%("e:/guangzhouhengda/guangzhouhengdazuqiujulebu")
    path_news_255 = r'%s/'%("e:/guangzhouhengda/guangzhouhengdazuqiujulebu/news")

    path_256 = r'%s/'%("e:/guangzhouhengda/hengdashijubei")
    path_news_256 = r'%s/'%("e:/guangzhouhengda/hengdashijubei/news")

    path_257 = r'%s/'%("e:/guangzhouhengda/hengdashipin")
    path_news_257 = r'%s/'%("e:/guangzhouhengda/hengdashipin/news")

    path_258 = r'%s/'%("e:/guangzhouhengda/hengdazuqiu")
    path_news_258 = r'%s/'%("e:/guangzhouhengda/hengdazuqiu/news")

    path_index =  r'%s/'%("e:/guangzhouhengda")
    path_news =  r'%s/'%("e:/guangzhouhengda")

    #url_base = "http://we.sportscn.com/category-253.html"
    filename_253 = r'%s/%s'%("e:/guangzhouhengda/guangzhouhengda", "index.html" )
    filename_254 = r'%s/%s'%("e:/guangzhouhengda/254", "index.html" )
    filename_255 =  r'%s/%s'%("e:/guangzhouhengda/255", "index.html" )
    filename_256 =  r'%s/%s'%("e:/guangzhouhengda/256", "index.html" )
    filename_257 =  r'%s/%s'%("e:/guangzhouhengda/257", "index.html" )
    filename_258 =  r'%s/%s'%("e:/guangzhouhengda/258", "index.html" )


    #读取Gzip文件
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

    def tihuan(self,html):
        html = html.replace("viewnews-","guangzhouhengda/guangzhouhengda/news/")


    #生成新闻列表的文件,通过编号
    def createnews(self,id,html):
        if id =="253":
            _path = self.path_news
        elif id == "254":
            _path = self.path_news
        elif id == "255":
            _path = self.path_news
        elif id== "256":
            _path = self.path_news
        elif id== "257":
            _path = self.path_news
        elif id== "258":
            _path = self.path_news
        else:
            _path = self.path_news


        _html = html



        try:
            soup = BeautifulSoup(_html)
            #取出文字列表
            div_list = soup.findAll("div",{'class':'wdlx'})
            for div in div_list:
                _data_url =  div.find("a").get("href")
                _filename = _data_url.split("viewnews-")[1]
                _html =  self.readgzip(_data_url)
                fileHandle = open(_path + _filename,"w")
                fileHandle.write(_html)
                fileHandle.close()

            #取出图文列表
            div_list = soup.findAll("div",{'class':'wdls'})
            for div in div_list:
                _data_url =  div.find("a").get("href")
                _filename = _data_url.split("viewnews-")[1]
                _html =  self.readgzip(_data_url)
                fileHandle = open(_path + _filename,"w")
                fileHandle.write(_html)
                fileHandle.close()

        except Exception,e:
            print e



    #广州恒大 guangzhouhengda  253
    def readpage253(self):
        try:
            html = self.readgzip(self.url_253)
            soup = BeautifulSoup(html)
            div = soup.find("div",{'class':'pages'})
            a_list = div.findAll('a')
            if a_list[-1].text == u"下一页":
                pagecount =  int(a_list[-2].text.replace("...",""))
            else:
                pagecount = 1

            #
            nrank_div = soup.find("div",{"class":"nmr nrank"})
            zxgx_div = soup.findAll("div",{"class":"nmr zxgx"})[1]
            ktss_div = soup.find("div",{"class":"nmr twns ktss"})
            twns_div = soup.find("div",{"class":"nm twns"})
            divpage_list = soup.findAll("div",{'class':'pages'})
            for div in divpage_list:
                div.clear()
                _page_template = createpage_template(1,pagecount,253)
                p  = BeautifulSoup(_page_template)
                div.insert(1,p)


            nrank_div.clear()
            zxgx_div.clear()
            ktss_div.clear()
            twns_div.clear()


            self.createnews("253",html)      #  生成详细

            #处理首页连接地址

            fileHandle = open(self.path_253+"index.html","w")
            _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
            _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
            _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
            _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
            _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
            fileHandle.write(_html)
            fileHandle.close()

            for i in range(2,pagecount+1):
                url = "http://we.sportscn.com/category-253-page-" + str(i) + ".html"
                index_data = self.readgzip(url)
                self.createnews("253",index_data) #生成详细
                soup = BeautifulSoup(index_data)

                nrank_div = soup.find("div",{"class":"nmr nrank"})
                zxgx_div = soup.findAll("div",{"class":"nmr zxgx"})[1]
                ktss_div = soup.find("div",{"class":"nmr twns ktss"})
                twns_div = soup.find("div",{"class":"nm twns"})
                divpage_list = soup.findAll("div",{'class':'pages'})
                for div in divpage_list:
                    div.clear()
                    _page_template = createpage_template(i,pagecount,253)
                    p  = BeautifulSoup(_page_template)
                    div.insert(1,p)

                nrank_div.clear()
                zxgx_div.clear()
                ktss_div.clear()
                twns_div.clear()

                fileHandle = open(self.path_253+"index" + str(i)+".html","w")
                _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
                _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
                _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
                _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
                _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
                fileHandle.write(_html)
                fileHandle.close()
                print i

        except Exception,e:
            print e


    #恒大亚冠 hengdayaguan 254
    def readpage254(self):
        try:
            html = self.readgzip(self.url_254)
            soup = BeautifulSoup(html)
            div = soup.find("div",{'class':'pages'})
            a_list = div.findAll('a')
            if a_list[-1].text == u"下一页":
                pagecount = int(a_list[-2].text.replace("...",""))
            else:
                pagecount = 1

            nrank_div = soup.find("div",{"class":"nmr nrank"})
            zxgx_div = soup.find("div",{"class":"nmr zxgx"})
            ktss_div = soup.find("div",{"class":"nmr twns ktss"})
            twns_div = soup.find("div",{"class":"nm twns"})
            divpage_list = soup.findAll("div",{"class":"pages"})
            for div in divpage_list:
                div.clear()
                _page_template = createpage_template(1,pagecount,254)
                p = BeautifulSoup(_page_template)
                div.insert(1,p)

            nrank_div.clear()
            zxgx_div.clear()
            ktss_div.clear()
            twns_div.clear()

            self.createnews("254",html)      #  生成详细

            fileHandle = open(self.path_254+"index.html","w")
            _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
            _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
            _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
            _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
            _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
            fileHandle.write(_html)
            fileHandle.close()

            for i in range(2,pagecount+1):
                url = "http://we.sportscn.com/category-254-page-" + str(i) + ".html"
                index_data = self.readgzip(url)
                self.createnews("254",index_data) #生成详细
                soup = BeautifulSoup(index_data)

                nrank_div = soup.find("div",{"class":"nmr nrank"})
                zxgx_div = soup.find("div",{"class":"nmr zxgx"})
                ktss_div = soup.find("div",{"class":"nmr twns ktss"})
                twns_div = soup.find("div",{"class":"nm twns"})
                divpage_list = soup.findAll("div",{'class':'pages'})
                for div in divpage_list:
                    div.clear()
                    _page_template = createpage_template(i,pagecount,254)
                    p  = BeautifulSoup(_page_template)
                    div.insert(1,p)

                nrank_div.clear()
                zxgx_div.clear()
                ktss_div.clear()
                twns_div.clear()

                fileHandle = open(self.path_254+"index" + str(i)+".html","w")
                _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
                _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
                _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
                _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
                _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
                fileHandle.write(_html)
                fileHandle.close()
                print i

        except Exception,e:
            print e

    #广州恒大足球俱乐部 guangzhouhengdazuqiujulebu 255
    def readpage255(self):
        try:
            html = self.readgzip(self.url_255)
            soup = BeautifulSoup(html)
            div = soup.find("div",{'class':'pages'})
            if div == None:         #判断是否有分页,没有就只抓取第一页
                nrank_div = soup.find("div",{"class":"nmr nrank"})
                zxgx_div = soup.find("div",{"class":"nmr zxgx"})
                ktss_div = soup.find("div",{"class":"nmr twns ktss"})
                twns_div = soup.find("div",{"class":"nm twns"})
                nrank_div.clear()
                zxgx_div.clear()
                ktss_div.clear()
                twns_div.clear()

                fileHandle = open(self.path_255+"index.html","w")
                _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
                _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
                _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
                _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
                _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
                fileHandle.write(_html)
                fileHandle.close()
                #抓取首页详细
                self.createnews("255",html)

        except Exception,e:
            print e

    # 恒大世俱杯  hengdashijubei 256
    def readpage256(self):
        try:
            html = self.readgzip(self.url_256)
            soup = BeautifulSoup(html)
            div = soup.find("div",{'class':'pages'})
            if div == None:
                nrank_div = soup.find("div",{"class":"nmr nrank"})
                zxgx_div = soup.find("div",{"class":"nmr zxgx"})
                ktss_div = soup.find("div",{"class":"nmr twns ktss"})
                twns_div = soup.find("div",{"class":"nm twns"})
                nrank_div.clear()
                zxgx_div.clear()
                ktss_div.clear()
                twns_div.clear()
                fileHandle = open(self.path_256+"index.html","w")
                _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
                _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
                _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
                _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
                _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
                fileHandle.write(_html)
                fileHandle.close()
                #抓取首页详细
                self.createnews("256",html)
        except Exception,e:
            print e


    #恒大视频  hengdashipin 257
    def readpage257(self):
        try:
            html = self.readgzip(self.url_257)
            soup = BeautifulSoup(html)
            div = soup.find("div",{'class':'pages'})
            if div == None:
                nrank_div = soup.find("div",{"class":"nmr nrank"})
                zxgx_div = soup.find("div",{"class":"nmr zxgx"})
                ktss_div = soup.find("div",{"class":"nmr twns ktss"})
                twns_div = soup.find("div",{"class":"nm twns"})
                nrank_div.clear()
                zxgx_div.clear()
                ktss_div.clear()
                twns_div.clear()
                fileHandle = open(self.path_257+"index.html","w")
                _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
                _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
                _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
                _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
                _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
                fileHandle.write(_html)
                fileHandle.close()
                #抓取首页详细
                self.createnews("257",html)
        except Exception,e:
            print e


    #恒大足球  hengdazuqiu 258
    def readpage258(self):
        try:
            html = self.readgzip(self.url_258)
            soup = BeautifulSoup(html)
            div = soup.find("div",{'class':'pages'})
            a_list = div.findAll('a')
            if a_list[-1].text == u"下一页":
                pagecount =  int(a_list[-2].text.replace("...",""))
            else:
                pagecount = 1

            nrank_div = soup.find("div",{"class":"nmr nrank"})
            zxgx_div = soup.find("div",{"class":"nmr zxgx"})
            ktss_div = soup.find("div",{"class":"nmr twns ktss"})
            twns_div = soup.find("div",{"class":"nm twns"})
            divpage_list = soup.findAll("div",{'class':'pages'})
            for div in divpage_list:
                div.clear()
                _page_template = createpage_template(1,pagecount,258)
                p  = BeautifulSoup(_page_template)
                div.insert(1,p)

            nrank_div.clear()
            zxgx_div.clear()
            ktss_div.clear()
            twns_div.clear()
            self.createnews("258",html)      #  生成详细

            #处理首页连接地址

            fileHandle = open(self.path_258+"index.html","w")
            _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
            _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
            _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
            _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
            _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
            fileHandle.write(_html)
            fileHandle.close()

            for i in range(2,pagecount+1):
                url = "http://we.sportscn.com/category-258-page-" + str(i) + ".html"
                index_data = self.readgzip(url)
                self.createnews("258",index_data) #生成详细
                soup = BeautifulSoup(index_data)
                nrank_div = soup.find("div",{"class":"nmr nrank"})
                zxgx_div = soup.find("div",{"class":"nmr zxgx"})
                ktss_div = soup.find("div",{"class":"nmr twns ktss"})
                twns_div = soup.find("div",{"class":"nm twns"})
                divpage_list = soup.findAll("div",{'class':'pages'})
                for div in divpage_list:
                    div.clear()
                    _page_template = createpage_template(i,pagecount,258)
                    p  = BeautifulSoup(_page_template)
                    div.insert(1,p)

                nrank_div.clear()
                zxgx_div.clear()
                ktss_div.clear()
                twns_div.clear()
                fileHandle = open(self.path_258+"index" + str(i)+".html","w")
                _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
                _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
                _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
                _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
                _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
                _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
                fileHandle.write(_html)
                fileHandle.close()
                print i

        except Exception,e:
            print e

    #生成首页
    def readpageindex(self):
        try:
            html = self.readgzip(self.url_index)
            soup = BeautifulSoup(html)
            ul =  soup.find("ul",{'class':'nav'})

            ul.clear()
            _nav_temp = create_index_nav()
            nav_temp = BeautifulSoup(_nav_temp)
            ul.insert(1,nav_temp)



            fileHandle = open(self.path_index+"index.html","w")
            _html = soup.prettify().replace("http://we.sportscn.com/viewnews-","http://we.sportscn.com/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-253.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengda/")
            _html = _html.replace("http://we.sportscn.com/category-254.html","http://we.sportscn.com/guangzhouhengda/hengdayaguan/")
            _html = _html.replace("http://we.sportscn.com/category-255.html","http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/")
            _html = _html.replace("http://we.sportscn.com/category-256.html","http://we.sportscn.com/guangzhouhengda/hengdashijubei/")
            _html = _html.replace("http://we.sportscn.com/category-257.html","http://we.sportscn.com/guangzhouhengda/hengdashipin/")
            _html = _html.replace("http://we.sportscn.com/category-258.html","http://we.sportscn.com/guangzhouhengda/hengdazuqiu/")
            fileHandle.write(_html)
            fileHandle.close()

        except Exception,e:
            print e




if __name__ == "__main__":
    hd = Hengda()
    hd.readpageindex()
    #hd.readpage253()
    #hd.readpage254()
    hd.readpage255()
    hd.readpage256()
    hd.readpage257()
    hd.readpage258()