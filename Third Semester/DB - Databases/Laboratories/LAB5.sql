USE EchipaDeHandbal3
GO

---VALIDARE STRING NOT NULL ---
CREATE OR ALTER Function IS_NOT_NULL(@string nvarchar(100))
   RETURNS INT
AS
BEGIN
	IF @string IS NOT NULL
		RETURN 1

	RETURN 0
	 
END


----CRUD PT Echipe-----
CREATE OR ALTER PROCEDURE CRUD_ECHIPE
              @denumire varchar(100),
			  @oras varchar(50),
			  @noOfRows INT = 1
AS
BEGIN
         SET NOCOUNT ON;
		  
		      IF(dbo.IS_NOT_NULL(@denumire) = 1 AND
			       dbo.IS_NOT_NULL(@oras) = 1)
				   BEGIN

				         ---INSERT--
						 DECLARE @n INT = 0;

						 DECLARE @lastId INT = (SELECT ISNULL (max (Eid), 0) + 1 from Echipe);
						 DECLARE @SearchString varchar(50) = '' + @denumire + '%';

						 WHILE (@n < @noOfRows)
						      BEGIN
							       declare @denumireUnique varchar(50) = @denumire + CONVERT(varchar(10), @lastId);
								   INSERT INTO Echipe VALUES (@denumireUnique, @oras);
								   SET @n = @n + 1
								   SET @lastId = @lastId + 1
							  END

						---SELECT---
						SELECT * FROM Echipe ORDER BY Denumire

						---UPDATE---
						UPDATE Echipe
						SET Denumire = @denumire + '_CRUD'
						WHERE Denumire LIKE @SearchString
						SELECT * FROM Echipe ORDER BY Denumire

						---DELETE---
						DELETE FROM Echipe
				        WHERE Denumire LIKE @denumire + '_CRUD';

				        SELECT * FROM Echipe ORDER BY Denumire;

				        PRINT 'Operatii CRUD pentru Echipe executate cu succes.';

			END
		ELSE
			BEGIN
				RAISERROR('Invalid input!', 18, 1);
			END

END;


SELECT * FROM Echipe
EXEC CRUD_ECHIPE 'denumireTest', 'orasTest',3;

GO

-- CRUD PENTRU Competitii --
CREATE OR ALTER PROCEDURE CRUD_COMPETITII
				@denumire varchar(50),
				@noOfRows INT = 1
AS
BEGIN
		SET NOCOUNT ON;

		IF( dbo.IS_NOT_NULL(@denumire) = 1)
			BEGIN
				
					-- INSERT --

					DECLARE @n INT = 0;

					WHILE (@n < @noOfRows)
					BEGIN
						
						INSERT INTO Competitii VALUES	(@denumire);
						SET @n = @n + 1;

					END;

					-- SELECT --
					
					SELECT * FROM Competitii ORDER BY Denumire;

					-- UPDATE --

					UPDATE Competitii
					SET Denumire = @denumire + '_CRUD'
					WHERE Denumire LIKE @denumire;

					SELECT * FROM Competitii ORDER BY Denumire;

					-- DELETE --


					DELETE FROM Competitii
					WHERE Denumire LIKE @denumire + '_CRUD';

					SELECT * FROM Competitii ORDER BY Denumire;

					PRINT 'Operatii CRUD pentru Competitii executate cu succes.';


			END
		ELSE
			BEGIN
				RAISERROR('Invalid input!', 18, 1);
			END

END

SELECT * FROM Competitii;
EXEC CRUD_COMPETITII'denumireTest',3;


GO



----VALIDARE FOREIGN KEYS----
CREATE OR ALTER FUNCTION IS_VALID_ECHIPE_COMPETITII(@echipaId INT, @competitieId INT)
     RETURNS INT
AS
BEGIN
       IF (EXISTS(SELECT * FROM Echipe WHERE Eid = @echipaId) AND EXISTS(SELECT * FROM Competitii WHERE Cid = @competitieId))
	                RETURN 1
	   RETURN 0
END
GO


CREATE OR ALTER PROCEDURE CRUD_ECHIPE_COMPETITII
    @echipaID INT,
    @competitieID INT
AS
BEGIN
    SET NOCOUNT ON;

    IF(dbo.IS_VALID_ECHIPE_COMPETITII(@echipaID, @competitieID) = 1)
    BEGIN
        -- Debugging statements
        PRINT 'Validation passed. Proceeding with CRUD operations.';

        -- INSERT
        PRINT 'Inserting into EchipeCompetitii';
        INSERT INTO EchipeCompetitii VALUES (@echipaID, @competitieID);

        -- SELECT
        PRINT 'Selecting from EchipeCompetitii';
        SELECT * FROM EchipeCompetitii ORDER BY Eid;

        -- UPDATE
        -- Your update logic here

        -- DELETE
        PRINT 'Deleting from EchipeCompetitii';
        DELETE FROM EchipeCompetitii WHERE Eid = @echipaID AND Cid = @competitieID;

        SELECT * FROM EchipeCompetitii ORDER BY Cid;
    END
    ELSE
    BEGIN
        RAISERROR('Invalid input! Check validation logic.', 18, 1);
    END
END

SELECT * FROM EchipeCompetitii;
EXEC CRUD_ECHIPE_COMPETITII 10, 1;



----VIEWS----
CREATE OR ALTER VIEW ViewNumberEchipe
AS
        select C.Denumire AS Echipa, COUNT(*) AS NumarEchipe
		FROM Echipe AS E
		INNER JOIN EchipeCompetitii AS EC ON E.Eid = EC.Eid
		INNER JOIN Competitii AS C ON EC.Cid = C.Cid
		GROUP BY C.Denumire;
GO
drop view ViewNumberEchipe

CREATE OR ALTER VIEW ViewListEchipe
AS
          SELECT E.Denumire AS DenumireEchipa
		  FROM Echipe AS E
		  INNER JOIN EchipeCompetitii AS EC ON E.Eid = EC.Eid
		  INNER JOIN Competitii AS C ON EC.Cid = C.Cid
		  WHERE C.Denumire = 'EHF Champions League';
GO

SELECT * FROM ViewNumberEchipe;

SELECT * FROM ViewListEchipe;


--- INDECSI ---

-- Echipe
CREATE NONCLUSTERED INDEX N_idx_DenumireEchipa ON Echipe (Denumire);

-- Competitii
CREATE NONCLUSTERED INDEX N_idx_DenumireCompetitie ON Competitii (Denumire);

-- Echipe Competitii
CREATE NONCLUSTERED INDEX N_idx_ECEid ON EchipeCompetitii (Eid);
CREATE NONCLUSTERED INDEX N_idx_ECCid ON EchipeCompetitii (Cid);							
							       