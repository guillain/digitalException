/*
 @ Target: MySQL structure
 @ Version: 0.1
 @ Date: 2017/02/04
 @ Author: Guillain (guillain@gmail.com)
 @ Copyright 2017 GPL - Guillain
*/

drop table if exists user;
create table user (
  uid integer primary key auto_increment,
  login varchar(32) not null,
  email varchar(64) not null,
  landline varchar(16) not null,
  mobile varchar(16) not null,
  pw_hash text not null,
  accesstoken text not null,
  creationdate date not null,
  UNIQUE KEY (login),
  UNIQUE KEY (email)
);

drop table if exists groups;
create table groups (
  gid integer primary key auto_increment,
  name varchar(32) not null,
  description text not null,
  creationdate date,
  UNIQUE KEY (name)
);

drop table if exists mapping;
create table mapping (
  mid integer primary key auto_increment,
  uid integer,
  gid integer,
  roomid text,
  teamid text,
  peopleid text,
  msgid text,
  admin boolean,
  moder boolean,
  level integer
);

--
-- Table structure for table `events`
--
DROP TABLE IF EXISTS `events`;
CREATE TABLE `events` (
  `eid` int(11) NOT NULL AUTO_INCREMENT,
  `module` varchar(32) NOT NULL,
  `id` varchar(32) NOT NULL,
  `timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `msg` text NOT NULL,
  `status` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`eid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

