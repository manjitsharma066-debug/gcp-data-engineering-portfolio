SELECT
    Product,
    SUM(Quantity) AS Total_Quantity,
    SUM(Price * Quantity) AS Total_Revenue

FROM `gcp-data-engineering-manjit.ecommerce.sales_native`

GROUP BY Product

ORDER BY Total_Revenue DESC

LIMIT 5;