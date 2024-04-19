/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 8.0.33 : Database - bloodbank
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`bloodbank` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

USE `bloodbank`;

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values 
(1,'Can add log entry',1,'add_logentry'),
(2,'Can change log entry',1,'change_logentry'),
(3,'Can delete log entry',1,'delete_logentry'),
(4,'Can view log entry',1,'view_logentry'),
(5,'Can add permission',2,'add_permission'),
(6,'Can change permission',2,'change_permission'),
(7,'Can delete permission',2,'delete_permission'),
(8,'Can view permission',2,'view_permission'),
(9,'Can add group',3,'add_group'),
(10,'Can change group',3,'change_group'),
(11,'Can delete group',3,'delete_group'),
(12,'Can view group',3,'view_group'),
(13,'Can add user',4,'add_user'),
(14,'Can change user',4,'change_user'),
(15,'Can delete user',4,'delete_user'),
(16,'Can view user',4,'view_user'),
(17,'Can add content type',5,'add_contenttype'),
(18,'Can change content type',5,'change_contenttype'),
(19,'Can delete content type',5,'delete_contenttype'),
(20,'Can view content type',5,'view_contenttype'),
(21,'Can add session',6,'add_session'),
(22,'Can change session',6,'change_session'),
(23,'Can delete session',6,'delete_session'),
(24,'Can view session',6,'view_session'),
(25,'Can add blood_table',7,'add_blood_table'),
(26,'Can change blood_table',7,'change_blood_table'),
(27,'Can delete blood_table',7,'delete_blood_table'),
(28,'Can view blood_table',7,'view_blood_table'),
(29,'Can add hospital_table',8,'add_hospital_table'),
(30,'Can change hospital_table',8,'change_hospital_table'),
(31,'Can delete hospital_table',8,'delete_hospital_table'),
(32,'Can view hospital_table',8,'view_hospital_table'),
(33,'Can add login_table',9,'add_login_table'),
(34,'Can change login_table',9,'change_login_table'),
(35,'Can delete login_table',9,'delete_login_table'),
(36,'Can view login_table',9,'view_login_table'),
(37,'Can add user_table',10,'add_user_table'),
(38,'Can change user_table',10,'change_user_table'),
(39,'Can delete user_table',10,'delete_user_table'),
(40,'Can view user_table',10,'view_user_table'),
(41,'Can add request_table',11,'add_request_table'),
(42,'Can change request_table',11,'change_request_table'),
(43,'Can delete request_table',11,'delete_request_table'),
(44,'Can view request_table',11,'view_request_table'),
(45,'Can add feedback_table',12,'add_feedback_table'),
(46,'Can change feedback_table',12,'change_feedback_table'),
(47,'Can delete feedback_table',12,'delete_feedback_table'),
(48,'Can view feedback_table',12,'view_feedback_table'),
(49,'Can add complaint_table',13,'add_complaint_table'),
(50,'Can change complaint_table',13,'change_complaint_table'),
(51,'Can delete complaint_table',13,'delete_complaint_table'),
(52,'Can view complaint_table',13,'view_complaint_table'),
(53,'Can add blood_bank_table',14,'add_blood_bank_table'),
(54,'Can change blood_bank_table',14,'change_blood_bank_table'),
(55,'Can delete blood_bank_table',14,'delete_blood_bank_table'),
(56,'Can view blood_bank_table',14,'view_blood_bank_table'),
(57,'Can add response_table',15,'add_response_table'),
(58,'Can change response_table',15,'change_response_table'),
(59,'Can delete response_table',15,'delete_response_table'),
(60,'Can view response_table',15,'view_response_table');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values 
(1,'pbkdf2_sha256$260000$Nx4aZ6YcH7w9Z5V5K0g0ev$+QCFp711rmAsjDz3bp4HkMhKdGeuQUHr29VngapIAmQ=','2024-01-27 08:30:12.448542',1,'abc','','','abc@gmail.com',1,1,'2024-01-02 08:28:02.353441');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `blood_blood_bank_table` */

DROP TABLE IF EXISTS `blood_blood_bank_table`;

