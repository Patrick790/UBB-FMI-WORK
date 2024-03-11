CREATE DATABASE GestiuneGaraje
GO

USE GestiuneGaraje
GO


create table Tipuri(
     id_tip int primary key identity,
	 tip varchar(30),
	 descriere varchar(50)
)

create table Garaje(
     id_garaj int primary key identity,
	 denumire varchar(50),
	 strada varchar(50),
	 numar int,
	 localitate varchar(50),
	 id_tip int foreign key references Tipuri(id_tip)
)


create table Clienti(
      id_client int primary key identity,
	  nume varchar(50),
	  prenume varchar(50),
	  gen varchar(30),
	  vechime int
)


create table Unelte(
     id_unealta int primary key identity,
	 denumire varchar(50),
	 pret float,
	 cantitate int,
	 id_client int foreign key references Clienti(id_client)
)

create table ClientiGaraje(
    id_client int foreign key references Clienti(id_client),
	id_garaj int foreign key references Garaje(id_garaj),
	data_activitatii date,
	beneficiu varchar(50),
	constraint pk_clienti_garaje primary key (id_client, id_garaj)
)


insert into Tipuri(tip, descriere) values
('masini', 'desc1'),
('unelte', 'desc2'),
('avioane', 'desc3'),
('depozitare', 'desc4')


insert into Garaje(denumire, strada, numar, localitate, id_tip) values
('Johns', 'Bucium', 11, 'Cluj-Napoca', 1),
('Daves', 'Bucegi', 23, 'Cluj-Napoca', 2),
('LaGaraj', 'Fericirii', 12, 'Galati', 3),
('Garajul', 'Bucovinei', 44, 'Baia-Mare', 1),
('Mikes', 'Iugoslaviei', 55, 'Arad', 4)


insert into Clienti(nume, prenume, gen, vechime) values
('Barbu', 'Ion', 'M', 2),
('Alexandrscu', 'Stefan', 'M', 3),
('Bartes', 'Silviu', 'M', 5),
('Barbu', 'Maia', 'F', 2),
('Rus', 'Anastasia', 'F', 3),
('Angheluta', 'Dragos', 'M', 10),
('Apetrei', 'Alexandru', 'M', 8)

insert into Unelte(denumire, pret, cantitate, id_client) values
('u1', 25.5, 2, 1),
('u2', 20.4, 3, 2),
('u3', 10.0, 1, 1),
('u4', 25.6, 4, 3),
('u5', 11.6, 1, 4)

insert into ClientiGaraje(id_client, id_garaj, data_activitatii, beneficiu) values
(1,1, '2024-01-03', 'beneficiu1'),
(2, 1, '2023-12-21', 'beneficiu2'),
(2, 2, '2023-10-23', 'beneficiu3'),
(3, 3, '2024-02-21', 'beneficiu4');


CREATE OR ALTER PROCEDURE Cerinta2 @idclient INT, @idgaraj INT, @dataactivitate DATE, @beneficiu VARCHAR(50)
AS
BEGIN
      IF (EXISTS(
	      SELECT * FROM ClientiGaraje 
		  WHERE id_client = @idclient AND id_garaj = @idgaraj))
	  BEGIN
	      UPDATE ClientiGaraje
		  SET data_activitatii = @dataactivitate, beneficiu = @beneficiu
		  WHERE id_client = @idclient AND id_garaj = @idgaraj
	  END
	  ELSE
	  BEGIN
	       INSERT INTO ClientiGaraje(id_client, id_garaj, data_activitatii, beneficiu)
		   VALUES (@idclient, @idgaraj, @dataactivitate, @beneficiu)
	  END
END

EXEC Cerinta2 3,1,'2023-08-30', 'beneficiu5';
EXEC Cerinta2 3,1,'2022-09-11', 'ben5';

SELECT * FROM ClientiGaraje


EXEC Cerinta2 4,2,'2023-11-30','b6';
EXEC Cerinta2 4,2, '2021-12-20','ben7';


CREATE OR ALTER FUNCTION Cerinta3(@n INT)
RETURNS TABLE
AS
RETURN (SELECT C.nume, C.prenume FROM Clienti C
WHERE @n <= ( SELECT COUNT(DISTINCT id_garaj)
              FROM ClientiGaraje
			  WHERE id_client = C.id_client)
);

SELECT * FROM dbo.Cerinta3(2);
SELECT * FROM dbo.Cerinta3(1);
SELECT * FROM dbo.Cerinta3(3);




