SELECT

SUM(Price * Quantity) AS Total_Revenue

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`;


SELECT

COUNT(Order_ID) AS Total_Orders

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`;

SELECT

ROUND(AVG(Price * Quantity),2) AS Average_Order_Value

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`;

SELECT

Product,

MAX(Price) AS Highest_Price

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`

GROUP BY Product

ORDER BY Highest_Price DESC;





SELECT

Product,

MIN(Price) AS Lowest_Price

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`

GROUP BY Product

ORDER BY Lowest_Price;