CREATE TABLE `blood_blood_bank_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phonno` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blood_blood_bank_table_LOGIN_id_bee95522_fk_blood_login_table_id` (`LOGIN_id`),
  KEY `blood_blood_bank_tab_HOSPITAL_id_e9e11d78_fk_blood_hos` (`HOSPITAL_id`),
  CONSTRAINT `blood_blood_bank_tab_HOSPITAL_id_e9e11d78_fk_blood_hos` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `blood_hospital_table` (`id`),
  CONSTRAINT `blood_blood_bank_table_LOGIN_id_bee95522_fk_blood_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `blood_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_blood_bank_table` */

insert  into `blood_blood_bank_table`(`id`,`name`,`place`,`post`,`pin`,`phonno`,`email`,`LOGIN_id`,`HOSPITAL_id`) values 
(1,'yadav','kozhikode','kkt',251365,1001001001,'vishnunarayanansreelayam@gmail.com',8,1),
(2,'ftyyg','dfgh','dfghj',85225,5678987,'dfghjklkloughuttf7t',7,1),
(3,'Adwaid K','kkkh','l0oo=-o',12582,85256,'5ftgyhujikolp;\'',15,1),
(4,'Adwaid K','kkkh','l0oo=-o',12582,85256,'hdfghjk;@gmail.com',16,1),
(5,'jjutu','eyy','teeyte',673322,665324566,'vishnunarayanansreelayam@gmail.com',20,1),
(6,'ghgj','hvjh','hhjl',456,8078422753,'vishnunarayanansreelayam@gmail.com',22,1),
(7,'ghgj','hvjh','hhjl',456,8078422753,'vishnunarayanansreelayam@gmail.com',23,1),
(8,'ghgj','hvjh','hhjl',630215,1234567890,'vishnunarayanansreelayam@gmail.com',27,1),
(9,'karth','ayancheri','kakkkatil',125820,8078422753,'vishnunarayanansreelayam@gmail.com',28,1),
(10,'vnfdjv','fbdfb','ggdf',986755,9876543211,'dcvds@gmail.com',29,1),
(11,'sadfghjk','zsdfghjk','sdfghjk',345678,7890678906,'asdfghjkl@gjh',31,1),
(12,'bmhbb','calicut','calicut',673004,8765432190,'bmhbb@gmail.com',34,15);

/*Table structure for table `blood_blood_table` */

DROP TABLE IF EXISTS `blood_blood_table`;

CREATE TABLE `blood_blood_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `bloodgroup` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `details` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_blood_table` */

insert  into `blood_blood_table`(`id`,`bloodgroup`,`date`,`details`) values 
(2,'b-','2024-01-10','good conitionhh');

/*Table structure for table `blood_complaint_table` */

DROP TABLE IF EXISTS `blood_complaint_table`;

CREATE TABLE `blood_complaint_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `complaint` varchar(300) NOT NULL,
  `replay` varchar(300) NOT NULL,
  `date` date NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blood_complaint_tabl_HOSPITAL_id_70a55f07_fk_blood_hos` (`HOSPITAL_id`),
  KEY `blood_complaint_table_USER_id_0364ad83_fk_blood_user_table_id` (`USER_id`),
  CONSTRAINT `blood_complaint_tabl_HOSPITAL_id_70a55f07_fk_blood_hos` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `blood_hospital_table` (`id`),
  CONSTRAINT `blood_complaint_table_USER_id_0364ad83_fk_blood_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `blood_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_complaint_table` */

insert  into `blood_complaint_table`(`id`,`complaint`,`replay`,`date`,`HOSPITAL_id`,`USER_id`) values 
(2,'ggfgfh','dgh','2024-01-10',13,2);

/*Table structure for table `blood_feedback_table` */

DROP TABLE IF EXISTS `blood_feedback_table`;

CREATE TABLE `blood_feedback_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `feedback` varchar(100) NOT NULL,
  `date` date NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blood_feedback_table_HOSPITAL_id_bbf78572_fk_blood_hos` (`HOSPITAL_id`),
  KEY `blood_feedback_table_USER_id_a10e81c6_fk_blood_user_table_id` (`USER_id`),
  CONSTRAINT `blood_feedback_table_HOSPITAL_id_bbf78572_fk_blood_hos` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `blood_hospital_table` (`id`),
  CONSTRAINT `blood_feedback_table_USER_id_a10e81c6_fk_blood_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `blood_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_feedback_table` */

