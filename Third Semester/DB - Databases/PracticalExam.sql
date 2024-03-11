CREATE DATABASE CFR;
USE CFR;
GO

create table tip_tren(
	tip_id int not null identity,
	descriere varchar(30),
	constraint tip_tren_pk primary key(tip_id)
)

create table tren(
	tren_id int not null identity,
	nume varchar(30),
	tip_id int foreign key references tip_tren(tip_id),
	constraint tren_id_pk primary key(tren_id)
)

create table rute(
	ruta_id int primary key identity,
	nume varchar(30),
	tren_id int foreign key references tren(tren_id)
)

create table statii(
	statie_id int primary key identity,
	nume varchar(30)
)

create table statii_rute(
	statie_id int foreign key references statii(statie_id),
	ruta_id int foreign key references rute(ruta_id),
	ora_plecare time,
	ora_sosire time,
	constraint pk_statii_rute primary key (statie_id,ruta_id)
)

insert into tip_tren(descriere) values('personal'),
('regio'),
('inter-regio')
 
insert into tren(nume,tip_id) values
('Tomas',1),
('Eduard',2),
('James',3),
('Toby',2),
('Emili',1),
('Cranky',1),
('Controlorul Gras',1)
 
insert into rute(nume,tren_id) values
('Galati-Cluj',1),
('Cluj-Napoca-Baia Mare',2),
('Cluj-Napoca-Botosani',3),
('Cluj-Napoca-Braila',4),
('Timisoara-Salaj',5),
('Constanta-Iasi',6),
('Botosani-Craiova',7)
 
insert into statii(nume) values
('Constanta'),
('Cluj-Napoca'),
('Bucuresti'),
('Ilva Mica'),
('Nasaud'),
('Salva'),
('Beclean'),
('Dej'),
('Dej Calatori'),
('Gherla'),
('Baia Mare')


CREATE PROCEDURE Pr @idstatie INT, @idruta INT, @oraplecare TIME, @orasosire TIME
AS
BEGIN
  IF (EXISTS(
    SELECT * FROM statii_rute
    WHERE statie_id=@idstatie AND ruta_id=@idruta
    ))
  BEGIN 
    UPDATE statii_rute 
    SET ora_plecare=@oraplecare, ora_sosire=@orasosire
    WHERE statie_id=@idstatie and ruta_id=@idruta
  END
  ELSE
  BEGIN 
    INSERT INTO statii_rute(statie_id,ruta_id,ora_plecare,ora_sosire)
    VALUES (@idstatie,@idruta,@oraplecare,@orasosire)
  END
END;
  
EXEC Pr 1,1,'12:09:14','19:13:54';
EXEC Pr 1,1,'13:09:14','19:13:54';
SELECT * FROM statii_rute;

EXEC Pr 2,1,'15:09:14','19:13:54';
EXEC Pr 3,1,'15:09:14','19:13:54';
EXEC Pr 4,1,'15:09:14','19:13:54';
EXEC Pr 5,1,'15:09:14','19:13:54';
EXEC Pr 6,1,'15:09:14','19:13:54';
EXEC Pr 7,1,'15:09:14','19:13:54';
EXEC Pr 8,1,'15:09:14','19:13:54';
EXEC Pr 9,1,'15:09:14','19:13:54';
EXEC Pr 10,1,'15:09:14','19:13:54';
EXEC Pr 11,1,'15:09:14','19:13:54';
 
 
EXEC Pr 11,2,'15:09:14','20:13:54';
 
GO
CREATE OR ALTER VIEW VW_RuteComplete AS
  SELECT R.nume AS Ruta FROM rute R
  INNER JOIN statii_rute SR ON SR.ruta_id = R.ruta_id
  GROUP BY R.ruta_id, R.nume
  HAVING COUNT(*) = (SELECT COUNT(*) FROM statii)
GO
 
SELECT * FROM VW_RuteComplete;