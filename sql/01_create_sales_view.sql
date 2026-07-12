CREATE OR REPLACE VIEW
`gcp-data-engineering-manjit.ecommerce.vw_sales_summary`

AS

SELECT

Product,

SUM(Quantity) AS Total_Quantity,

SUM(Price * Quantity) AS Total_Revenue

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`

GROUP BY Product;