/*Table structure for table `blood_hospital_table` */

DROP TABLE IF EXISTS `blood_hospital_table`;

CREATE TABLE `blood_hospital_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `latitude` double NOT NULL,
  `longitude` double NOT NULL,
  `phonno` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blood_hospital_table_LOGIN_id_d62807e3_fk_blood_login_table_id` (`LOGIN_id`),
  CONSTRAINT `blood_hospital_table_LOGIN_id_d62807e3_fk_blood_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `blood_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_hospital_table` */

insert  into `blood_hospital_table`(`id`,`name`,`place`,`post`,`pin`,`latitude`,`longitude`,`phonno`,`email`,`LOGIN_id`) values 
(1,'hohhbb','fghoo','hhjl',112365,40,75,312654126,'vishnunarayanansreelayam@gmail.com',7),
(2,'ghgj','hvjh','yuyiuh',456,546,787,56454555,'vishnunarayanansreelayam@gmail.com',10),
(3,'ghgj','hvjh','yuyiuh',456,546,787,56454555,'vishnunarayanansreelayam@gmail.com',11),
(4,'ghgj','hvjh','yuyiuh',456,546,787,56454555,'vishnunarayanansreelayam@gmail.com',12),
(5,'ghgj','hvjh','yuyiuh',456,546,787,56454555,'vishnunarayanansreelayam@gmail.com',13),
(6,'ghgj','hvjh','yuyiuh',456,546,787,56454555,'vishnunarayanansreelayam@gmail.com',14),
(7,'ghgj','hvjh','yuyiuh',456,546,787,56454555,'vishnunarayanansreelayam@gmail.com',17),
(8,'ghgj','hvjh','yuyiuh',456,546,787,56454555,'vishnunarayanansreelayam@gmail.com',19),
(9,'admin','calicut','chorode',673106,40,75,8078422753,'vishnunarayanansreelayam@gmail.com',21),
(10,'admin','calicut','chorode',673106,40,75,8078422753,'vishnunarayanansreelayam@gmail.com',24),
(11,'admin','calicut','chorode',673106,40,75,12,'vishnunarayanansreelayam@gmail.com',25),
(12,'admin','calicut','chorode',673106,40,75,1203452123,'152463@gmail.com',26),
(13,'dfghjkl','fghjkl','dfghjk',525444,11.2,65.5,3456789088,'dfgh@gmail.com',30),
(14,'ertyu','rtyhuj','dfghjk',525444,11.2,65.5,3456789088,'dfgh@gmail.com',32),
(15,'BMH','Calicut','Calicut',673004,11.2600489,75.7900391,9876543210,'bmh@gmail.com',33);

/*Table structure for table `blood_login_table` */

DROP TABLE IF EXISTS `blood_login_table`;

CREATE TABLE `blood_login_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `password` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_login_table` */

insert  into `blood_login_table`(`id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(7,'ghhgjh','uuiji','block'),
(8,'yadav','12345','blood bank'),
(9,'','','pending'),
(10,'anu','anu','hospital'),
(11,'ygnhg','2222','hospital'),
(12,'ygnhg','2222','hospital'),
(13,'ygnhg','2222','hospital'),
(14,'ygnhg','2222','hospital'),
(15,'adw','adw','blood bank'),
(16,'adw','adw','reject'),
(17,'adw','adw','hospital'),
(18,'','','pending'),
(19,'adw','adw','reject'),
(20,'adw','adw','blood bank'),
(21,'admin123','123admin','hospital'),
(22,'adw','2222','reject'),
(23,'adw','2222','reject'),
(24,'admin123','123admin','reject'),
(25,'admin123','123admin','reject'),
(26,'admin123','123admin','hospital'),
(27,'adw','2222','reject'),
(28,'kaarthu','333','blood bank'),
(29,'df','fd','blood bank'),
(30,'def','def','reject'),
(31,'dfghjk','sdfghjkl;\'','pending'),
(32,'def','def','pending'),
(33,'bmhclt','bmhclt','hospital'),
(34,'bmhbbclt','bmhbbclt','blood bank'),
(35,'u','u','user');

