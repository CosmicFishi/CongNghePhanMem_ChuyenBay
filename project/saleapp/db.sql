-- Adminer 4.7.7 MySQL dump

SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

INSERT INTO `KhachHang` (`MaKH`, `TenKH`, `TenTK`, `MatKhau`, `CMND`, `SDT`, `active`) VALUES
(1,	'Haungo',	'haungo',	'202cb962ac59075b964b07152d234b70',	'000011111',	'012345678',	1);

INSERT INTO `chuyenbay` (`MaMayBay`, `MaChuyenBay`, `SanBayDi`, `SanBayDen`, `TGXuatPhat`, `TGBay`) VALUES
(1,	1,	1,	2,	'1607517379',	'0130');



INSERT INTO `maybay` (`MaMayBay`, `TenMayBay`) VALUES
(1,	'B52');

INSERT INTO `sanbay` (`MaSanBay`, `TenSanBay`, `Anh`) VALUES
(1,	'Tân Sơn Nhất ',	'/images/airport/Ho-Chi-Minh-City-SGN.jpg'),
(2,	'Hue',	'/images/airport/Hue-HUI.jpg');


-- 2020-12-09 13:50:26
