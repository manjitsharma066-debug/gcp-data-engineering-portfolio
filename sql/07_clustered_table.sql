CREATE OR REPLACE TABLE
`gcp-data-engineering-manjit.ecommerce.sales_clustered`

PARTITION BY Order_Date

CLUSTER BY
Customer_ID,
Product

AS

SELECT *

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`;