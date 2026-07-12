SELECT

Product,

SUM(Quantity) AS Total_Units_Sold,

SUM(Price * Quantity) AS Total_Revenue

FROM `gcp-data-engineering-manjit.ecommerce.sales_native`

GROUP BY Product

ORDER BY Total_Units_Sold DESC;