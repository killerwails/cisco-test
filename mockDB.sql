DROP DATABASE IF EXISTS `cisco`;
CREATE DATABASE cisco;
USE cisco;
DROP USER IF EXISTS 'lookupService'@'localhost';
CREATE USER 'lookupService'@'localhost' IDENTIFIED BY 'd85g2J~oo77D';
GRANT ALL PRIVILEGES ON cisco TO 'lookupService'@'localhost'; 
DROP TABLE IF EXISTS `mockData`;
CREATE TABLE `mockData` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(2083) NOT NULL,
  `port` smallint(5) unsigned NOT NULL,
  `hostname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `lookup` (`id`,`url`,`port`,`hostname`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
LOCK TABLES `mockData` WRITE;
INSERT INTO `mockData` VALUES (1,'fosssso?djd/ee/',42,'fosobar'),(2,'ssso?djd/ee/',42,'fosobar'),(3,'sssso?djd/ee/',42,'fosobar'),(4,'sssso?djd/ee/',42,'fosobar'),(5,'ss3so?djd/ee/',42,'fosobar'),(6,'acc/sssso?djd/ee/',42,'fosobar'),(7,'acc/sssso?djd/ee/',42,'fosobar'),(8,'login?sssso?djd/ee/',42,'fosobar'),(9,'user/sssso?djd/ee/',42,'fosobar'),(10,'testurl?query',42,'foobar.com');
UNLOCK TABLES;
