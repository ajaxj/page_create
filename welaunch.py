# -*- coding:gbk -*-
import os
import string
import random
import time
import wetemplate
import wetemplateindex
from BeautifulSoup import BeautifulSoup

__author__ = 'ajaxj'


def parseHtml():
    soup = BeautifulSoup(wetemplate.getTemplate())
    a_list  = soup.findAll("a")
    for a in a_list:
        print a
    print len(a_list)



def readText():
    list = []
    # filename = "1.txt.bak"
    filename = "2.txt"
    fileHandle = open(filename)
    msg = fileHandle.read()
    # s  = unicode(s,'gbk') #转为unicode
    # s  = s.encode('utf-8')
    # #
    # fileHandle.close()
    # s = template.txt1
    # print s
    # print len(s)
    # print cut_str(s, 110)
    # exit(1)
    # s = s.replace("\n","")
    # s = s.replace("\r","")
    # s = s.replace("\t","")
    # j = 499
    # for i in range(1,len(s),499):
    #     # print i,j
    #     txt = s[i:j]
    #     list.append(txt)
    #     j =j+499

    n = 300
    #长度
    l = len(msg)
    #循环截取开始num
    start = 0
    #循环截取截止num
    end = n

    while True:
            #判断截止num是否超过总长度
            if(end >= l):
                    end = l
                    #如果超出长度怎停止while
                    stop = True
            else:
                    stop = False

            try:
                    t = msg[start:end]
                    #判断可否unicode，如果不能则截取提前一位
                    unicode(t,'gbk')
                    w = 0
            except:
                    end -=1
                    t = msg[start:end]
                    w = 1
            #计算下次截取的开始与截止num
            if w == 0:
                    start += n
                    end   += n
            else:
                    start += n-1
                    end   += n
            # print t
            list.append(t)
            #跳出
            if stop:
                    break



    # print list[0]

    return list


def readSeoToList():
    # filename = "0607seo1000.txt.bak"
    filename = "bf4500_0618.txt"
    fileHandle = open(filename)
    line = fileHandle.readline().decode('gbk').encode('utf-8')
    list = []
    i = 1
    while line:
        line_arr = line.split("\t")

        list.append([line_arr[0], line_arr[1],i])
        line = fileHandle.readline().decode('gbk').encode('utf-8')
        i+=1
    fileHandle.close()
    return list



def cut_str(str, length=10):
    """
    截取字符串，使得字符串长度等于length，并在字符串后加上省略号
    """
    is_encode = False
    try:
        str_encode = str.encode('gb18030') #为了中文和英文的长度一致（中文按长度2计算）
        is_encode = True
    except:
        pass
    if is_encode:
        l = length*2
        if l < len(str_encode):
            l = l - 3
            str_encode = str_encode[:l]
            try:
                str = str_encode.decode('gb18030') + '...'
            except:
                str_encode = str_encode[:-1]
                try:
                    str = str_encode.decode('gb18030') + '...'
                except:
                    is_encode = False
    if not is_encode:
        if length < len(str):
            length = length - 2
            return str[:length] + '...'
    return str





def createPages():

    seo_list = readSeoToList()
    page_count = 0
    for seo in seo_list:
        if page_count == 100:
            html_tmp = ""
            for seo in seo_list[0:100]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 200:
            html_tmp = ""
            for seo in seo_list[1000:1200]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index2.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 300:
            html_tmp = ""
            for seo in seo_list[2200:2300]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index3.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 400:
            html_tmp = ""
            for seo in seo_list[3300:3400]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index4.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 500:
            html_tmp = ""
            for seo in seo_list[1400:1500]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index5.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 600:
            html_tmp = ""
            for seo in seo_list[2500:2600]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index6.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 700:
            html_tmp = ""
            for seo in seo_list[1600:1700]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index7.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 800:
            html_tmp = ""
            for seo in seo_list[2700:2800]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index8.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 900:
            html_tmp = ""
            for seo in seo_list[3800:3900]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index9.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 1000:
            html_tmp = ""
            for seo in seo_list[900:1000]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/news/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/news/index10.html"
            fileHandle = open(filename,'w')
            index_html = wetemplateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        else:
            print "none"
        page_count += 1






    page = 0
    index_html = ""
    for seo in seo_list:
        path = r'%s/%s'%("d:/news","/news_"+str(seo[2]))
        if os.path.exists(path) == False:
            os.makedirs(path)
        list_str = readText()

        index_html += '<a href="">test</a><br/>'



        msg = ''
        msg_1 = random.choice(list_str)

        for ml in range(1,10):
            msg_1 = random.choice(list_str)
            msg +=  msg_1.decode('gbk').encode('utf-8') + seo[0]# + random.choice(list_str)
            # msg =msg + msg_1[:int(index)] + seo


        temp_seo_list = []
        for i in range(1,86):
            temp_seo_list.append(random.choice(seo_list))

        html =  wetemplate.getHtml(msg,seo,temp_seo_list)
        filename = path + "/index.html"
        fileHandle = open(filename,'w')
        fileHandle.write(html)
        fileHandle.close()
        page +=1
        print path




if __name__ == "__main__":
    # parseHtml()
    createPages()

