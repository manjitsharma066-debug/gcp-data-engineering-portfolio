SELECT

Order_Date,

COUNT(*) AS Total_Orders,

SUM(Price * Quantity) AS Total_Revenue

FROM `gcp-data-engineering-manjit.ecommerce.sales_native`

GROUP BY Order_Date

ORDER BY Order_Date;


SELECT *
FROM `gcp-data-engineering-manjit.ecommerce.sales_native`
LIMIT 1;