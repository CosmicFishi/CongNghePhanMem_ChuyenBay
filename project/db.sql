-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

INSERT INTO `chuyenbay` (`MaMayBay`, `MaChuyenBay`, `SanBayDi`, `SanBayDen`, `TGXuatPhat`, `TGBay`) VALUES
(1,	1,	1,	2,	'1607517379',	'0130');



INSERT INTO `maybay` (`MaMayBay`, `TenMayBay`) VALUES
(1,	'B52'),
(2,	'Vietnam Airlines 1'),
(3,	'Vietnam Airlines 2'),
(4,	'Vietnam Airlines 3'),
(5,	'Vietnam Airlines 4'),
(6,	'Vietjet Air 1'),
(7,	'Vietjet Air 2'),
(8,	'Vietjet Air 3'),
(9,	'Vietjet Air 4'),
(10,	'Jetstar Pacific 1'),
(11,	'Jetstar Pacific 2'),
(12,	'Jetstar Pacific 3'),
(13,	'Jetstar Pacific 4'),
(14,	'Bamboo Airways 1'),
(15,	'Bamboo Airways 2'),
(16,	'Bamboo Airways 3'),
(17,	'Bamboo Airways 4');

INSERT INTO `sanbay` (`MaSanBay`, `TenSanBay`, `Anh`) VALUES
(1,	'Tân Sơn Nhất ',	'/images/airport/Ho-Chi-Minh-City-SGN.jpg'),
(2,	'Huế',	'/images/airport/Hue-HUI.jpg'),
(3,	'Vinh',	'/images/airport/Vinh-VII.jpg'),
(4,	'Phú Quốc',	'/images/airport/Phu-Quoc-PQC.jpg'),
(5,	'Hải Phòng',	'images/airport/Hai-Phong-HPH.jpg'),
(6,	'Đà Nẵng',	'images/airport/Da-Nang-DAD.jpg'),
(7,	'Đà Lạt',	'images/airport/Da-Lat-DLI.jpg');


-- 2020-12-11 16:55:28
