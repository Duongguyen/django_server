use QLSV
select * from Ketqua
sp_help ketqua
	
select * from dbo.SinhVien
delete from Ketqua
alter table Ketqua add constraint FK_mh foreign key (Mamh) references dbo.Monhoc(Mamh)

insert  into dbo.SinhVien values('1', N'Trần Bảo Trọng', N'Nam', '1995-12-14', N'Hà Giang', 'L02'),
('2', N'Lê Thùy Dương', N'Nữ', '1997-05-12', N'Hà Nội', 'L03'),
('3', N'Trần Phương Thảo', N'Nữ', '1996-03-30', N'Quảng Ninh', 'L01'),
('4', N'Lê Trường An', N'Nam', '1995-11-20', N'Ninh Bình', 'L04'),
('5', N'Phạm Thị Hương Giang', N'Nữ', '1999-02-21', N'Hòa Bình', 'L02'),
('6', N'Trần Anh Bảo', N'Nam', '1995-12-14', N'Hà Giang', 'L02'),
('7', N'Lê Thùy Dung', N'Nữ', '1997-05-12', N'Hà Nội', 'L03'),
('8', N'Phạm Trung Tình', N'Nam', '1996-03-30', N'Quảng Ninh', 'L01'),
('9', N'Lê An Hải', N'Nam', '1995-11-20', N'Ninh Bình', 'L04'),
('10', N'Phạm Thị Giang Hương', N'Nữ', '1999-02-21', N'Hòa Bình', 'L02'),
('11', N'Đoàn Duy Thức', N'Nam', '1994-04-12', N'Hà Nội', 'L01'),
('12', N'Dương Tuấn Thông', N'Nam', '1994-04-12', N'Nam Định', 'L03'),
('13', N'Lê Thành Đạt', N'Nam', '1993-04-15', N'Phú Thọ', 'L04'),
('14', N'Nguyễn Hằng Nga', N'Nữ', '1993-05-25', N'Hà Nội', 'L01'),
('15', N'Trần Thanh Nga', N'Nữ', '1994-06-20', N'Phú Thọ', 'L03'),
('16', N'Trần Trọng Hoàng', N'Nam', '1995-12-14', N'Hà Giang', 'L02'),
('17', N'Nguyễn Mai Hoa', N'Nữ', '1997-05-12', N'Hà Nội', 'L03'),
('18', N'Lê Thúy An	Nữ', N'Nữ', '1998-03-23', N'Hà Nội', 'L01')


insert  into dbo.Monhoc values('1', N'Toán Cao Cấp', 3),
('2', N'Mạng Máy Tính', 3),
('3', N'Tin đại cương', 4)

insert into dbo.Ketqua values('1','1',3),
('1','2',5),
('1','3',7),
('2','1',9),
('2','2',5),
('2','3',2),
('3','1',4),
('3','2',2),
('4','1',1),
('4','2',3),
('5','1',4),
('6','1',2),
('6','2',7),
('6','3',9),
('7','1',4),
('7','2',5),
('7','3',8),
('8','1',9),
('8','2',8),
('9','1',7),
('9','2',7),
('9','3',5),
('10','1',3),
('10','3',6),
('11','1',6),
('12','1',8),
('12','2',7),
('12','3',5),
('13','1',5),
('13','2',5),
('13','3',5),
('14','1',8),
('14','2',9),
('14','3',7),
('15','1',3),
('15','2',6),
('15','3',4)

