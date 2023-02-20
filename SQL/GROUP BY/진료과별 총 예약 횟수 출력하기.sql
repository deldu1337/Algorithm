SELECT MCDP_CD as 진료과코드, SUM(MONTH(APNT_YMD) = '5') as 5월예약건수
FROM APPOINTMENT
GROUP BY 진료과코드
HAVING 5월예약건수 >= 1
ORDER BY 5월예약건수, 진료과코드
