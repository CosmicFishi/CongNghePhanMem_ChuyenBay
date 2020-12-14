-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

DROP TABLE IF EXISTS `airport`;
CREATE TABLE `airport` (
  `id` int NOT NULL AUTO_INCREMENT,
  `place` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `airport_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `image` varchar(300) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `airport` (`id`, `place`, `airport_name`, `image`) VALUES
(1,	'TP. HCM',	'Tân Sơn Nhất',	'/images/airport/Ho-Chi-Minh-City-SGN.jpg'),
(2,	'Huế',	'Phú Bài',	'/images/airport/Hue-HUI.jpg'),
(3,	'Trà Vinh',	'Trà Vinh',	'/images/airport/Vinh-VII.jpg'),
(4,	'Kiên Giang',	'Phú Quốc',	'/images/airport/Phu-Quoc-PQC.jpg'),
(5,	'Hải Phòng',	'Kiến An',	'/images/airport/Hai-Phong-HPH.jpg'),
(6,	'Đà Nẵng',	'Đà Nẵng',	'/images/airport/Da-Nang-DAD.jpg'),
(7,	'Lâm Đồng',	'Liên Khương',	'/images/airport/Da-Lat-DLI.jpg');

DROP TABLE IF EXISTS `customer`;
CREATE TABLE `customer` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `account_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `password` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `type_user` enum('USER','ADMIN','STAFF') CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `id_card` varchar(12) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(11) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `active` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `customer_chk_1` CHECK ((`active` in (0,1)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `customer` (`id`, `user_name`, `account_name`, `password`, `type_user`, `id_card`, `phone`, `active`) VALUES
(1,	'haungo',	'Ngo Van Hau',	'202cb962ac59075b964b07152d234b70',	'ADMIN',	'000011111',	'012345678',	1),
(2,	'a',	'Nguyen van A',	'202cb962ac59075b964b07152d234b70',	'USER',	'025651545',	'0383793',	1),
(3,	'b',	'Nguyen Van B',	'202cb962ac59075b964b07152d234b70',	'USER',	'285704152',	'0325648122',	1);

DROP TABLE IF EXISTS `flight`;
CREATE TABLE `flight` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plane_id` int DEFAULT NULL,
  `flight_from` int NOT NULL,
  `flight_to` int NOT NULL,
  `time_start` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `flight_time` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY (`id`),
  KEY `plane_id` (`plane_id`),
  KEY `flight_from` (`flight_from`),
  KEY `flight_to` (`flight_to`),
  CONSTRAINT `flight_ibfk_1` FOREIGN KEY (`plane_id`) REFERENCES `plane` (`id`),
  CONSTRAINT `flight_ibfk_2` FOREIGN KEY (`flight_from`) REFERENCES `airport` (`id`),
  CONSTRAINT `flight_ibfk_3` FOREIGN KEY (`flight_to`) REFERENCES `airport` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `flight` (`id`, `plane_id`, `flight_from`, `flight_to`, `time_start`, `flight_time`) VALUES
(1,	1,	2,	1,	'2020-12-19 23:06:00',	'0130'),
(2,	1,	1,	2,	'2020-12-23 23:09:00',	'0130'),
(3,	2,	4,	3,	'2020-12-21 23:09:00',	'0150'),
(4,	2,	2,	4,	'2020-12-24 23:09:00',	'0200'),
(5,	2,	1,	3,	'2020-12-25 23:11:00',	'0130'),
(6,	3,	2,	1,	'2020-12-24 23:11:00',	'0130');

DROP TABLE IF EXISTS `intermediate_airport`;
CREATE TABLE `intermediate_airport` (
  `flight_id` int NOT NULL,
  `id` int DEFAULT NULL,
  `time_layover` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `order` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `note` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`flight_id`),
  KEY `id` (`id`),
  CONSTRAINT `intermediate_airport_ibfk_1` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`id`),
  CONSTRAINT `intermediate_airport_ibfk_2` FOREIGN KEY (`id`) REFERENCES `airport` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `intermediate_airport` (`flight_id`, `id`, `time_layover`, `order`, `note`) VALUES
(1,	5,	'0015',	'0',	'trong lúc dừng chỉ được ngồi trong máy bay');

DROP TABLE IF EXISTS `plane`;
CREATE TABLE `plane` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plane_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  `airlines` varchar(50) CHARACTER SET utf8 COLLATE utf8_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `plane` (`id`, `plane_name`, `airlines`) VALUES
(1,	'ATK 23',	'Dung Hau'),
(2,	'ATK 45',	'Vietnam Airlines 1'),
(3,	'MKR 89',	'Vietnam Airlines 2'),
(4,	'TY 4',	'Vietnam Airlines 3'),
(5,	'TY 5',	'Vietnam Airlines 4'),
(6,	'MB 5',	'Vietjet Air 1'),
(7,	'MB 78',	'Vietjet Air 2'),
(8,	'HU 9',	'Vietjet Air 3'),
(9,	'HU 10',	'Vietjet Air 4'),
(10,	'HU 12',	'Jetstar Pacific 1'),
(11,	'HU 15',	'Jetstar Pacific 2'),
(12,	'JI 7',	'Jetstar Pacific 3'),
(13,	'JI 10',	'Jetstar Pacific 4'),
(14,	'KHU 5',	'Bamboo Airways 1'),
(15,	'HAU 7',	'Bamboo Airways 2'),
(16,	'DUNG 7',	'Bamboo Airways 3'),
(17,	'AHIHI',	'Bamboo Airways 4');

DROP TABLE IF EXISTS `scheduled`;
CREATE TABLE `scheduled` (
  `flight_id` int NOT NULL,
  `customer_id` int NOT NULL,
  `seat_type_id` int NOT NULL,
  `count_seat` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `price` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `is_used` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`flight_id`,`customer_id`,`seat_type_id`),
  KEY `customer_id` (`customer_id`),
  KEY `seat_type_id` (`seat_type_id`),
  CONSTRAINT `scheduled_ibfk_1` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`id`),
  CONSTRAINT `scheduled_ibfk_2` FOREIGN KEY (`customer_id`) REFERENCES `customer` (`id`),
  CONSTRAINT `scheduled_ibfk_3` FOREIGN KEY (`seat_type_id`) REFERENCES `seat_type` (`id`),
  CONSTRAINT `scheduled_chk_1` CHECK ((`is_used` in (0,1)))
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `scheduled` (`flight_id`, `customer_id`, `seat_type_id`, `count_seat`, `price`, `is_used`) VALUES
(1,	2,	1,	'2',	'200',	0);

DROP TABLE IF EXISTS `seat_type`;
CREATE TABLE `seat_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `plane_id` int DEFAULT NULL,
  `seat_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_unicode_ci NOT NULL,
  `row_from` int NOT NULL,
  `row_to` int NOT NULL,
  `amount_of_row` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `plane_id` (`plane_id`),
  CONSTRAINT `seat_type_ibfk_1` FOREIGN KEY (`plane_id`) REFERENCES `plane` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

INSERT INTO `seat_type` (`id`, `plane_id`, `seat_name`, `row_from`, `row_to`, `amount_of_row`) VALUES
(1,	1,	'Ghế thương gia',	1,	8,	4),
(2,	1,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(3,	1,	'Ghế phổ thông',	14,	20,	8),
(4,	2,	'Ghế thương gia',	1,	8,	4),
(5,	2,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(6,	2,	'Ghế phổ thông',	14,	20,	8),
(7,	3,	'Ghế thương gia',	1,	8,	4),
(8,	3,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(9,	3,	'Ghế phổ thông',	14,	20,	8),
(10,	4,	'Ghế thương gia',	1,	8,	4),
(11,	4,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(12,	4,	'Ghế phổ thông',	14,	20,	8),
(13,	5,	'Ghế thương gia',	1,	8,	4),
(14,	5,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(15,	5,	'Ghế phổ thông',	14,	20,	8),
(16,	6,	'Ghế thương gia',	1,	8,	4),
(17,	6,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(18,	6,	'Ghế phổ thông',	14,	20,	8);

-- 2020-12-14 02:54:37
