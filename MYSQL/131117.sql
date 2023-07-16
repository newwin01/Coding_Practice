SELECT FP.PRODUCT_ID, FP.PRODUCT_NAME, SUM(FP.PRICE * FO.AMOUNT) AS TOTAL_SALES
FROM FOOD_PRODUCT AS FP JOIN FOOD_ORDER AS FO ON FP.PRODUCT_ID = FO.PRODUCT_ID
WHERE FO.PRODUCE_DATE LIKE '2022-05%' 
GROUP BY FP.PRODUCT_ID 
ORDER BY TOTAL_SALES DESC, FP.PRODUCT_ID;