# -*- coding:utf-8 -*-
__author__ = 'Administrator'


# current 当前页号 pagecount 页总数,id 分类
def createpage_template(current,pagecount,id):
    _page = "<div>"
    if id == 253:
        for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index"+str(i)+".html\">"+str(i)+"</a>"
        _page += "</div>"
    elif id == 254:
        for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdayaguan/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdayaguan/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdayaguan/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdayaguan/index"+str(i)+".html\">"+str(i)+"</a>"
        _page += "</div>"
    elif id == 255:
        for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/index"+str(i)+".html\">"+str(i)+"</a>"
        _page += "</div>"
    elif id == 256:
        for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashijubei/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashijubei/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashijubei/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashijubei/index"+str(i)+".html\">"+str(i)+"</a>"
        _page += "</div>"
    elif id == 257:
        for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashipin/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashipin/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashipin/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdashipin/index"+str(i)+".html\">"+str(i)+"</a>"
        _page += "</div>"
    elif id == 258:
        for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiu/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiu/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiu/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiu/index"+str(i)+".html\">"+str(i)+"</a>"
        _page += "</div>"
    elif id == 260:
        for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiuxuexiao/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiuxuexiao/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiuxuexiao/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiuxuexiao/index"+str(i)+".html\">"+str(i)+"</a>"
        _page += "</div>"
    else:
       for i in range(1,pagecount+1):
            if i == 1:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index.html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index.html\">"+str(i)+"</a>"
            else:
                if current == i:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index"+str(i)+".html\"><strong>"+str(i)+"</strong></a>"
                else:
                    _page += "<a href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index"+str(i)+".html\">"+str(i)+"</a>"
    _page += "</div>"
    return _page

#生成首页导航
def create_index_nav():
    _page ="<h1>广州恒大</h1><h2><a href=\"http://we.sportscn.com/guangzhouhengda\">首页</a></h2><h2><a title=\"恒大新闻\" href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengda/index.html\">球队新闻</a></h2><h2><a title=\"恒大官方公告\" href=\"http://we.sportscn.com/guangzhouhengda/guangzhouhengdazuqiujulebu/index.html\">官方公告</a></h2><h2><a title=\"恒大赛程赛果\" href=\"http://scripts1.sportscn.com/team.do?tid=5065&amp;lid=213&amp;lang=tr\">恒大赛程赛果</a></h2><h2><a title=\"恒大世俱杯\" href=\"http://we.sportscn.com/guangzhouhengda/hengdashijubei/index.html\">恒大世俱杯</a></h2><h2><a title=\"恒大亚冠\" href=\"http://we.sportscn.com/guangzhouhengda/hengdayaguan/index.html\">恒大亚冠</a></h2><h2><a title=\"恒大视频\" href=\"http://we.sportscn.com/guangzhouhengda/hengdashipin/index.html\">恒大视频</a></h2><h2><a title=\"恒大足球\" href=\"http://we.sportscn.com/guangzhouhengda/hengdazuqiu/index.html\">恒大足球</a></h2>"
    return _page