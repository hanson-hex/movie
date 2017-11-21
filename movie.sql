-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: movie_project
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `is_super` smallint(6) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `role_id` (`role_id`),
  KEY `ix_admin_addtime` (`addtime`),
  CONSTRAINT `admin_ibfk_1` FOREIGN KEY (`role_id`) REFERENCES `role` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'admin1','pbkdf2:sha256:50000$dC0rNmML$21e09b16d72c089972bbe0aaa95a2c6676c1879bd0eb02fbd4fb8049abf7475d',1,'2017-11-13 22:33:27',NULL),(2,'admin2','pbkdf2:sha256:50000$eDVK1IKv$5ebe8fe3304a6a3e04fe09a40659321bad003b92006ef0fde6d0b92f97e26dae',1,'2017-11-13 22:33:27',NULL),(3,'admin3','pbkdf2:sha256:50000$1u3PXlis$996e0d931504cf2b32d718e4deb26f2aea3e46450fe8a70e81c452b029743541',1,'2017-11-13 22:33:27',NULL),(4,'admin4','pbkdf2:sha256:50000$eF37IXP0$a8426f7edc439dc7d089e8a7595facda9edbec74764ffde516316f6ff97788d0',1,'2017-11-13 22:33:27',NULL),(5,'admin5','pbkdf2:sha256:50000$latOWYfp$540a09a587079206966922a2da1ed80ceffaa7c7f542d46f5dc10754b23058e4',1,'2017-11-13 22:33:28',NULL),(6,'admin6','pbkdf2:sha256:50000$jZMOc7r1$3d6bf11d421bc430b8b97c7e87b1d1d4a43ab0180443660ccaa8cd7b5468728e',1,'2017-11-13 22:33:28',NULL),(7,'admin7','pbkdf2:sha256:50000$B0vpcOPW$f1d413aaf24216921ffe5e5b31cfea16b16c00e10d9374be5621b623276a8f7f',1,'2017-11-13 22:33:28',NULL),(8,'admin8','pbkdf2:sha256:50000$vWGpLqBj$7ae8ef7fe2fbd7db670c9913067bbf6e0fbeb279c5d78082da4a1f771570e6e4',1,'2017-11-13 22:33:28',NULL),(9,'admin9','pbkdf2:sha256:50000$AtbJZp5T$f1102e9aef9deb5f2266d80b866d79f3edc553443dbf94307fdf9580f1fdef96',1,'2017-11-13 22:33:28',NULL),(10,'admin99','pbkdf2:sha256:50000$v1ng0565$0460ee172502c499e3d39d433fb9d55a35602baa004354170ee8084781658af3',1,'2017-11-15 19:40:45',3);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `adminlog`
--

