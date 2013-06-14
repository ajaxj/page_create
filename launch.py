# -*- coding:gbk -*-
import os
import string
import random
import time
import template
import templateindex
from BeautifulSoup import BeautifulSoup

__author__ = 'ajaxj'


def parseHtml():
    soup = BeautifulSoup(template.getTemplate())
    a_list  = soup.findAll("a")
    for a in a_list:
        print a
    print len(a_list)



def readText():
    list = []
    filename = "1.txt"
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
    filename = "0607seo1000.txt"
    fileHandle = open(filename)
    line = fileHandle.readline().decode('gbk').encode('utf-8')
    list = []
    i = 2484
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
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 200:
            html_tmp = ""
            for seo in seo_list[100:200]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index2.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 300:
            html_tmp = ""
            for seo in seo_list[200:300]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index3.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 400:
            html_tmp = ""
            for seo in seo_list[300:400]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index4.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 500:
            html_tmp = ""
            for seo in seo_list[400:500]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index5.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 600:
            html_tmp = ""
            for seo in seo_list[500:600]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index6.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 700:
            html_tmp = ""
            for seo in seo_list[600:700]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index7.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 800:
            html_tmp = ""
            for seo in seo_list[700:800]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index8.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 900:
            html_tmp = ""
            for seo in seo_list[800:900]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index9.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 1000:
            html_tmp = ""
            for seo in seo_list[900:1000]:
                title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index10.html"
            fileHandle = open(filename,'w')
            index_html = templateindex.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        else:
            print "none"
        page_count += 1

    # page_count = len(seo_list)
    # pagenum = 0
    # page = 2
    # html_tmp = ""
    # for i in range(1,page_count):
    #     html_tmp +="<DIV class=wdlx>"
    #     html_tmp +="<DL>&gt;&gt;</DL>"
    #     html_tmp +="<UL><A title=\"世界杯预选赛阿根廷三连平 马斯切拉诺离奇罚下\" href=\"http://we.sportscn.com/viewnews-1322177.html\" target=_blank>世界杯预选赛阿根廷三连平 马斯切拉诺离奇罚下</A></UL><SPAN>06-13</SPAN></DIV>"
    #     if(pagenum > 100):
    #         # filename = "d:/data/index" + str(page) +".html"
    #         # fileHandle = open(filename,'w')
    #         # index_html = templateindex.index_getHtml(html_tmp)
    #         # fileHandle.write(index_html)
    #         # fileHandle.close()
    #         print html_tmp
    #         pagenum = 0
    #         page += 1
    #         html_tmp=""
    #     else:
    #         # index_html = templateindex.index_getHtml(html_tmp)
    #         # filename = "d:/data/index.html"
    #         # fileHandle = open(filename,'w')
    #         # fileHandle.write(index_html)
    #         # fileHandle.close()
    #         html_tmp=""
    #     pagenum+=1





    page = 0
    index_html = ""
    for seo in seo_list:
        path = r'%s/%s'%("d:/data","news_"+str(seo[2]))
        if os.path.exists(path) == False:
            os.makedirs(path)
        list_str = readText()

        index_html += '<a href="">test</a><br/>'

        # for i in range(1,len(list_str)):
        #     print list_str[i]
        #
        # exit(1)


        msg = ''
        msg_1 = random.choice(list_str)
        # print list_str[1].decode('gbk').encode('utf-8')
        # print msg_1.decode("gbk").encode('utf-8')
        # exit(1)
        # msg_1 = list_str[3]
        # print msg_1.decode('gbk').encode('utf-8')
        # print msg_1
        # exit(1)
        for ml in range(1,6):
            msg_1 = random.choice(list_str)
            msg +=  msg_1.decode('gbk').encode('utf-8') + seo[0]# + random.choice(list_str)
            # msg =msg + msg_1[:int(index)] + seo


        # msg = msg_1.decode('gbk').encode('utf-8')
        #print msg
        # msg = list_str[page].decode('gbk').encode('utf-8')
        # print msg
        temp_seo_list = []
        for i in range(1,86):
            temp_seo_list.append(random.choice(seo_list))

        html =  template.getHtml(msg,seo,temp_seo_list)
        # html = template.getTemplate()
        filename = path + "/index.html"
        fileHandle = open(filename,'w')
        fileHandle.write(html)
        fileHandle.close()
        page +=1
        print path




if __name__ == "__main__":
    # parseHtml()
    createPages()
    # list = readText()
    # print len(list)
    # # print list[0]
    # print "-----------"
    # txt = random.choice(list)
    # print txt
    # print list[97]
    # print list[100]
    # print list[199]