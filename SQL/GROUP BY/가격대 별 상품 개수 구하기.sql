SELECT TRUNCATE(PRICE/10000, 0) * 10000 as PRICE_GROUP, COUNT(PRICE) as PRODUCTS
FROM PRODUCT
GROUP BY PRICE_GROUP
ORDER BY PRICE_GROUP
