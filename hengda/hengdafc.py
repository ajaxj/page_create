# -*- coding:gb2312 -*-
import cookielib
import os
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

class Hengdafc:
    url_fc = "http://www.gzevergrandefc.com/news.aspx"

    def readtohtml(self):
        req = urllib2.Request(self.url_fc)
        res = urllib2.urlopen(req)
        htmlstr =  res.read();
        soup = BeautifulSoup(htmlstr)
        div_sahishi_main = soup.find("div",{'class':'sahishi_main'})
        return div_sahishi_main.prettify()

    #亚冠
    def getText173(self):
        posturl = "http://www.gzevergrandefc.com/ajax/handler.ashx"
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.1.2) Gecko/20090803 Fedora/3.5.2-2.fc11 Firefox/3.5.2'}
        postData = {'action' : 'bang','from':'other','id':'173','nocache' : '0.6874064390080088'}
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl,postData,headers)
        response = urllib2.urlopen(request,timeout=40)
        text = response.read().replace("{$race$}","")
        return text

    def template173(self,txtone,txttwo):
        _html = "<div class=\"nrank mt10\">"
        _html += "<div class=\"fm\"><b>亚冠</b> <a name=\"M1\" style=\"LEFT: 174px\" class=\"Off\" id=\"M1\" onmouseover=\"MM(0,'M1','B1','');\">赛程表</a> <a name=\"M1\" style=\"LEFT: 244px\" class=\"On\" id=\"M1\" onmouseover=\"MM(1,'M1','B1','');\">射手榜</a> </div>"
        _html += "<div class=\"fm_b2\">"
        _html += "<ul name=\"B1\" class=\"Bang\" id=\"B1\" style=\"\">"
        _html += "<div style=\"DISPLAY: block\" class=\"Banglist\">"
        _html += txtone
        _html +="</div>"
        _html +="</ul>"
        _html +="<ul name=\"B1\" style=\"display:none\" class=\"Bang\" id=\"B1\">"
        _html +="<div jquery17205382323661072996=\"11\" style=\"DISPLAY: block\" class=\"Banglist\">"
        _html += txttwo
        _html +="</div>"
        _html +="</ul>"
        _html +="</div>"
        _html +="</div>"
        return _html

    #中超


    def template170(self,txtone,txttwo):
        _html = "<div class=\"nrank mt10\">"
        _html +="<div class=\"fm\"><b>中超</b> <a name=\"M2\" style=\"LEFT: 174px\" class=\"On\" id=\"M2\" onmouseover=\"MM(0,'M2','B2','');\">积分榜</a> <a name=\"M2\" style=\"LEFT: 244px\" class=\"Off\" id=\"M2\" onmouseover=\"MM(1,'M2','B2','');\">射手榜</a> </div>"
        _html +="<div class=\"fm_b2\">"
        _html +="<ul name=\"B2\" class=\"Bang\" id=\"B2\" style=\"\">"
        _html +="<div style=\"DISPLAY: block\" class=\"Banglist\">"
        _html += txtone
        _html +="</div>"
        _html +="</ul>"
        _html +="<ul name=\"B2\" style=\"display: none;\" class=\"Bang\" id=\"B2\">"
        _html +="<div jquery17205382323661072996=\"11\" style=\"DISPLAY: block\" class=\"Banglist\">"
        _html += txttwo
        _html +="</div>"
        _html +="</ul>"
        _html +="</div>"
        _html +="</div>"
        return _html


    def getText170(self):
        posturl = "http://www.gzevergrandefc.com/ajax/handler.ashx"
        cj = cookielib.LWPCookieJar()
        cookie_support = urllib2.HTTPCookieProcessor(cj)
        opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        headers = {'User-Agent':'Mozilla/5.0 (X11; U; Linux i686; zh-CN; rv:1.9.1.2) Gecko/20090803 Fedora/3.5.2-2.fc11 Firefox/3.5.2'}
        postData = {'action' : 'bang','from':'other','id':'170','nocache' : '0.6874064390080088'}
        postData = urllib.urlencode(postData)
        request = urllib2.Request(posturl,postData,headers)
        response = urllib2.urlopen(request,timeout=40)
        text = response.read().replace("{$race$}","")
        return text


    def parse17(self):
        html = ""
        _html = self.getText173()
        soup = BeautifulSoup(_html,fromEncoding="gb18030")
        div_list = soup.findAll("div",{'class':'Banglist'})
        _txt1 =  "".join([str(x) for x in  div_list[0].contents])
        _txt2 =  "".join([str(x) for x in  div_list[1].contents])
        _173txt = self.template173(_txt1.decode("utf8").encode("gb2312"),_txt2.decode("utf8").encode("gb2312"))

        _html = self.getText170()
        soup = BeautifulSoup(_html,fromEncoding="gb18030")
        div_list= soup.findAll("div",{'class':'Banglist'})
        _txt1 =  "".join([str(x) for x in  div_list[0].contents])
        _txt2 =  "".join([str(x) for x in  div_list[1].contents])
        _170txt =self.template170(_txt1.decode("utf8").encode("gb2312"),_txt2.decode("utf8").encode("gb2312"))
        html += _173txt
        html += _170txt
        return html


if __name__ == "__main__":
    obj = Hengdafc()
    _html =  obj.parse17()
    #_html =  obj.getText170()
    filename = "/data0/htdocs/www/we/guangzhouhengda/hengdafc.html"
    #filename = "hengdafc.html"
    fileHandle = open(filename,'w')
    fileHandle.write(_html)
    fileHandle.close()
  