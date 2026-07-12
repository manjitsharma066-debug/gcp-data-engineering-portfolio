CREATE OR REPLACE TABLE
`gcp-data-engineering-manjit.ecommerce.sales_partitioned`

PARTITION BY Order_Date

AS

SELECT *

FROM
`gcp-data-engineering-manjit.ecommerce.sales_native`;