/*Table structure for table `blood_request_table` */

DROP TABLE IF EXISTS `blood_request_table`;

CREATE TABLE `blood_request_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `blood_id` bigint NOT NULL,
  `details` varchar(300) NOT NULL,
  `status` varchar(300) NOT NULL,
  `HOSPITAL_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  `date` date NOT NULL,
  `count` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blood_request_table_HOSPITAL_id_ec74f438_fk_blood_hos` (`HOSPITAL_id`),
  KEY `blood_request_table_USER_id_bf33ffe1_fk_blood_user_table_id` (`USER_id`),
  KEY `blood_request_table_blood_id_e8fbcd0a` (`blood_id`),
  CONSTRAINT `blood_request_table_blood_id_e8fbcd0a_fk_blood_blood_table_id` FOREIGN KEY (`blood_id`) REFERENCES `blood_blood_table` (`id`),
  CONSTRAINT `blood_request_table_HOSPITAL_id_ec74f438_fk_blood_hos` FOREIGN KEY (`HOSPITAL_id`) REFERENCES `blood_hospital_table` (`id`),
  CONSTRAINT `blood_request_table_USER_id_bf33ffe1_fk_blood_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `blood_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_request_table` */

insert  into `blood_request_table`(`id`,`blood_id`,`details`,`status`,`HOSPITAL_id`,`USER_id`,`date`,`count`) values 
(1,2,'dfghjk','pending',15,2,'2024-01-12',3);

/*Table structure for table `blood_response_table` */

DROP TABLE IF EXISTS `blood_response_table`;

CREATE TABLE `blood_response_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `status` varchar(300) NOT NULL,
  `REQUEST_id` bigint NOT NULL,
  `USER_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blood_response_table_REQUEST_id_e74aeadf_fk_blood_req` (`REQUEST_id`),
  KEY `blood_response_table_USER_id_8ebe5743_fk_blood_user_table_id` (`USER_id`),
  CONSTRAINT `blood_response_table_REQUEST_id_e74aeadf_fk_blood_req` FOREIGN KEY (`REQUEST_id`) REFERENCES `blood_request_table` (`id`),
  CONSTRAINT `blood_response_table_USER_id_8ebe5743_fk_blood_user_table_id` FOREIGN KEY (`USER_id`) REFERENCES `blood_user_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_response_table` */

insert  into `blood_response_table`(`id`,`date`,`status`,`REQUEST_id`,`USER_id`) values 
(1,'2024-01-12','Donated',1,3);

/*Table structure for table `blood_user_table` */

DROP TABLE IF EXISTS `blood_user_table`;

CREATE TABLE `blood_user_table` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `firstname` varchar(100) NOT NULL,
  `lastname` varchar(100) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(100) NOT NULL,
  `place` varchar(100) NOT NULL,
  `post` varchar(100) NOT NULL,
  `pin` int NOT NULL,
  `phonno` bigint NOT NULL,
  `email` varchar(100) NOT NULL,
  `BLOOD_id` bigint NOT NULL,
  `LOGIN_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `blood_user_table_BLOOD_id_3805da35_fk_blood_blood_table_id` (`BLOOD_id`),
  KEY `blood_user_table_LOGIN_id_5eb99f77_fk_blood_login_table_id` (`LOGIN_id`),
  CONSTRAINT `blood_user_table_BLOOD_id_3805da35_fk_blood_blood_table_id` FOREIGN KEY (`BLOOD_id`) REFERENCES `blood_blood_table` (`id`),
  CONSTRAINT `blood_user_table_LOGIN_id_5eb99f77_fk_blood_login_table_id` FOREIGN KEY (`LOGIN_id`) REFERENCES `blood_login_table` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `blood_user_table` */

