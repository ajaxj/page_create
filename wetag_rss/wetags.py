# -*- coding:gbk -*-
import urllib
import urllib2
import MySQLdb
import sys


class Wetags:
    usernames = ['2000stars','apple','awalaz','bwin','gyj129','gonebabygone','xiaoxiongmao','cicy',\
                 'iverson','ˮ����','cason','tennis','racing','tutu','��Ҧ������ϯ','����ʯ','�߸�',\
                 '�����˶�','�ϴ�С','��·','��������','��ý�˾��ֲ�','ð�հ���','hoopking','��ʢ',\
                 '��ʿ����','diver','��ɫ����','����','sportscn','ppmm','golfer']
    #usernames =['ˮ����','��ʿ����']

    #��������ʱSQLite
    def selectUsername(self,username):
        html = ""
        try:
            conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="mitiyu",charset="gbk")
            sql = "SELECT tagid,tagname,spacenewsnum FROM supe_tags WHERE username = '%s' order by spacenewsnum desc limit 8000" %(username)
            #sql = "SELECT tagid,tagname FROM supe_tags WHERE username = '%s' order by spacenewsnum" %(username)
            cur = conn.cursor()
            cur.execute(sql)
            data = cur.fetchall()
            for row in data:
                print row[0]
                html +="<LI><a href=\"http://we.sportscn.com/action-tag-tagname-"+ urllib.quote(row[1].encode('gbk')) +".html\"  target=\"_blank\" title=\""+ row[1] + "\">"+ row[1] + "</a> </LI>"
                #html +="<LI><a href=\"http://we.sportscn.com/action-tag-tagname-"+ urllib.quote(row[1].encode('gbk') +".html\" target=\"_blank\" title=\""+ row[1] + "\"><b>"+ row[1] + "</b></a></LI>"
        except Exception,e:
            print e
        finally:
            cur.close()
            conn.close()
        return html

    def createHtml(self,html):
        _html = "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">"
        _html +="<html xmlns=\"http://www.w3.org/1999/xhtml\">"
        _html +="<head>"
        _html +="<meta http-equiv=\"Content-Type\" content=\"text/html; charset=gbk\" />"
        _html +="<title>tagҳ��-������</title>"
        _html +="<link href=\"style/style.css\" rel=\"stylesheet\" type=\"text/css\" media=\"all\" />"
        _html +="</head>"
        _html +="<body id=\"home\">"
        _html +="<h1>������ tagҳ��</h1>"
        _html +="<div id=\"bodyBg\">"
        _html +="<div id=\"footerBg\">"
        _html +="<div id=\"warper\">"
        _html +="<div class=\"top\"><a href=\" http://www.sportscn.com\" class=\"logo\"></a>"
        _html +="<div class=\"seach\">"
        _html +="<form>"
        _html +="<input type=\"text\" value=\"����ȫ������\" />"
        _html +="<a href=\"#nogo\"><img src=\"style/img/space.gif\" alt=\"����\" /></a>"
        _html +="</form>"
        _html +="<p><a href=\"http://news.sportscn.com\" target=\"_blank\">����</a> | <a href=\"http://live.sportscn.com\" target=\"_blank\">�ȷ�</a> | <a href=\"http://guess.sportscn.com\" target=\"_blank\">��Ϸ</a> | <a href=\"http://golf.sportscn.com\" target=\"_blank\">�߶���</a> | <a href=\"http://club.sportscn.com\" target=\"_blank\">����</a></p>"
        _html +="</div>"
        _html +="<div class=\"nav\"> <a href=\"index.html\">���ڻ���</a><a href=\"ad.html\">������</a><a href=\"job.html\">��Ƹ��Ϣ</a><a href=\"legal.html\">��������</a><a href=\"contact.html\">��ϵ����</a><a class=\"cur\" href=\"sitemape.html\" title=\"��վ��ͼ\">��վ��ͼ</a><a class=\"last\" href=\"events.html\">���¼�</a> </div>"
        _html +="</div>"
        _html +="<div class=\"main clearfix\">"
        _html +="<h2>������ tag</h2>"
        _html +="<div class=\"mainCon\">"
        _html +="<DIV class=\"about\">"
        _html +="<Div>"
        _html +="<H3><A href=\"http://live.sportscn.com/\" title=\"������ tag\" target=_blank>������ tagҳ��</A></H3>"
        _html +="<UL>"
        _html += html
        _html +="</UL></DIV>"
        _html +="</DIV>"
        _html +="</p>"
        _html +="</div>"
        _html +="</div>"
        _html +="<div class=\"footer\">"
        _html +="<p>&copy;2000-<script>var date=new Date();document.write(date.getFullYear());</script>  ������  ��Ȩ���� ��<a href=\"http://www.sportscn.com/aboutus/aboutus4.html\" target=\"_blank\">������[2005]016��</a> ��ICP��10022738��</p>"
        _html +="</div></div>"
        _html +="</div>"
        _html +="</div>"
        _html +="</body>"
        _html +="</html>"
        return _html

    def createTag(self):
        html =""
        for username in self.usernames:
        #    print username
            html += self.selectUsername(username)

        print html
        _html = self.createHtml(html.encode('gbk'))
        filename = "tag.html"
        fileHandle = open(filename,'w')
        fileHandle.write(_html)
        fileHandle.close()

if __name__ == '__main__':
    obj = Wetags()
    obj.createTag()



