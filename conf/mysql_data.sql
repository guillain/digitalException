/*
 @ Target: MySQL init data
 @ Version: 0.1
 @ Date: 2017/02/04
 @ Author: Guillain (guillain@gmail.com)
 @ Copyright 2017 GPL - Guillain
*/

INSERT INTO user (uid, login, email, landline, mobile, pw_hash, accesstoken, creationdate) VALUES
  ('1', 'guillain', 'guillain@gmail.com', '', '', '','', NOW()),

INSERT INTO groups (gid, name, description, creationdate) VALUES
  ('1', 'admin','Admin group',NOW()),
  ('2', 'user','User group',NOW()),
  ('3', 'guest','Guest group',NOW());

/* App user */
INSERT INTO mapping (uid, gid, admin, moder) VALUES
  ('1','1','1','1'),
  ('2','2','1','0'),
  ('3','3','0','0');


