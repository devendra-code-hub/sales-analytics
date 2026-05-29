-- queries.sql

-- 1. Revenue and profit by region
SELECT Region,
       ROUND(SUM(Sales), 2)  AS total_sales,
       ROUND(SUM(Profit), 2) AS total_profit,
       ROUND(AVG(Profit / NULLIF(Sales,0)) * 100, 2) AS avg_margin_pct
FROM sales
GROUP BY Region
ORDER BY total_sales DESC;

-- 2. Month-over-month sales (window function)
SELECT strftime('%Y-%m', "Order Date") AS month,
       ROUND(SUM(Sales), 2) AS monthly_sales,
       ROUND(SUM(Sales) - LAG(SUM(Sales)) OVER (ORDER BY strftime('%Y-%m',"Order Date")), 2) AS mom_change
FROM sales
GROUP BY month
ORDER BY month;

-- 3. Customer cohort: top 10 customers by lifetime value
SELECT "Customer Name",
       COUNT(DISTINCT "Order ID") AS orders,
       ROUND(SUM(Sales), 2)       AS lifetime_value,
       ROUND(AVG(Sales), 2)       AS avg_order_value
FROM sales
GROUP BY "Customer Name"
ORDER BY lifetime_value DESC
LIMIT 10;

-- 4. Discount impact on profit
SELECT
  CASE
    WHEN Discount = 0          THEN '0%'
    WHEN Discount <= 0.2       THEN '1–20%'
    WHEN Discount <= 0.4       THEN '21–40%'
    ELSE '40%+'
  END AS discount_band,
  COUNT(*) AS orders,
  ROUND(AVG(Profit), 2) AS avg_profit
FROM sales
GROUP BY discount_band
ORDER BY avg_profit DESC;