SELECT

Customer_ID,

COUNT(Order_ID) AS Total_Orders,

SUM(Price * Quantity) AS Total_Revenue

FROM `gcp-data-engineering-manjit.ecommerce.sales_native`

GROUP BY Customer_ID

ORDER BY Total_Revenue DESC

LIMIT 5;