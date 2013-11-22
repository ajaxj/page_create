DROP TABLE IF EXISTS `spcns`.`supe_tags`;
CREATE TABLE  `spcns`.`supe_tags` (
  `tagid` mediumint(8) unsigned NOT NULL auto_increment,
  `tagname` char(20) NOT NULL default '',
  `uid` mediumint(8) unsigned NOT NULL default '0',
  `username` char(15) NOT NULL default '',
  `dateline` int(10) unsigned NOT NULL default '0',
  `close` tinyint(1) NOT NULL default '0',
  `spacenewsnum` mediumint(8) unsigned NOT NULL default '0',
  `relativetags` char(255) NOT NULL default '',
  PRIMARY KEY  (`tagid`),
  KEY `tagname` (`tagname`),
  KEY `tagid` (`tagid`,`dateline`),
  KEY `close` (`close`,`spacenewsnum`),
  KEY `close1` (`close`),
  KEY `num` (`spacenewsnum`)
) ENGINE=MyISAM AUTO_INCREMENT=107579 DEFAULT CHARSET=gbk;

账号:
2000stars
apple
awalaz
bwin
gyj129
gonebabyone
gonebabygone
xiaoxiongmao
cicy
iverson
水立方
cason
tennis
racing
tutu
爱姚联盟主席
点金成石
高杆
健康运动
老大不小
盘路
体育星尚
传媒人俱乐部
冒险阿宝
hoopking
高盛
绅士网球
diver
蓝色王国
土豆
sportscn
ppmm
golfer
