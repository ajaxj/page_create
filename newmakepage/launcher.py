#!/usr/bin/python
# -*- coding:utf-8 -*-
import random
import time
import template

__author__ = 'ajaxj'
import os

PATH = "D:\data1"

#添加目录下的文件进list
def AddPathToList(path):
    fileList = []
    files = os.listdir(path)
    for f in files:
        if not os.path.isdir(path+'/'+f) :
            fileList.append(f)
    return fileList

#读取文件内容分标题和正文
def ReadFilesToList(fileList):
    list = []
    pageNum = 10001
    for file in fileList:
        filename = PATH + '/' + file
        fileHandle = open(filename)
        i = 0       #控制计数
        _title = None
        _content= None
        for line in fileHandle:
            if i > 0:
                _content = line
            else:
                _title = line
            i= i+1

        if _content != None:
            list.append([_title,_content,pageNum])
        pageNum = pageNum + 1
        fileHandle.close()
    return list


def createPages():
    fileList = AddPathToList(PATH)
    textList = ReadFilesToList(fileList)
    # print len(textList)
    # exit(1)

    page_count = 0
    for seo in textList:
        if page_count == 100:
            html_tmp = ""
            for seo in textList[0:100]:
                title = seo[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index.html"
            fileHandle = open(filename,'w')
            index_html = template.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 200:
            html_tmp = ""
            for seo in textList[100:200]:
                title = seo[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index2.html"
            fileHandle = open(filename,'w')
            index_html = template.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 300:
            html_tmp = ""
            for seo in textList[200:300]:
                title = seo[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index3.html"
            fileHandle = open(filename,'w')
            index_html = template.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
        elif page_count == 400:
            html_tmp = ""
            for seo in textList[300:400]:
                title = seo[0]
                html_tmp +="<DIV class=wdlx>"
                html_tmp +="<DL>&gt;&gt;</DL>"
                html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
            filename = "d:/data/index4.html"
            fileHandle = open(filename,'w')
            index_html = template.index_getHtml(html_tmp)
            fileHandle.write(index_html)
            fileHandle.close()
    #     elif page_count == 500:
    #         html_tmp = ""
    #         for seo in textList[400:500]:
    #             title = seo[0]
    #             html_tmp +="<DIV class=wdlx>"
    #             html_tmp +="<DL>&gt;&gt;</DL>"
    #             html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
    #         filename = "d:/data/index5.html"
    #         fileHandle = open(filename,'w')
    #         index_html = template.index_getHtml(html_tmp)
    #         fileHandle.write(index_html)
    #         fileHandle.close()
    #     elif page_count == 600:
    #         html_tmp = ""
    #         for seo in textList[500:600]:
    #             title = seo[0]
    #             html_tmp +="<DIV class=wdlx>"
    #             html_tmp +="<DL>&gt;&gt;</DL>"
    #             html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
    #         filename = "d:/data/index6.html"
    #         fileHandle = open(filename,'w')
    #         index_html = templateindex.index_getHtml(html_tmp)
    #         fileHandle.write(index_html)
    #         fileHandle.close()
        # elif page_count == 700:
        #     html_tmp = ""
        #     for seo in seo_list[1600:1700]:
        #         title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
        #         html_tmp +="<DIV class=wdlx>"
        #         html_tmp +="<DL>&gt;&gt;</DL>"
        #         html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
        #     filename = "d:/data/index7.html"
        #     fileHandle = open(filename,'w')
        #     index_html = wetemplateindex.index_getHtml(html_tmp)
        #     fileHandle.write(index_html)
        #     fileHandle.close()
        # elif page_count == 800:
        #     html_tmp = ""
        #     for seo in seo_list[2700:2800]:
        #         title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
        #         html_tmp +="<DIV class=wdlx>"
        #         html_tmp +="<DL>&gt;&gt;</DL>"
        #         html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
        #     filename = "d:/data/index8.html"
        #     fileHandle = open(filename,'w')
        #     index_html = wetemplateindex.index_getHtml(html_tmp)
        #     fileHandle.write(index_html)
        #     fileHandle.close()
        # elif page_count == 900:
        #     html_tmp = ""
        #     for seo in seo_list[3800:3900]:
        #         title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
        #         html_tmp +="<DIV class=wdlx>"
        #         html_tmp +="<DL>&gt;&gt;</DL>"
        #         html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
        #     filename = "d:/data/index9.html"
        #     fileHandle = open(filename,'w')
        #     index_html = wetemplateindex.index_getHtml(html_tmp)
        #     fileHandle.write(index_html)
        #     fileHandle.close()
        # elif page_count == 1000:
        #     html_tmp = ""
        #     for seo in seo_list[900:1000]:
        #         title = seo[0] + random.choice(seo_list)[0] + random.choice(seo_list)[0]
        #         html_tmp +="<DIV class=wdlx>"
        #         html_tmp +="<DL>&gt;&gt;</DL>"
        #         html_tmp +="<UL><A title=\""+title+"\" href=\"/data/news_"+str(seo[2])+"/index.html\" target=_blank>"+title+"</A></UL><SPAN>"+time.strftime("%m-%d",time.localtime())+"</SPAN></DIV>"
        #     filename = "d:/data/index10.html"
        #     fileHandle = open(filename,'w')
        #     index_html = wetemplateindex.index_getHtml(html_tmp)
        #     fileHandle.write(index_html)
        #     fileHandle.close()
        else:
            print "none"
        page_count += 1




    for text in textList:
        path = r'%s/%s'%("d:/data","news_"+str(text[2]))
        if os.path.exists(path) == False:
            os.makedirs(path)


        temp_seo_list=[]
        for i in range(1,86):
            temp_seo_list.append(random.choice(textList))
        html = template.getHtml(text[1],text,temp_seo_list)
        filename = path + "/index.html"
        fileHandle = open(filename,'w')
        fileHandle.write(html)
        fileHandle.close()
        print path




if __name__ == '__main__':
    createPages()


