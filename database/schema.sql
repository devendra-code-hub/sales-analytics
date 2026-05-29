-- schema.sql  (reference only, table is auto-created by load_data.py)
CREATE TABLE IF NOT EXISTS sales (
    "Row ID"        INTEGER,
    "Order ID"      TEXT,
    "Order Date"    TEXT,
    "Ship Date"     TEXT,
    "Ship Mode"     TEXT,
    "Customer ID"   TEXT,
    "Customer Name" TEXT,
    "Segment"       TEXT,
    "Region"        TEXT,
    "Category"      TEXT,
    "Sub-Category"  TEXT,
    "Product Name"  TEXT,
    "Sales"         REAL,
    "Quantity"      INTEGER,
    "Discount"      REAL,
    "Profit"        REAL
);