insert  into `blood_user_table`(`id`,`firstname`,`lastname`,`age`,`gender`,`place`,`post`,`pin`,`phonno`,`email`,`BLOOD_id`,`LOGIN_id`) values 
(2,'dfghj','sdfghj',23,'male','gyhij','huij',2552,16553,'hjkl;s',2,12),
(3,'u','u',24,'male','kkm','kkkm',654321,9876543217,'jjjj',2,35);

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values 
(1,'admin','logentry'),
(3,'auth','group'),
(2,'auth','permission'),
(4,'auth','user'),
(14,'blood','blood_bank_table'),
(7,'blood','blood_table'),
(13,'blood','complaint_table'),
(12,'blood','feedback_table'),
(8,'blood','hospital_table'),
(9,'blood','login_table'),
(11,'blood','request_table'),
(15,'blood','response_table'),
(10,'blood','user_table'),
(5,'contenttypes','contenttype'),
(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values 
(1,'contenttypes','0001_initial','2023-10-24 07:48:34.138716'),
(2,'auth','0001_initial','2023-10-24 07:48:34.449650'),
(3,'admin','0001_initial','2023-10-24 07:48:34.540693'),
(4,'admin','0002_logentry_remove_auto_add','2023-10-24 07:48:34.550660'),
(5,'admin','0003_logentry_add_action_flag_choices','2023-10-24 07:48:34.559691'),
(6,'contenttypes','0002_remove_content_type_name','2023-10-24 07:48:34.623416'),
(7,'auth','0002_alter_permission_name_max_length','2023-10-24 07:48:34.659481'),
(8,'auth','0003_alter_user_email_max_length','2023-10-24 07:48:34.685431'),
(9,'auth','0004_alter_user_username_opts','2023-10-24 07:48:34.694431'),
(10,'auth','0005_alter_user_last_login_null','2023-10-24 07:48:34.739808'),
(11,'auth','0006_require_contenttypes_0002','2023-10-24 07:48:34.746090'),
(12,'auth','0007_alter_validators_add_error_messages','2023-10-24 07:48:34.755128'),
(13,'auth','0008_alter_user_username_max_length','2023-10-24 07:48:34.801278'),
(14,'auth','0009_alter_user_last_name_max_length','2023-10-24 07:48:34.846883'),
(15,'auth','0010_alter_group_name_max_length','2023-10-24 07:48:34.877366'),
(16,'auth','0011_update_proxy_permissions','2023-10-24 07:48:34.891362'),
(17,'auth','0012_alter_user_first_name_max_length','2023-10-24 07:48:34.939036'),
(18,'blood','0001_initial','2023-10-24 07:48:35.289268'),
(19,'sessions','0001_initial','2023-10-24 07:48:35.317911'),
(20,'blood','0002_blood_bank_table','2023-12-01 07:26:15.132774'),
(21,'blood','0003_blood_bank_table_hospital','2024-01-12 06:35:47.945481'),
(22,'blood','0004_auto_20240112_1227','2024-01-12 06:58:22.881593'),
(23,'blood','0005_request_table_date','2024-01-12 07:02:38.431227'),
(24,'blood','0006_request_table_count','2024-01-12 07:28:58.064141'),
(25,'blood','0007_response_table','2024-01-12 07:33:55.952795');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values 
('6rfk067ncc1x8nibd2yfqf0y5yp7suh6','eyJiaWQiOjJ9:1rJ7z9:mP1BaxXbc8lKD4tZg6yoyMqEpcoU_cZyc24IaAGx-3E','2024-01-12 08:12:51.821720'),
('n1mo97gl5gih2h3ok0vql22qzrks4lz2','eyJjaWQiOjF9:1rAnyS:umSWvk2LDzPoH9GDZDhVtNqltrhk7LZN5HIKbJJyHpU','2023-12-20 09:13:44.412537'),
('tfrw62jwoaxsfw2rd9ugm7oe4vhmcxdv','.eJxVjsEOgjAQRP-lZ9PQltqtR-98Q7PLbgUlJaFwMv67kHDQ65uZl3mrhNs6pK3KkkZWN2XU5ZcR9i8pR8BPLI9Z93NZl5H0UdFnWnU3s0z3s_snGLAO-1quIaAFoAwmEnLrhXMkE8ibCDsTS2J7y85nsbGx3oOEhtuA4Fx2u3Q6_pnPF7EsOdI:1rTe4q:U1pdwjFZsoWlEf5oMTviuVh076b5MwTl3Y9ILpGtr2o','2024-02-10 08:30:12.454234');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
