SELECT DATETIME as 시간
FROM ANIMAL_INS
WHERE DATETIME IN
(SELECT MAX(DATETIME) FROM ANIMAL_INS)