DROP TABLE IF EXISTS `adminlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `adminlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `admin_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_adminlog_addtime` (`addtime`),
  CONSTRAINT `adminlog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `adminlog`
--

LOCK TABLES `adminlog` WRITE;
/*!40000 ALTER TABLE `adminlog` DISABLE KEYS */;
/*!40000 ALTER TABLE `adminlog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth`
--

DROP TABLE IF EXISTS `auth`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `url` (`url`),
  KEY `ix_auth_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth`
--

LOCK TABLES `auth` WRITE;
/*!40000 ALTER TABLE `auth` DISABLE KEYS */;
INSERT INTO `auth` VALUES (2,'标签添加','/admin/tag/add/','2017-11-15 14:32:04'),(3,'标签列表','/admin/tag/list/<int:page>/','2017-11-15 14:32:18'),(4,'电影添加','/admin/movie/add/','2017-11-15 14:32:51'),(5,'电影列表','/admin/movie/list/<int:page>/','2017-11-15 14:33:05'),(6,'标签编辑','/admin/tag/edit/<int:id>/','2017-11-15 20:27:22'),(7,'电影编辑','/admin/movie/edit/<int:id>/','2017-11-15 20:32:26'),(8,'预告添加','/admin/preview/add/','2017-11-15 20:33:01'),(9,'预告列表','/admin/preview/list/<int:page>/','2017-11-15 20:33:40'),(10,'预告编辑','/admin/preview/edit/<int:id>/','2017-11-15 20:34:21'),(11,'标签删除','/admin/tag/delete/<int:id>/','2017-11-15 20:37:09'),(12,'电影删除','/admin/movie/delete/<int:id>/','2017-11-15 20:38:42'),(13,'预告删除','/admin/preview/delete/<int:id>/','2017-11-15 20:40:13'),(14,'会员列表','/admin/user/list/<int:page>/','2017-11-15 20:40:56'),(15,'会员删除','/admin/user/delete/<int:id>/','2017-11-15 20:41:14'),(16,'会员查看','/admin/user/view/<int:id>/','2017-11-15 20:41:37'),(17,'评论列表','/admin/comment/list/<int:page>/','2017-11-15 20:42:50'),(18,'评论删除','/admin/comment/delete/<int:id>/','2017-11-15 20:43:05'),(19,'电影收藏删除','/admin/moviecol/delete/<int:id>/','2017-11-15 20:43:46'),(20,'电影收藏列表','/admin/moviecol/list/<int:page>/','2017-11-15 20:44:47'),(21,'操作日志列表','/admin/optlogl/list/<int:page>/','2017-11-15 20:45:28'),(22,'管理员登录日志列表','/admin/adminloginlog/list/<int:page>/','2017-11-15 20:46:03'),(23,'会员登录日志列表','/admin/userloginlog/list/<int:page>/','2017-11-15 20:46:27'),(24,'权限列表','/admin/auth/list/<int:page>/','2017-11-15 20:47:01'),(25,'角色列表','/admin/role/list/<int:page>/','2017-11-15 20:47:39'),(26,'管理员列表','/admin/administrator/list/<int:page>/','2017-11-15 20:48:04'),(27,'添加权限','/admin/auth/add/','2017-11-15 20:48:29'),(28,'添加角色','/admin/role/add/','2017-11-15 20:48:42'),(29,'添加管理员','/admin/administor/add/','2017-11-15 20:48:56'),(30,'删除权限','/admin/auth/delete/<int:id>/','2017-11-15 20:49:29'),(31,'删除角色','/admin/role/delete/<int:id>/','2017-11-15 20:49:46'),(32,'删除管理员','/admin/administor/delete/<int:id>/','2017-11-15 20:50:02'),(33,'权限编辑','/admin/auth/edit/<int:id>/','2017-11-15 20:50:49'),(34,'角色编辑','/admin/role/edit/<int:id>/','2017-11-15 20:51:04');
/*!40000 ALTER TABLE `auth` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `comment`
--

DROP TABLE IF EXISTS `comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `addtime` datetime DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_comment_addtime` (`addtime`),
  CONSTRAINT `comment_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`),
  CONSTRAINT `comment_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=104 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `comment`
--

