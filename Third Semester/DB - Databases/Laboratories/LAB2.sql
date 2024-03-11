--Selecteaza toti jucatorii peste 25 ani de la Kielce care au antrenament de forta
SELECT J.Nume, J.Prenume, J.Varsta
FROM Jucatori AS J
INNER JOIN Echipe AS E ON J.Eid = E.Eid
INNER JOIN JucatoriAntrenamente AS JA ON J.Jid = JA.Jid
INNER JOIN Antrenamente AS A ON JA.Antid = A.Antid
WHERE E.Denumire = 'Vive Kielce'
  AND J.Varsta > 25
  AND A.Tip = 'Forta';

--Selecteaza toti jucatorii de pe pozitia centru care poarta marimea XL si sunt la PSG sau la Kielce
SELECT J.Nume, J.Prenume, EC.Marime, E.Denumire
FROM Jucatori AS J
INNER JOIN Echipe AS E ON J.EID = E.Eid
INNER JOIN Echipamente AS EC ON J.Jid = EC.Jid
WHERE EC.Marime = 'XL' AND J.Pozitie = 'Centru' AND (E.Denumire = 'PSG' OR E.Denumire = 'Vive Kielce');

--Selecteaza o lista distincta cu numele jucatorilor, prenumele, pozitia,denumire echipa, numar ec
SELECT DISTINCT J.Nume, J.Prenume, J.Pozitie, E.Denumire, EC.Numar
FROM Jucatori AS J
INNER JOIN Echipe AS E ON J.Eid = E.Eid
INNER JOIN Echipamente AS EC ON J.Eid = EC.Jid

--Selecteaza o lista de echipe distincte, competitia in care evolueaza si numele si prenumele antrenorilor
SELECT DISTINCT E.Denumire, C.Denumire, A.Nume, A.Prenume
FROM Echipe AS E
INNER JOIN EchipeCompetitii AS EC ON E.Eid = EC.Eid
INNER JOIN Competitii AS C ON EC.Cid = C.Cid
INNER JOIN Antrenori AS A ON E.Eid = A.Eid AND A.Rol = 'Principal'

--Selecteaza jucatorii care au inaltimea peste 190cm
SELECT J.Nume, J.Prenume, J.Inaltime
FROM Jucatori AS J
WHERE J.Inaltime > 190

--Selecteaza echipele cu media de varsta peste 25 ani care au antrenor principal
SELECT E.Denumire AS Echipa, AVG(J.Varsta) AS MedieVarsta
FROM Echipe AS E
INNER JOIN Jucatori AS J ON E.Eid = J.Eid
INNER JOIN Antrenori AS A ON E.Eid = A.Eid
WHERE A.Rol = 'Principal'
GROUP BY E.Denumire
HAVING AVG(J.Varsta) > 25


--Selecteaza echipele cu media de inaltime peste 195cm si care au antrenor principal
SELECT E.Denumire AS Echipa, AVG(J.Inaltime) AS MedieInaltime
FROM Echipe AS E
INNER JOIN Jucatori AS J ON E.Eid = J.Eid
INNER JOIN Antrenori AS A ON E.Eid = A.Eid
WHERE A.Rol = 'Principal'
GROUP BY E.Denumire
HAVING AVG(J.Inaltime) > 195


--Selecteaza echipele cu nr lor de jucatori
SELECT E.Denumire AS Echipa, COUNT(J.Jid) AS NumarJucatori
FROM Echipe AS E
INNER JOIN Jucatori AS J ON E.Eid = J.Eid
GROUP BY E.Denumire


--Selecteaza toate meciurile care au avut mai mult de 4000 de spectatori din EHF Champions League
SELECT M.Echipe, M.Scor, C.Denumire, M.NrSpectatori
FROM Meciuri AS M
INNER JOIN Competitii AS C ON M.Cid = C.Cid
WHERE M.NrSpectatori > 4000


--Selecteaza jucatorii din EHF Champions League cu varsta mai mica de 25 ani
SELECT J.Nume, J.Prenume, J.Varsta, C.Denumire
FROM Jucatori AS J
INNER JOIN Echipe AS E ON J.Eid = E.Eid
INNER JOIN EchipeCompetitii AS EC ON E.Eid = EC.Eid
INNER JOIN Competitii AS C ON EC.Cid = C.Cid
WHERE C.Denumire = 'EHF Champions League' AND J.Varsta < 25;



