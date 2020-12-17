-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP DATABASE IF EXISTS `db`;
CREATE DATABASE `db` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `db`;

DROP TABLE IF EXISTS `admin_properties`;
CREATE TABLE `admin_properties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number_airport` int NOT NULL,
  `min_flight` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `max_intermediate_airport` int NOT NULL,
  `min_time_layover` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `max_time_layover` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  `time_for_cancel_ticket` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `time_for_booking_ticket` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `admin_properties`;
INSERT INTO `admin_properties` (`id`, `number_airport`, `min_flight`, `max_intermediate_airport`, `min_time_layover`, `max_time_layover`, `time_for_cancel_ticket`, `time_for_booking_ticket`) VALUES
(1,	100,	'000030',	10,	'000010',	'000020',	'010000',	'010000');

DROP TABLE IF EXISTS `airport`;
CREATE TABLE `airport` (
  `id` int NOT NULL AUTO_INCREMENT,
  `place` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `airport_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(300) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `airport`;
INSERT INTO `airport` (`id`, `place`, `airport_name`, `image`) VALUES
(1,	'TP HCM',	'Tân Sơn Nhất',	'/images/airport/Ho-Chi-Minh-City-SGN.jpg'),
(2,	'Huế',	'Phú Bài',	'/images/airport/Hue-HUI.jpg'),
(3,	'Trà Vinh',	'Trà Vinh',	'/images/airport/Vinh-VII.jpg'),
(4,	'Kiên Giang',	'Phú Quốc',	'/images/airport/Phu-Quoc-PQC.jpg'),
(5,	'Hải Phòng',	'Kiến An',	'/images/airport/Hai-Phong-HPH.jpg'),
(6,	'Đà Nẵng',	'Đà Nẵng',	'/images/airport/Da-Nang-DAD.jpg'),
(7,	'Lâm Đồng',	'Liên Khương',	'/images/airport/Da-Lat-DLI.jpg');

DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `email` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `account_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `password` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  `type_user` enum('USER','ADMIN','STAFF') COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_card` varchar(12) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(11) COLLATE utf8_unicode_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `customer_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `customer`;
INSERT INTO `customer` (`id`, `user_name`, `email`, `account_name`, `password`, `type_user`, `id_card`, `phone`, `active`) VALUES
(1,	'haungo',	'ngovanhau@gmail.com',	'Ngo Van Hau',	'202cb962ac59075b964b07152d234b70',	'ADMIN',	'000011111',	'012345678',	1),
(2,	'a',	'ngovanhau@gmail.com',	'Nguyen van A',	'202cb962ac59075b964b07152d234b70',	'USER',	'025651545',	'0383793',	1),
(3,	'b',	'ngovanhau@gmail.com',	'Nguyen Van B',	'202cb962ac59075b964b07152d234b70',	'USER',	'285704152',	'0325648122',	1),
(4,	'haungo',	'ngovanhau@gmail.com',	'Hau Ngo',	'202cb962ac59075b964b07152d234b70',	'STAFF',	'123465',	'01235679',	1);

DROP TABLE IF EXISTS `flight`;
CREATE TABLE `flight` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plane_id` int DEFAULT NULL,
  `flight_from` int NOT NULL,
  `flight_to` int NOT NULL,
  `time_start` datetime NOT NULL,
  `flight_time` varchar(10) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `plane_id` (`plane_id`),
  KEY `flight_from` (`flight_from`),
  KEY `flight_to` (`flight_to`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`plane_id`) REFERENCES `plane` (`id`),
  CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`flight_from`) REFERENCES `airport` (`id`),
  CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`flight_to`) REFERENCES `airport` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `flight`;
INSERT INTO `flight` (`id`, `plane_id`, `flight_from`, `flight_to`, `time_start`, `flight_time`) VALUES
(1,	1,	2,	1,	'2020-12-19 23:00:00',	'0130'),
(2,	1,	1,	2,	'2020-12-23 17:30:00',	'0130'),
(3,	2,	4,	3,	'2020-12-21 15:10:00',	'0150'),
(4,	2,	2,	4,	'2020-12-24 12:30:00',	'0200'),
(5,	2,	1,	3,	'2020-12-25 16:15:00',	'0130'),
(6,	3,	2,	1,	'2020-12-24 18:00:00',	'0130'),
(7,	1,	4,	2,	'2020-12-26 07:15:00',	'0300');

DROP TABLE IF EXISTS `intermediate_airport`;
CREATE TABLE `intermediate_airport` (
  `flight_id` int NOT NULL,
  `id` int NOT NULL,
  `time_layover` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `order` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `note` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`flight_id`,`id`),
  KEY `id` (`id`),
  CONSTRAINT `intermediate_airport_ibfk_1` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`id`),
  CONSTRAINT `intermediate_airport_ibfk_2` FOREIGN KEY (`id`) REFERENCES `airport` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `intermediate_airport`;
INSERT INTO `intermediate_airport` (`flight_id`, `id`, `time_layover`, `order`, `note`) VALUES
(1,	5,	'0015',	'0',	'trong lúc dừng chỉ được ngồi trong máy bay'),
(7,	1,	'0030',	'0',	'được xuống máy bay trong 15p'),
(7,	7,	'0015',	'1',	'k xuong may bay');

DROP TABLE IF EXISTS `plane`;
CREATE TABLE `plane` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plane_name` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `airlines` varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `plane`;
INSERT INTO `plane` (`id`, `plane_name`, `airlines`) VALUES
(1,	'ATK 23',	'Dung Hau'),
(2,	'ATK 45',	'Vietnam Airlines 1'),
(3,	'MKR 89',	'Vietnam Airlines 2');

DROP TABLE IF EXISTS `scheduled`;
CREATE TABLE `scheduled` (
  `id` int NOT NULL AUTO_INCREMENT,
  `flight_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `seat_type_id` int NOT NULL,
  `position` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `count_seat` int NOT NULL,
  `price` float NOT NULL,
  `is_used` tinyint(1) DEFAULT NULL,
  `time_create` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `flight_id` (`flight_id`),
  KEY `customer_id` (`customer_id`),
  KEY `seat_type_id` (`seat_type_id`),
  CONSTRAINT `scheduled_ibfk_1` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`id`),
  CONSTRAINT `scheduled_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `scheduled_ibfk_3` FOREIGN KEY (`seat_type_id`) REFERENCES `seat_type` (`id`),
  CONSTRAINT `scheduled_chk_1` CHECK ((`is_used` in (0,1)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `scheduled`;
INSERT INTO `scheduled` (`id`, `flight_id`, `customer_id`, `seat_type_id`, `position`, `count_seat`, `price`, `is_used`, `time_create`) VALUES
(1,	1,	2,	1,	'12,13,90,100,110,120,126',	2,	200,	0,	'2020-12-19 23:06:00'),
(2,	7,	1,	1,	'22,33',	2,	600,	0,	'2020-12-20 23:06:00'),
(3,	7,	3,	2,	'11',	1,	100,	0,	'2020-12-25 23:06:00'),
(4,	2,	2,	1,	'12,13,93,102,111,123,124,222',	2,	20,	NULL,	'2020-12-16 11:03:39');

DROP TABLE IF EXISTS `seat_type`;
CREATE TABLE `seat_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plane_id` int DEFAULT NULL,
  `seat_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `row_from` int NOT NULL,
  `row_to` int NOT NULL,
  `amount_of_row` int NOT NULL,
  `price` float NOT NULL,
  PRIMARY KEY (`id`),
  KEY `plane_id` (`plane_id`),
  CONSTRAINT `seat_type_ibfk_1` FOREIGN KEY (`plane_id`) REFERENCES `plane` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

TRUNCATE `seat_type`;
INSERT INTO `seat_type` (`id`, `plane_id`, `seat_name`, `row_from`, `row_to`, `amount_of_row`, `price`) VALUES
(1,	1,	'ECONOMY',	1,	7,	4,	2),
(2,	1,	'BUSINESS ',	8,	13,	6,	8),
(4,	2,	'ECONOMY',	1,	8,	4,	1),
(5,	2,	'BUSINESS ',	9,	13,	6,	7),
(7,	3,	'ECONOMY',	1,	8,	4,	2),
(8,	3,	'BUSINESS ',	9,	13,	6,	10);

-- 2020-12-16 20:56:56