LOCK TABLES `comment` WRITE;
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` VALUES (58,'this is user1\'s comment','2017-11-15 12:40:41',6,14),(59,'this is user2\'s comment','2017-11-15 12:40:41',6,15),(60,'this is user3\'s comment','2017-11-15 12:40:41',6,16),(61,'this is user4\'s comment','2017-11-15 12:40:41',6,17),(62,'this is user5\'s comment','2017-11-15 12:40:41',6,18),(63,'this is user6\'s comment','2017-11-15 12:40:41',6,19),(64,'this is user7\'s comment','2017-11-15 12:40:41',6,20),(65,'this is user1\'s comment','2017-11-15 12:40:41',7,14),(66,'this is user2\'s comment','2017-11-15 12:40:41',7,15),(67,'this is user3\'s comment','2017-11-15 12:40:41',7,16),(68,'this is user4\'s comment','2017-11-15 12:40:41',7,17),(69,'this is user5\'s comment','2017-11-15 12:40:41',7,18),(70,'this is user6\'s comment','2017-11-15 12:40:41',7,19),(71,'this is user7\'s comment','2017-11-15 12:40:41',7,20),(72,'this is user1\'s comment','2017-11-15 12:40:41',8,14),(73,'this is user2\'s comment','2017-11-15 12:40:41',8,15),(74,'this is user3\'s comment','2017-11-15 12:40:41',8,16),(75,'this is user4\'s comment','2017-11-15 12:40:41',8,17),(76,'this is user5\'s comment','2017-11-15 12:40:41',8,18),(77,'this is user6\'s comment','2017-11-15 12:40:41',8,19),(79,'this is user1\'s comment','2017-11-15 12:40:41',9,14),(80,'this is user2\'s comment','2017-11-15 12:40:41',9,15),(81,'this is user3\'s comment','2017-11-15 12:40:41',9,16),(82,'this is user4\'s comment','2017-11-15 12:40:41',9,17),(83,'this is user5\'s comment','2017-11-15 12:40:41',9,18),(86,'<p>好看</p>','2017-11-16 14:12:28',7,29),(87,'<p>好看</p>','2017-11-16 14:12:43',7,29),(88,'<p>好看</p>','2017-11-16 14:12:47',7,29),(89,'<p>不可</p>','2017-11-16 14:20:23',7,29),(90,'<p>不可</p>','2017-11-16 14:22:59',7,29),(91,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>','2017-11-16 14:23:46',8,29),(92,'<p>好呀</p>','2017-11-16 23:05:36',7,14),(93,'<p>好</p>','2017-11-16 23:22:04',7,14),(94,'<p>好</p>','2017-11-16 23:30:05',7,14),(95,'<p>好</p>','2017-11-16 23:30:24',7,14),(96,'<p>好的</p>','2017-11-16 23:30:31',7,14),(97,'<p>扽扽</p>','2017-11-16 23:31:08',7,14),(98,'<p>光放</p>','2017-11-16 23:32:17',7,14),(99,'<p>东拐</p>','2017-11-16 23:33:26',7,14),(100,'<p>alert(&#39;你好呀&#39;)</p>','2017-11-16 23:37:44',7,14),(101,'<p>&lt;script&gt;alert(&#39;你好呀&#39;)&lt;/script&gt;<br/></p>','2017-11-21 20:45:15',7,14),(102,'<p>&lt;script&gt;alert(1)&lt;/script&gt;</p>','2017-11-21 20:48:31',7,14),(103,'<p><img src=\"http://img.baidu.com/hi/jx2/j_0002.gif\"/></p>','2017-11-21 20:48:43',7,14);
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movie`
--

