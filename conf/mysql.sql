/*
 @ Target: MySQL structure
 @ Version: 0.1
 @ Date: 2017/02/04
 @ Author: Guillain (guillain@gmail.com)
 @ Copyright 2017 GPL - Guillain
*/

--
-- Database: digitalException
--
CREATE DATABASE IF NOT EXISTS digitalExceptionDEFAULT CHARACTER SET latin1 COLLATE latin1_swedish_ci;
USE digitalException;

-- --------------------------------------------------------

--
-- Table structure for table events
--

DROP TABLE IF EXISTS events;
CREATE TABLE events (
  eid int(11) NOT NULL,
  module varchar(32) NOT NULL,
  id varchar(128) NOT NULL,
  msg text NOT NULL,
  owner varchar(128) NOT NULL,
  status varchar(32) DEFAULT NULL,
  timestamp timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE events
  MODIFY eid int(11) NOT NULL AUTO_INCREMENT;

-- --------------------------------------------------------

--
-- Table structure for table groups
--

DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
  gid int(11) NOT NULL,
  name varchar(32) NOT NULL,
  description text NOT NULL,
  creationdate date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE groups
  MODIFY gid int(11) NOT NULL AUTO_INCREMENT;

-- --------------------------------------------------------

--
-- Table structure for table mapping
--

DROP TABLE IF EXISTS mapping;
CREATE TABLE mapping (
  id int(11) NOT NULL,
  uid int(11) DEFAULT NULL,
  gid int(11) DEFAULT NULL,
  roomid text,
  teamid text,
  peopleid text,
  msgid text,
  admin tinyint(1) DEFAULT NULL,
  moder tinyint(1) DEFAULT NULL,
  level int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE mapping
  MODIFY id int(11) NOT NULL AUTO_INCREMENT;

-- --------------------------------------------------------

--
-- Table structure for table user
--

DROP TABLE IF EXISTS user;
CREATE TABLE user (
  uid int(11) NOT NULL,
  login varchar(32) NOT NULL,
  email varchar(64) NOT NULL,
  landline varchar(16) NOT NULL,
  mobile varchar(16) NOT NULL,
  pw_hash text NOT NULL,
  accesstoken text NOT NULL,
  creationdate date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE user
  MODIFY uid int(11) NOT NULL AUTO_INCREMENT;

