#!/usr/bin/python
# -*- coding:utf-8 -*-
import MySQLdb
import template
import os

__author__ = 'Administrator'
import win32com.client

# 109  112 澳门赌场 1

# 110   114 玩法 2

# 111 113 攻略 3

dbpath = "E:/LocoySpider/Data/LocoySpider/109/SpiderResult.mdb"



def getDatabaseForList113():
    data_list = []
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=E:/LocoySpider/Data/LocoySpider/113/SpiderResult.mdb;"
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Cursorlocation=3
    rs_name = 'select * from Content'#表名
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()
    for x in range(rs.RecordCount):
        if rs.EOF:
            print "End of records"
            break
        else:
            data_list.append([rs.Fields.Item(3).Value,rs.Fields.Item(4).Value,3])
            rs.MoveNext()
    rs.Close()
    conn.Close()
    for data in data_list:
        insertToSQLite(data)


def getDatabaseForList111():
    data_list = []
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=E:/LocoySpider/Data/LocoySpider/137/SpiderResult.mdb;"
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Cursorlocation=3
    rs_name = 'select * from Content'#表名
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()
    for x in range(rs.RecordCount):
        if rs.EOF:
            print "End of records"
            break
        else:
            data_list.append([rs.Fields.Item(3).Value,rs.Fields.Item(4).Value,3])
            rs.MoveNext()
    rs.Close()
    conn.Close()
    for data in data_list:
        insertToSQLite(data)



def getDatabaseForList114():
    data_list = []
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=E:/LocoySpider/Data/LocoySpider/137/SpiderResult.mdb;"
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Cursorlocation=3
    rs_name = 'select * from Content'#表名
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()
    for x in range(rs.RecordCount):
        if rs.EOF:
            print "End of records"
            break
        else:
            data_list.append([rs.Fields.Item(3).Value,rs.Fields.Item(4).Value,2])
            rs.MoveNext()
    rs.Close()
    conn.Close()
    # print len(data_list)
    for data in data_list:
        # print data
        insertToSQLite(data)



def getDatabaseForList110():
    data_list = []
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=E:/LocoySpider/Data/LocoySpider/136/SpiderResult.mdb;"
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Cursorlocation=3
    rs_name = 'select * from Content'#表名
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()
    for x in range(rs.RecordCount):
        if rs.EOF:
            print "End of records"
            break
        else:
            data_list.append([rs.Fields.Item(3).Value,rs.Fields.Item(4).Value,2])
            rs.MoveNext()
    rs.Close()
    conn.Close()
    for data in data_list:
        insertToSQLite(data)


def getDatabaseForList112():
    data_list = []
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=E:/LocoySpider/Data/LocoySpider/112/SpiderResult.mdb;"
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Cursorlocation=3
    rs_name = 'select * from Content'#表名
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()
    for x in range(rs.RecordCount):
        if rs.EOF:
            print "End of records"
            break
        else:
            print rs.Fields.Item(3).Value,rs.Fields.Item(4).Value
            data_list.append([rs.Fields.Item(3).Value,rs.Fields.Item(4).Value,1])
            rs.MoveNext()
    rs.Close()
    conn.Close()
    for data in data_list:
        insertToSQLite(data)


def getDatabaseForList109():
    data_list = []
    conn = win32com.client.Dispatch(r'ADODB.Connection')
    DSN = "Provider=Microsoft.ACE.OLEDB.12.0;Data Source=E:/LocoySpider/Data/LocoySpider/135/SpiderResult.mdb;"
    conn.Open(DSN)
    rs = win32com.client.Dispatch(r'ADODB.Recordset')
    rs.Cursorlocation=3
    rs_name = 'select * from Content'#表名
    rs.Open('[' + rs_name + ']', conn, 1, 3)
    rs.MoveFirst()
    for x in range(rs.RecordCount):
        if rs.EOF:
            print "End of records"
            break
        else:
            data_list.append([rs.Fields.Item(3).Value,rs.Fields.Item(4).Value,1])
            rs.MoveNext()
    rs.Close()
    conn.Close()
    for data in data_list:
        # print data
        insertToSQLite(data)


#保存数据时SQLite
def insertToSQLite(data):
    conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="macao",charset="utf8")
    sql = "SELECT * FROM arts WHERE title = '%s' and cateid='%d'" %(data[0],data[2])
    # print sql + str(data[2])
    cur = conn.cursor()
    cur.execute(sql)
    if cur.fetchone() == None:
        sql = "INSERT INTO arts(title,content,cateid)" \
                " VALUES ('%s','%s','%d')" %(data[0].replace('\'','`'),data[1].replace('\'','`'),data[2])
        # print sql
        try:
            cur.execute(sql)
            conn.commit()
        except Exception,e:
            print e
            exit(1)
        finally:
            cur.close()
            conn.close()