DROP TABLE IF EXISTS `movie`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movie` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `info` text,
  `logo` varchar(255) DEFAULT NULL,
  `star` smallint(6) DEFAULT NULL,
  `playnum` bigint(20) DEFAULT NULL,
  `commentnum` bigint(20) DEFAULT NULL,
  `area` varchar(255) DEFAULT NULL,
  `release_time` date DEFAULT NULL,
  `length` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `tag_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `url` (`url`),
  UNIQUE KEY `logo` (`logo`),
  KEY `tag_id` (`tag_id`),
  KEY `ix_movie_addtime` (`addtime`),
  CONSTRAINT `movie_ibfk_1` FOREIGN KEY (`tag_id`) REFERENCES `tag` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movie`
--

LOCK TABLES `movie` WRITE;
/*!40000 ALTER TABLE `movie` DISABLE KEYS */;
INSERT INTO `movie` VALUES (6,'变形金刚5','20171114144809d31ce991293c45ecb92a8390eadbe3a4.ifox','该片讲述了地球陷入毁灭危机，以凯德·伊格尔为首的人类反抗小组，与汽车人联手反击霸天虎在内的入侵者的故事。','201711141328006e9d4bfba1bb4c179fb6c3c21ffb97f6.jpg',3,1,0,'美国','2017-11-22','5','2017-11-14 13:28:00',2),(7,'天才枪手','201711141330393711f8d50f8c4b4fb98905446a8de9ea.mp4','影片根据2014年轰动一时的亚洲考场作弊案改编','20171114133039ef97d4c736b347feb258de9dc3962a9d',3,60,24,'泰国','2017-11-15','5','2017-11-14 13:30:40',16),(8,'缝纫机乐队','20171114144937c6b417c84aea43258e79f8fdd4572d10.mp4','《缝纫机乐队》是由上海儒意影业、霍尔果斯青春光线影业、万达影业出品，由大鹏（董成鹏）执导，大鹏、乔杉、娜扎、李鸿其、韩童生、曲隽希等主演的喜剧电影。影片讲述摇滚青年胡亮散尽家财请来乐队经纪人程宫，组建“缝纫机乐队”，试图保住“摇滚公园”的故事。','20171114133847a7ab165f57254aad8c9273c5a97a9694',2,2,0,'中国','2017-11-16','4','2017-11-14 13:38:47',16),(9,'变形金刚','2017111420534682ad96907597469983b3d8cf99602833.mp4','风横','20171114201148518a3108a5fa4792abe80422183a669f.jpg',1,1,0,'扽','2017-11-28','43','2017-11-14 20:11:49',7),(10,'香港华尔街','201711142138064883c4340b044debae2c193f3df4bb20.mp4','撒扽','20171114213806efdaf9534175404ea82f8ecc7a2c863d.jpg',1,1,0,'中国','2017-11-07','2','2017-11-14 21:38:07',7),(11,'让他跟','2017111422182529481c38962d4bcdac1072ca641986d0.mp4','东方风','201711142218256f2e95f893464f6ea81bfdebd1ce4a4e.jpg',1,1,0,'扥根','2017-11-28','4','2017-11-14 22:18:26',2),(12,'fd','20171114230245ca110a26d2714dd59b2ae949c949c709.mp4','dsgfdg','20171114230245919c9acb92114aed997ecb54e23eecab.jpg',1,1,0,'fghj','2017-11-14','3','2017-11-14 23:02:45',1),(13,'dcv','201711142327378a19b80060a140a197ad4fca1dc7dc58.flv','fdvnc','20171114232737eaef93610be748dcb7ec2a333b4d7cbc.jpg',1,2,0,'dgf','2017-11-21','3','2017-11-14 23:27:38',1);
/*!40000 ALTER TABLE `movie` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `moviecol`
--

DROP TABLE IF EXISTS `moviecol`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `moviecol` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `addtime` datetime DEFAULT NULL,
  `movie_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `movie_id` (`movie_id`),
  KEY `user_id` (`user_id`),
  KEY `ix_moviecol_addtime` (`addtime`),
  CONSTRAINT `moviecol_ibfk_1` FOREIGN KEY (`movie_id`) REFERENCES `movie` (`id`),
  CONSTRAINT `moviecol_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `moviecol`
--

LOCK TABLES `moviecol` WRITE;
/*!40000 ALTER TABLE `moviecol` DISABLE KEYS */;
INSERT INTO `moviecol` VALUES (1,'2017-11-15 13:52:30',6,14),(2,'2017-11-15 13:52:30',6,15),(3,'2017-11-15 13:52:30',6,16),(4,'2017-11-15 13:52:30',7,14),(5,'2017-11-15 13:52:30',7,15),(6,'2017-11-15 13:52:30',7,16),(7,'2017-11-15 13:52:30',8,14),(9,'2017-11-15 13:52:30',8,16),(10,'2017-11-15 13:52:30',9,14),(11,'2017-11-15 13:52:30',9,15),(13,'2017-11-16 14:20:31',7,29);
/*!40000 ALTER TABLE `moviecol` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oplog`
--

DROP TABLE IF EXISTS `oplog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oplog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(600) DEFAULT NULL,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `admin_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `admin_id` (`admin_id`),
  KEY `ix_oplog_addtime` (`addtime`),
  CONSTRAINT `oplog_ibfk_1` FOREIGN KEY (`admin_id`) REFERENCES `admin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oplog`
