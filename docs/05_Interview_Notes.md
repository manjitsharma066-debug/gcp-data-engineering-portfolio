# Interview Notes

## Why Cloud Storage?

Cloud Storage acts as the staging area for batch ETL pipelines.

---

## Why External Table?

Allows querying data without loading it into BigQuery.

---

## Why Native Table?

Provides better performance and supports partitioning and clustering.

---

## Why Partitioning?

Reduces scanned data and query cost.

---

## Why Clustering?

Improves query performance for frequently filtered columns.

---

## Difference between External and Native Tables

External Table

- Data remains in Cloud Storage

Native Table

- Data is stored inside BigQuery