def createPage():
    #UPDATE arts SET publish = 1 WHERE cateid = 1 and publish=0 limit 20
    conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="macao",charset="utf8")
    sql_1 = "SELECT * FROM arts WHERE cateid = 1 and publish=0 limit 0, 20"
    sql_2 = "SELECT * FROM arts WHERE cateid = 2 and publish=0 limit 0, 20"
    sql_3 = "SELECT * FROM arts WHERE cateid = 3 and publish=0 limit 0, 20"
    cur = conn.cursor()
    cur.execute(sql_1)
    data_list1 = cur.fetchall()
    cur.execute(sql_2)
    data_list2 = cur.fetchall()
    cur.execute(sql_3)
    data_list3 = cur.fetchall()
    cur.close()
    conn.close()

    news1_data = []
    news2_data = []
    news3_data = []


    #先取出来解码，然后加入标题，内容，页码
    pagenum = 640
    for row in data_list1:
        data = [row[1].encode('utf-8'),row[2].encode('utf-8'),pagenum]
        news1_data.append(data)
        pagenum += 1


    # 玩法
    pagenum = 640
    for row in data_list2:
        data = [row[1].encode('utf-8'),row[2].encode('utf-8'),pagenum]
        news2_data.append(data)
        #createDetailPage(data,pagenum,2,data_list1,data_list2,data_list3)
        pagenum += 1

    #攻略
    pagenum = 640
    for row in data_list3:
        data = [row[1].encode('utf-8'),row[2].encode('utf-8'),pagenum]
        news3_data.append(data)
        #createDetailPage(data,pagenum,3,data_list1,data_list2,data_list3)
        pagenum += 1

    #产生页面
    for news in news1_data:
        createDetailPage(news,1,news1_data,news2_data,news3_data)
    createListPage(1,news1_data,news2_data,news3_data)

    for news in news2_data:
        createDetailPage(news,2,news1_data,news2_data,news3_data)
    createListPage(2,news2_data,news1_data,news3_data)

    for news in news3_data:
        createDetailPage(news,3,news1_data,news2_data,news3_data)

    createListPage(3,news3_data,news1_data,news2_data)
    createHomePage(news1_data,news2_data,news3_data)






def createHomePage(news1_data,news2_data,news3_data):
    filename = r'%s/%s'%("e:/macao/", "index.html" )
    html = template.getHomeText(news1_data,news2_data,news3_data)
    fileHandle = open(filename,'w')
    fileHandle.write(html)
    fileHandle.close()

def createListPage(cateid,data,data1,data2):
    if cateid == 1:
        filename = r'%s/%s'%("e:/macao/duchang", "index.html" )
    elif cateid == 2:
        filename = r'%s/%s'%("e:/macao/wanfa","index.html" )
    else:
        filename = r'%s/%s'%("e:/macao/gonglue", "index.html" )
    html = template.getListseoText(cateid,data,data1,data2)
    fileHandle = open(filename,'w')
    fileHandle.write(html)
    fileHandle.close()

def createDetailPage(data,cateid,data_list1,data_list2,data_list3):
    if cateid == 1:
        filename = r'%s/%s'%("e:/macao/duchang",str(data[2]) + ".html" )
    elif cateid == 2:
        filename = r'%s/%s'%("e:/macao/wanfa",str(data[2]) + ".html" )
    else:
        filename = r'%s/%s'%("e:/macao/gonglue",str(data[2]) + ".html" )
    html = template.getDetailText(data,cateid,data_list1,data_list2,data_list3)
    fileHandle = open(filename,'w')
    fileHandle.write(html)
    fileHandle.close()
    print "ok " + str(data[2])


# 重命名生成INDEX 进一的文件名
def createIndexPage():
    path = 'e:\macao\duchang\\'
    newpath = 'e:\macao1\d\\'
    listfile = os.listdir(path)
    list = []
    for line in listfile:
        s =line[5:-5]
        if s == '':
            s = '1'
        s = int(s)
        list.append((line,s))

    a  = sorted(list, key=lambda list : list[1])
    for i in a:
        filename =i[0]
        newfilename = "index" + str(i[1]+1) + ".html"
        print filename,newfilename
        os.rename(os.path.join(path,filename), os.path.join(newpath,newfilename))

    path = 'e:\macao\gonglue\\'
    newpath = 'e:\macao1\g\\'
    listfile = os.listdir(path)
    list = []
    for line in listfile:
        s =line[5:-5]
        if s == '':
            s = '1'
        s = int(s)
        list.append((line,s))

    a  = sorted(list, key=lambda list : list[1])
    for i in a:
        filename =i[0]
        newfilename = "index" + str(i[1]+1) + ".html"
        print filename,newfilename
        os.rename(os.path.join(path,filename), os.path.join(newpath,newfilename))


    path = 'e:\macao\wanfa\\'
    newpath = 'e:\macao1\w\\'
    listfile = os.listdir(path)
    list = []
    for line in listfile:
        s =line[5:-5]
        if s == '':
            s = '1'
        s = int(s)
        list.append((line,s))

    a  = sorted(list, key=lambda list : list[1])
    for i in a:
        filename =i[0]
        newfilename = "index" + str(i[1]+1) + ".html"
        print filename,newfilename
        os.rename(os.path.join(path,filename), os.path.join(newpath,newfilename))


if __name__ == '__main__':
    # createIndexPage()
    # 1
    # getDatabaseForList109()
    # getDatabaseForList112()
    # # 2
    # getDatabaseForList110()
    # getDatabaseForList114()
    # 3
    # getDatabaseForList111()
    # getDatabaseForList113()

    createPage()












