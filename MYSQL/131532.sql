SELECT YEAR(sales_date) AS YEAR ,  
    MONTH(sales_date) MONTH, 
    gender, 
    COUNT(DISTINCT U.USER_ID) USERS

FROM USER_INFO U , ONLINE_SALE O
WHERE U.USER_ID = O.USER_ID
AND gender IS NOT NULL

GROUP BY YEAR,MONTH,gender

ORDER BY YEAR,MONTH,gender