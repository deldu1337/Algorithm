SELECT *
FROM FOOD_PRODUCT
WHERE PRICE in
(SELECT MAX(PRICE) as PRICE FROM FOOD_PRODUCT)
