USE EchipaDeHandbal3
GO

SELECT * FROM Tests
SELECT * FROM Tables
SELECT * FROM TestTables
SELECT * FROM Views 
SELECT * FROM TestViews 
SELECT * FROM TestRuns
SELECT * FROM TestRunTables 
SELECT * FROM TestRunViews
GO
delete from Views

drop table Views



CREATE TABLE [Tables] (
	[TableID] [int] IDENTITY (1, 1) NOT NULL ,
	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [TestRunTables] (
	[TestRunID] [int] NOT NULL ,
	[TableID] [int] NOT NULL ,
	[StartAt] [datetime] NOT NULL ,
	[EndAt] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [TestRunViews] (
	[TestRunID] [int] NOT NULL ,
	[ViewID] [int] NOT NULL ,
	[StartAt] [datetime] NOT NULL ,
	[EndAt] [datetime] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [TestRuns] (
	[TestRunID] [int] IDENTITY (1, 1) NOT NULL ,
	[Description] [nvarchar] (2000) COLLATE SQL_Latin1_General_CP1_CI_AS NULL ,
	[StartAt] [datetime] NULL ,
	[EndAt] [datetime] NULL 
) ON [PRIMARY]
GO

CREATE TABLE [TestTables] (
	[TestID] [int] NOT NULL ,
	[TableID] [int] NOT NULL ,
	[NoOfRows] [int] NOT NULL ,
	[Position] [int] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [TestViews] (
	[TestID] [int] NOT NULL ,
	[ViewID] [int] NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [Tests] (
	[TestID] [int] IDENTITY (1, 1) NOT NULL ,
	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 
) ON [PRIMARY]
GO

CREATE TABLE [Views] (
	[ViewID] [int] IDENTITY (1, 1) NOT NULL ,
	[Name] [nvarchar] (50) COLLATE SQL_Latin1_General_CP1_CI_AS NOT NULL 
) ON [PRIMARY]
GO

CREATE OR ALTER VIEW ViewOneTable
AS
        SELECT * FROM Echipe
GO

CREATE OR ALTER VIEW ViewTwoTables
AS
   SELECT E.Denumire, J.Nume, J.Prenume, J.Varsta
   FROM Jucatori AS J
   INNER JOIN Echipe AS E ON J.Eid = E.Eid
GO

CREATE OR ALTER VIEW ViewGroupBy
AS
     SELECT COUNT(J.Jid) as NoOfPlayers, J.Eid
	  FROM  Jucatori J
	  GROUP BY J.Eid
	  HAVING J.Eid IN (SELECT E.Eid FROM Echipe E)

GO

create or alter procedure delete_table
       @no_of_rows INT,
	   @table_name VARCHAR(30)
AS
begin
       declare @last_row INT

	   if @table_name = 'Echipe'
	   begin
	   if(select count(*) from Echipe) < @no_of_rows
	   begin
	         print('Too many rows to delete')
			 return 1
       end
	   else
	   begin
	          set @last_row = (select max(Eid) from Echipe) - @no_of_rows

			  delete from Echipe where Eid > @last_row
	   end
	   end

	   else if @table_name = 'Competitii'
	   begin
	   if(select count(*) from Competitii) < @no_of_rows
	   begin
	         print('Too many rows to delete')
			 return 1
	   end
	   else
	   begin
	         set @last_row = (SELECT MAX(Cid) from Competitii) - @no_of_rows
			 delete from Competitii
			 where Cid > @last_row
	   end
	   end

	   else if @table_name = 'Jucatori'
	   BEGIN
	   if(select count(*) from Jucatori) < @no_of_rows
	   begin
	        print('Too many rows to delete')
			return 1
	   end
	   else
	   begin
	        set @last_row = (select max(Jid) from Jucatori) - @no_of_rows

			delete from Jucatori where Jid > @last_row
       end
	   end

	   else if @table_name = 'EchipeCompetitii'
	   begin
	   if(select count(*) from EchipeCompetitii) < @no_of_rows
	   begin
	       print ('Too many rows to delete')
		   return 1
	   end

	   else
	   begin
	          delete from EchipeCompetitii where Eid >= @no_of_rows
	   end
	   end

	   else
	   begin
	        print('Not a valid table name')
			return 1
	   end
end
go

create or alter procedure insert_table
      @no_of_rows INT,
	  @table_name varchar(30)
AS
BEGIN
        declare @input_id INT
		if @table_name = 'Echipe'
		begin
		       while @no_of_rows > 0
			   begin
			           insert into Echipe(Denumire, Oras) VALUES ('POLI', 'TIMISOARA')

					   set @no_of_rows = @no_of_rows - 1
			   end
		end


		else if @table_name = 'Competitii'
		BEGIN
		    while @no_of_rows > 0
			BEGIN
			      insert into Competitii(Denumire) VALUES ('Liga Zimbrilor')
				  set @no_of_rows = @no_of_rows - 1
			end
	    end

		else if @table_name = 'Jucatori'
		begin
		declare @fk1 int
		set @fk1=(select top 1 Eid from Echipe)

		       while @no_of_rows > 0
			   begin
			     insert into Jucatori(Nume, Prenume, Pozitie, Inaltime, Varsta, Eid) VALUES('Ardelean', 'Patrick', 'Centru', 180, 20, @fk1)


				 set @no_of_rows = @no_of_rows - 1
	           end
        end


        else if @table_name = 'EchipeCompetitii'
		begin
		set @input_id = @no_of_rows
		DECLARE @fk INT
		--DECLARE @fk2 INT
		SET @fk=(select top 1 Cid from Competitii)
		--SET @fk2=(select top 1 Eid from Echipe)
		      while @no_of_rows > 0
			  begin
			       insert into EchipeCompetitii(Eid, Cid) VALUES (@input_id, @fk)

				   set @input_id = @input_id + 1
				   
				   set @no_of_rows = @no_of_rows - 1
				   
			  end
	     end

		 else
		 begin 
		         print('Not a valid table name')
				 return 1
		 end
	end
	go

	

drop procedure insert_table


CREATE OR ALTER PROCEDURE select_view
	@view_name VARCHAR(30)
AS
BEGIN
	IF @view_name='ViewOneTable'
	BEGIN 
		SELECT * FROM ViewOneTable
	END

	ELSE IF @view_name='ViewTwoTables'
	BEGIN 
		SELECT * FROM ViewTwoTables
	END

	ELSE IF @view_name='ViewGroupBy'
	BEGIN 
		SELECT * FROM ViewGroupBy
	END

	ELSE
	BEGIN 
		PRINT('Not a valid view name')
		RETURN 1
	END
END
GO

DELETE FROM Tables
INSERT INTO Tables VALUES ('Echipe'),('Competitii'),('Jucatori'),('EchipeCompetitii')
GO

DELETE FROM Views
INSERT INTO Views VALUES ('ViewOneTable'),('ViewTwoTables'),('ViewGroupBy')
GO

DELETE FROM Tests
INSERT INTO Tests VALUES ('test_10'),('test_100'),('test_1000'),('test_5000')
GO

DELETE FROM TestViews
INSERT INTO TestViews(TestID,ViewID) VALUES (1,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (1,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (1,3)
INSERT INTO TestViews(TestID,ViewID) VALUES (2,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (2,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (2,3)
INSERT INTO TestViews(TestID,ViewID) VALUES (3,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (3,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (3,3)
INSERT INTO TestViews(TestID,ViewID) VALUES (4,1)
INSERT INTO TestViews(TestID,ViewID) VALUES (4,2)
INSERT INTO TestViews(TestID,ViewID) VALUES (4,3)
GO

DELETE FROM TestTables
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (1,1,10,1)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (1,2,10,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (1,3,10,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (1,4,10,4)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (2,1,100,1)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (2,2,100,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (2,3,100,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (2,4,100,4)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (3,1,1000,1)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (3,2,1000,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (3,3,1000,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (3,4,1000,4)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (4,1,5000,1)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (4,2,5000,2)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (4,3,5000,3)
INSERT INTO TestTables(TestId, TableID, NoOfRows, Position) VALUES (4,4,5000,4)

GO

DELETE FROM TestRuns
DELETE FROM TestRunTables
DELETE FROM TestRunViews
GO


CREATE OR ALTER PROCEDURE mainTest
	@testID INT
AS
BEGIN
	INSERT INTO TestRuns VALUES ((SELECT Name FROM Tests WHERE TestID=@testID),GETDATE(),GETDATE())
	DECLARE @testRunID INT
	SET @testRunID=(SELECT MAX(TestRunID) FROM TestRuns)

	DECLARE @noOfRows INT
	DECLARE @tableID INT
	DECLARE @tableName VARCHAR(30)
	DECLARE @startAt DATETIME
	DECLARE @endAt DATETIME
	DECLARE @viewID INT
	DECLARE @viewName VARCHAR(30)

	DECLARE testDeleteCursor CURSOR FOR
	SELECT TableID,NoOfRows
	FROM TestTables
	WHERE TestID=@testID
	ORDER BY Position DESC

	OPEN testDeleteCursor

	FETCH NEXT 
	FROM testDeleteCursor
	INTO @tableID,@noOfRows

	WHILE @@FETCH_STATUS=0
	BEGIN
		SET @tableName=(SELECT Name FROM Tables WHERE TableID=@tableID)

		EXEC delete_table @noOfRows,@tableName

		FETCH NEXT 
		FROM testDeleteCursor
		INTO @tableID,@noOfRows
	END

	CLOSE testDeleteCursor
	DEALLOCATE testDeleteCursor

	DECLARE testInsertCursor CURSOR FOR
	SELECT TableID,NoOfRows
	FROM TestTables
	WHERE TestID=@testID
	ORDER BY Position ASC

	OPEN testInsertCursor

	FETCH NEXT 
	FROM testInsertCursor
	INTO @tableID,@noOfRows

	WHILE @@FETCH_STATUS=0
	BEGIN
		SET @tableName=(SELECT Name FROM Tables WHERE TableID=@tableID)

		SET @startAt=GETDATE()
		EXEC insert_table @noOfRows,@tableName
		SET @endAt=GETDATE()

		INSERT INTO TestRunTables VALUES (@testRunID,@tableID,@startAt,@endAt)

		FETCH NEXT 
		FROM testInsertCursor
		INTO @tableID,@noOfRows
	END

	CLOSE testInsertCursor
	DEALLOCATE testInsertCursor

	DECLARE testViewCursor CURSOR FOR
	SELECT ViewID
	FROM TestViews
	WHERE TestID=@testID

	OPEN testViewCursor

	FETCH NEXT 
	FROM testViewCursor
	INTO @viewID

	WHILE @@FETCH_STATUS=0
	BEGIN
		SET @viewName=(SELECT Name FROM Views WHERE ViewID=@viewID)

		SET @startAt=GETDATE()
		EXEC select_view @viewName
		SET @endAt=GETDATE()

		INSERT INTO TestRunViews VALUES (@testRunID,@viewID,@startAt,@endAt)

		FETCH NEXT 
		FROM testViewCursor
		INTO @viewID
	END

	CLOSE testViewCursor
	DEALLOCATE testViewCursor

	UPDATE TestRuns
	SET EndAt=GETDATE()
	WHERE TestRunID=@testRunID

END
GO

drop procedure mainTest

EXEC mainTest 1
EXEC mainTest 2
EXEC mainTest 3
EXEC mainTest 4

select * from Jucatori