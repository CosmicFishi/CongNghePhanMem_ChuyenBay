-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

INSERT INTO `airport` (`id`, `place`, `airport_name`, `image`) VALUES
(1,	'TP HCM',	'Tân Sơn Nhất',	'/images/airport/Ho-Chi-Minh-City-SGN.jpg'),
(2,	'Huế',	'Phú Bài',	'/images/airport/Hue-HUI.jpg'),
(3,	'Trà Vinh',	'Trà Vinh',	'/images/airport/Vinh-VII.jpg'),
(4,	'Kiên Giang',	'Phú Quốc',	'/images/airport/Phu-Quoc-PQC.jpg'),
(5,	'Hải Phòng',	'Kiến An',	'/images/airport/Hai-Phong-HPH.jpg'),
(6,	'Đà Nẵng',	'Đà Nẵng',	'/images/airport/Da-Nang-DAD.jpg'),
(7,	'Lâm Đồng',	'Liên Khương',	'/images/airport/Da-Lat-DLI.jpg');

INSERT INTO `customer` (`id`, `user_name`, `email`, `account_name`, `password`, `type_user`, `id_card`, `phone`, `active`) VALUES
(1,	'haungo',	'ngovanhau@gmail.com',	'Ngo Van Hau',	'202cb962ac59075b964b07152d234b70',	'ADMIN',	'000011111',	'012345678',	1),
(2,	'a',	'ngovanhau@gmail.com',	'Nguyen van A',	'202cb962ac59075b964b07152d234b70',	'USER',	'025651545',	'0383793',	1),
(3,	'b',	'ngovanhau@gmail.com',	'Nguyen Van B',	'202cb962ac59075b964b07152d234b70',	'USER',	'285704152',	'0325648122',	1),
(4,	'haungo',	'ngovanhau@gmail.com',	'Hau Ngo',	'202cb962ac59075b964b07152d234b70',	'STAFF',	'123465',	'01235679',	1);

INSERT INTO `flight` (`id`, `plane_id`, `flight_from`, `flight_to`, `time_start`, `flight_time`) VALUES
(1,	1,	2,	1,	'2020-12-19 23:00:00',	'0130'),
(2,	1,	1,	2,	'2020-12-23 17:30:00',	'0130'),
(3,	2,	4,	3,	'2020-12-21 15:10:00',	'0150'),
(4,	2,	2,	4,	'2020-12-24 12:30:00',	'0200'),
(5,	2,	1,	3,	'2020-12-25 16:15:00',	'0130'),
(6,	3,	2,	1,	'2020-12-24 18:00:00',	'0130'),
(7,	1,	4,	2,	'2020-12-26 07:15:00',	'0300');

INSERT INTO `intermediate_airport` (`flight_id`, `id`, `time_layover`, `order`, `note`) VALUES
(1,	5,	'0015',	'0',	'trong lúc dừng chỉ được ngồi trong máy bay'),
(7,	1,	'0030',	'0',	'được xuống máy bay trong 15p'),
(7,	7,	'0015',	'1',	'k xuong may bay');

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

INSERT INTO `scheduled` (`id`, `flight_id`, `customer_id`, `seat_type_id`, `position`, `count_seat`, `price`, `is_used`, `time_create`) VALUES
(1,	1,	2,	1,	'12,13,90,100,110,120,126',	2,	200,	0,	'2020-12-19 23:06:00'),
(2,	7,	1,	1,	'22,33',	2,	600,	0,	'2020-12-20 23:06:00'),
(3,	7,	3,	2,	'11',	1,	100,	0,	'2020-12-25 23:06:00'),
(4,	2,	2,	1,	'12,13,93,102,111,123,124,222',	2,	20,	NULL,	'2020-12-16 11:03:39');

INSERT INTO `seat_type` (`id`, `plane_id`, `seat_name`, `row_from`, `row_to`, `amount_of_row`, `price`) VALUES
(1,	1,	'ECONOMY',	1,	8,	4,	300),
(2,	1,	'BUSINESS ',	9,	13,	6,	80),
(4,	2,	'ECONOMY',	1,	8,	4,	0),
(5,	2,	'BUSINESS ',	9,	13,	6,	0),
(7,	3,	'ECONOMY',	1,	8,	4,	0),
(8,	3,	'BUSINESS ',	9,	13,	6,	0),
(10,	4,	'ECONOMY',	1,	8,	4,	0),
(11,	4,	'BUSINESS ',	9,	13,	6,	0),
(13,	5,	'ECONOMY',	1,	8,	4,	0),
(14,	5,	'BUSINESS ',	9,	13,	6,	0),
(16,	6,	'ECONOMY',	1,	8,	4,	0),
(17,	6,	'BUSINESS ',	9,	13,	6,	0);

-- 2020-12-16 14:38:40
