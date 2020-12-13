-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

INSERT INTO `airport` (`id`, `place`, `image`, `airport_name`) VALUES
(1,	'TP. HCM',	'/images/airport/Ho-Chi-Minh-City-SGN.jpg', 'Tân Sơn Nhất'),
(2,	'Huế',	'/images/airport/Hue-HUI.jpg', 'Phú Bài'),
(3,	'Trà Vinh',	'/images/airport/Vinh-VII.jpg', 'Trà Vinh'),
(4,	'Kiên Giang',	'/images/airport/Phu-Quoc-PQC.jpg', 'Phú Quốc'),
(5,	'Hải Phòng',	'images/airport/Hai-Phong-HPH.jpg', 'Kiến An'),
(6,	'Đà Nẵng',	'images/airport/Da-Nang-DAD.jpg', 'Đà Nẵng'),
(7,	'Lâm Đồng',	'images/airport/Da-Lat-DLI.jpg', 'Liên Khương');

INSERT INTO `customer` (`id`, `user_name`, `account_name`, `password`, `type_user`, `id_card`, `phone`, `active`) VALUES
(1,	'haungo',	'Ngo Van Hau',	'202cb962ac59075b964b07152d234b70',	'ADMIN',	'000011111',	'012345678',	1),
(2,	'a',	'Nguyen van A',	'202cb962ac59075b964b07152d234b70',	'USER',	'025651545',	'0383793',	1);

INSERT INTO `flight` (`id`, `plane_id`, `flight_from`, `flight_to`, `time_start`, `flight_time`) VALUES
(1,	1,	1,	2,	'1607517379',	'0130'),
(2,	2,	4,	3,	'1607836081',	'130');

INSERT INTO `intermediate_airport` (`flight_id`, `id`, `time_layover`, `order`, `note`) VALUES
(1,	5,	'0015',	'0',	'trong lúc dừng chỉ được ngồi trong máy bay');

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

INSERT INTO `scheduled` (`flight_id`, `customer_id`, `seat_type_id`, `count_seat`, `price`, `is_used`) VALUES
(1,	2,	1,	'2',	'200',	0);

INSERT INTO `seat_type` (`id`, `plane_id`, `seat_name`, `row_from`, `row_to`, `amount_of_row`) VALUES
(1,	1,	'Ghế thương gia',	1,	8,	4),
(2,	1,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(3,	1,	'Ghế phổ thông',	14,	20,	8),
(4,	2,	'Ghế thương gia',	1,	8,	4),
(5,	2,	'Ghế phổ thông đặc biệt ',	9,	13,	6),
(6,	2,	'Ghế phổ thông',	14,	20,	8);

-- 2020-12-13 05:12:46
