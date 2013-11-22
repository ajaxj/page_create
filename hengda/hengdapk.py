# -*- coding:gb2312 -*-
import cookielib
import os
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup


class Hengdapk:

    url_fc = "http://www.gzevergrandefc.com/news.aspx"

    def Pankou(self,head_txt):
        _pk = "<div class=\"zxyg\">"
        _pk +="<div class=\"fm\"><b>恒大赛程</b> <a target=\"_blank\" href=\"http://live.sportscn.com\" class=\"more\">更多&gt;&gt;</a>"
        _pk +="</div>"
        _pk +="<div class=\"fm_b2\">"
        _pk +="<ul>"
        _pk += head_txt
        #_pk +="<div sizcache08117529042446193=\"30\" sizset=\"2\" class=\"sahishi_main\"><div sizcache08117529042446193=\"30\" sizset=\"2\" class=\"saishi_top\">"
        #_pk +="<ul sizcache08117529042446193=\"29\" sizset=\"15\">"
        #_pk +="<li sizcache08117529042446193=\"28\" sizset=\"15\" class=\"bisai\"><span><img src=\"images/yglogo.png\"></span><a>亚冠联赛</a> </li>"
        #_pk +="<li sizcache08117529042446193=\"28\" sizset=\"16\" class=\"s_left\">"
        #_pk +="<h3><img src=\"UploadFile\2013-10\31e3d70f-3d81-4a18-972a-9d5498bdc8a4.png\"></h3><a>广州恒大</a> </li>"
        #_pk +="<li sizcache08117529042446193=\"28\" sizset=\"17\" class=\"s_right\">"
        #_pk +="<h3><img src=\"UploadFile\2013-10\08553be9-6b44-45f7-b96b-80e6f5b0c4ad.png\"></h3><a>FC首尔</a> </li></ul></div>"
        #_pk +="<div sizcache08117529042446193=\"28\" sizset=\"18\" id=\"ctl00_ContentPlaceHolder1_ctl00_ctl00_UpdatePanel1\">"
        #_pk +="<div class=\"saishi_time\"><a id=\"ctl00_ContentPlaceHolder1_ctl00_ctl00_otherTime\">1天4时58分37秒</a> <span style=\"DISPLAY: none; VISIBILITY: hidden\" id=\"ctl00_ContentPlaceHolder1_ctl00_ctl00_Timer1\"></span></div></div>"
        #_pk +="<div class=\"saishi_bottom\">比赛时间：2013年11月09日20:00<br>地点：天河体育中心 直播：CCTV5</div></div>"
        _pk +="</ul>"
        _pk +="</div>"
        _pk +="</div>"
        return _pk

    def readToHtml(self):
        req = urllib2.Request(self.url_fc)
        res = urllib2.urlopen(req)
        htmlstr = res.read()
        soup = BeautifulSoup(htmlstr)
        div_sahishi_main = soup.find("div",{'class':'sahishi_main'})

        return div_sahishi_main.prettify().replace("<img src=\"","<img src=\"http://www.gzevergrandefc.com/")





if __name__ == "__main__":
    obj = Hengdapk()
    _head_txt = obj.readToHtml()
    _html = obj.Pankou(_head_txt.decode("utf8").encode("gb2312"))
    filename = "/data0/htdocs/www/we/guangzhouhengda/hengdapk.html"
    fileHandle = open(filename,"w")
    fileHandle.write(_html)
    fileHandle.close()




