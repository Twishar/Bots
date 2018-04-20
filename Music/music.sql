BEGIN TRANSACTION;
CREATE TABLE `music` (
	`Id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`file_id`	TEXT NOT NULL,
	`right_answer`	TEXT NOT NULL,
	`wrong_answer`	TEXT NOT NULL
);
INSERT INTO `music` VALUES (1,'deck_the_halls','Deck','HZ');
INSERT INTO `music` VALUES (2,'lava_falls','Lava','hz');
INSERT INTO `music` VALUES (3,'the_midnight_ninja','Ninja','Hz');
INSERT INTO `music` VALUES (4,'we_three_kings','Kings','Hz');
COMMIT;