--

LOCK TABLES `oplog` WRITE;
/*!40000 ALTER TABLE `oplog` DISABLE KEYS */;
/*!40000 ALTER TABLE `oplog` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preview`
--

DROP TABLE IF EXISTS `preview`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `preview` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(255) DEFAULT NULL,
  `logo` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `logo` (`logo`),
  KEY `ix_preview_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preview`
--

LOCK TABLES `preview` WRITE;
/*!40000 ALTER TABLE `preview` DISABLE KEYS */;
INSERT INTO `preview` VALUES (2,'dfhgdfhg','2017111423105674a6bc3283964d6e8980e7461c4a39df','2017-11-14 23:10:56'),(3,'变形金刚5','2017111510502889fc7b35327e4032b1cf42e082c4e856','2017-11-15 10:17:52'),(4,'扽广丰','20171115102327174a4c9f6d51476b812a5f019726e507.jpg','2017-11-15 10:23:28');
/*!40000 ALTER TABLE `preview` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `role`
--

DROP TABLE IF EXISTS `role`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `role` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `auths` varchar(600) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_role_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `role`
--

LOCK TABLES `role` WRITE;
/*!40000 ALTER TABLE `role` DISABLE KEYS */;
INSERT INTO `role` VALUES (2,'超级管理员','2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34','2017-11-13 22:33:27'),(3,'标签管理员','2,3,4,5','2017-11-15 14:43:15'),(4,'电影管理员','4,5','2017-11-15 15:53:43');
/*!40000 ALTER TABLE `role` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tag`
--

DROP TABLE IF EXISTS `tag`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tag` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `ix_tag_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tag`
--

LOCK TABLES `tag` WRITE;
/*!40000 ALTER TABLE `tag` DISABLE KEYS */;
INSERT INTO `tag` VALUES (1,'爱情','2017-11-14 08:59:43'),(2,'科幻','2017-11-14 09:00:09'),(7,'动作','2017-11-14 09:08:00'),(16,'现实','2017-11-14 13:28:10');
/*!40000 ALTER TABLE `tag` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `pwd` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phone` varchar(11) DEFAULT NULL,
  `info` text,
  `face` varchar(255) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `uuid` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`),
  UNIQUE KEY `face` (`face`),
  UNIQUE KEY `uuid` (`uuid`),
  KEY `ix_user_addtime` (`addtime`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (14,'User1','pbkdf2:sha256:50000$FeNFkiSh$ed166322d25e000b48c6ddbd0ebe570e7f02198bbf582128a091a06cf434007a','982492401@qq.com','13928739101','我是User1','0001.png','2017-11-15 11:44:27','3a1521e905ec436f833696aa3455eb21'),(15,'User2','pbkdf2:sha256:50000$cYPRtqxy$bbc574631439036ef4e56e06a516a4f35e0518ac305cc18f109eec8769f95d6a','982492402@qq.com','13928739102','我是User2','0002.png','2017-11-15 11:44:28','2821d441d7104d919bb2acf0d7cca27c'),(16,'User3','pbkdf2:sha256:50000$WBnsQKIZ$9d9f75b60fd3ca90b342393d0452c0d50b4854c1f0180c16e5646111e3c3e76f','982492403@qq.com','13928739103','我是User3','0003.png','2017-11-15 11:44:28','aa1a271932e4435c884cb05cea6ba253'),(17,'User4','pbkdf2:sha256:50000$NM5Q12e0$364f8e61d8c70f04c77b3e801802edcc7930d793596d1ec792737c4a388ecaf1','982492404@qq.com','13928739104','我是User4','0004.png','2017-11-15 11:44:28','46d99f111493449c99b423be9bb87c89'),(18,'User5','pbkdf2:sha256:50000$PJ681lyQ$f2e8890a44a39ac501cf75d3f928d4ed0b50d8570e5927f71198fa2e4c3b4ca5','982492405@qq.com','13928739105','我是User5','0005.png','2017-11-15 11:44:28','e5f65530a2eb4f3484a8dcca42677f33'),(19,'User6','pbkdf2:sha256:50000$gZrwU6RN$db9933594a66994d7b4fff4c55d11433ef94787d00d8a3b98395c12d0cd8596c','982492406@qq.com','13928739106','我是User6','0006.png','2017-11-15 11:44:28','e286786bf46641cb9d66c806ba949bb2'),(20,'User7','pbkdf2:sha256:50000$anwoN3vK$d6b6dc30b4aa75527b00688321c2fa9e74a9628368edafe91cec43739ac91559','982492407@qq.com','13928739107','我是User7','0007.png','2017-11-15 11:44:28','81c9069e3b494d82b3858a1f2ddabc08'),(21,'User8','pbkdf2:sha256:50000$Sh9VuX1T$4cb9d98c7d5bb5c2888d93aa1f124be50b0fd3488f9cab5a73fcc3b88340dc85','982492408@qq.com','13928739108','我是User8','0008.png','2017-11-15 11:44:28','a460d8212ed54441b3a2f3868d11f19a'),(22,'User9','pbkdf2:sha256:50000$XbVrDKgk$8e99aa94fb2f3649f674f8bc46a810be1e90ba96070714a03635deabeb93b4a4','982492409@qq.com','13928739109','我是User9','0009.png','2017-11-15 11:44:28','0bc9d266a0384c00adb87a44bda6cc6a'),(24,'User11','pbkdf2:sha256:50000$GrghikTF$ba2290c962e08bd70f9acccf42e6a62138698d398da7768fc84e668990c7e7cd','982492411@qq.com','13928739111','我是User11','0011.png','2017-11-15 11:44:29','5014c01d2a814c41a44a25df0aad7390'),(25,'User12','pbkdf2:sha256:50000$N4qUs1Wn$6dde5089afa4ddea3f8e1c7d89fb335be50a6516cd5aebf1316b608bbc5e4c8f','982492412@qq.com','13928739112','我是User12','0012.png','2017-11-15 11:44:29','38c12775a7354ab4a83b1f27431da671'),(26,'hex','pbkdf2:sha256:50000$Kl8G6Wjx$55841b40b41d55afa28b2981620c433bca9a03b59430d39fb8b3ab9b7aa74192','982492477@qq.com','13928739114','','','2017-11-15 21:58:31','b227fcb044454ea2a42f4b558192bfea'),(29,'hex123','pbkdf2:sha256:50000$WV5NH145$9a2f6a2f845c8d4587c34b95441f1acd6710291b90728870383b2f9db55708f9','982492433@qq.com','15096009304','你好呀！','20171115225754ecbec54ea3b04a55b133ac454939e37b.jpg','2017-11-15 22:53:30','a79de5403be04f3b9b821051522886e8');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userlog`
--

DROP TABLE IF EXISTS `userlog`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `userlog` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ip` varchar(100) DEFAULT NULL,
  `addtime` datetime DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `ix_userlog_addtime` (`addtime`),
  CONSTRAINT `userlog_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userlog`
--

LOCK TABLES `userlog` WRITE;
/*!40000 ALTER TABLE `userlog` DISABLE KEYS */;
INSERT INTO `userlog` VALUES (1,'127.0.0.1','2017-11-15 21:59:27',26),(2,'127.0.0.1','2017-11-15 22:49:31',26),(3,'127.0.0.1','2017-11-15 22:53:40',29),(4,'127.0.0.1','2017-11-16 14:11:55',29),(5,'127.0.0.1','2017-11-16 23:05:22',14),(6,'127.0.0.1','2017-11-16 23:21:54',14),(7,'127.0.0.1','2017-11-21 20:44:33',14);
/*!40000 ALTER TABLE `userlog` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-11-21  4:56:22
