# 📊 Sales Analytics Dashboard

An end-to-end data analytics project built on the **Superstore Sales dataset**, covering data ingestion, cleaning, SQL analysis, and an interactive Streamlit dashboard with Plotly visualizations.

> Built as a portfolio project demonstrating the full data analyst workflow: raw data → cleaning → SQL → storytelling dashboard.

---

## 🖥️ Live Demo

> _Deploy to Render and paste your URL here_  
> `https://your-app-name.onrender.com`

---

## 📁 Project Structure

```
sales-analytics/
│
├── data/
│   ├── raw/                  # Original Superstore CSV
│   └── processed/            # Cleaned CSV output
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb    # Pandas cleaning & feature engineering
│   ├── 02_eda.ipynb              # Exploratory data analysis & charts
│   └── 03_sql_analysis.ipynb    # SQL queries via SQLAlchemy
│
├── database/
│   ├── schema.sql            # Table schema reference
│   ├── queries.sql           # Analytical SQL queries
│   └── sales.db              # SQLite database (auto-generated)
│
├── dashboard/
│   ├── app.py                # Streamlit dashboard (main entry point)
│   ├── charts.py             # Plotly chart functions
│   └── utils.py              # Helper utilities
│
├── load_data.py              # CSV → SQLite loader
├── requirements.txt
└── README.md
```

---

## 🔍 Key Features

- **Data Cleaning** — handled nulls, fixed date types, engineered features: profit margin, ship days, order month/year
- **Exploratory Analysis** — sales by category/region, monthly trends, top sub-categories by profit
- **SQL Analysis** — window functions (MoM growth), cohort analysis (customer LTV), discount impact on profit
- **Interactive Dashboard** — filter by year and region, live KPI metrics, Plotly charts
- **Business Narrative** — insights framed as actionable recommendations, not just visuals

---

## 📊 Dashboard Preview

| KPI Cards | Sales by Category | Monthly Trend |
|-----------|-------------------|---------------|
| Total Sales, Profit, Margin, Orders | Grouped bar chart | Line chart with markers |

---

## 🛠️ Tech Stack

| Layer | Tools |
|-------|-------|
| Data manipulation | Python, Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Database | SQLite, SQLAlchemy |
| Dashboard | Streamlit |
| Notebook | Jupyter (VS Code) |

---

## ⚙️ Setup & Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/your-username/sales-analytics.git
cd sales-analytics
```

### 2. Create a virtual environment
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the dataset
Download the [Superstore dataset from Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) and place it at:
```
data/raw/superstore.csv
```

### 5. Load data into SQLite
```bash
python load_data.py
```

### 6. Run the dashboard
```bash
streamlit run dashboard/app.py
```

The app will open at `http://localhost:8501`

---

## 📓 Notebooks Walkthrough

| Notebook | Description |
|----------|-------------|
| `01_data_cleaning.ipynb` | Load raw CSV, handle data types, engineer `Profit Margin`, `Ship Days`, `Order Year/Month`, remove duplicates |
| `02_eda.ipynb` | Seaborn/Matplotlib charts — sales by category, regional profit margin, monthly sales trend, top sub-categories |
| `03_sql_analysis.ipynb` | SQL queries for region summary, MoM growth (window functions), top 10 customers by LTV, discount impact analysis |

---

## 🔑 Key SQL Queries

**Month-over-Month Sales Growth (Window Function)**
```sql
SELECT strftime('%Y-%m', "Order Date") AS month,
       ROUND(SUM(Sales), 2) AS monthly_sales,
       ROUND(SUM(Sales) - LAG(SUM(Sales)) OVER (ORDER BY strftime('%Y-%m',"Order Date")), 2) AS mom_change
FROM sales
GROUP BY month
ORDER BY month;
```

**Discount Impact on Profit**
```sql
SELECT
  CASE
    WHEN Discount = 0    THEN '0%'
    WHEN Discount <= 0.2 THEN '1–20%'
    WHEN Discount <= 0.4 THEN '21–40%'
    ELSE '40%+'
  END AS discount_band,
  COUNT(*) AS orders,
  ROUND(AVG(Profit), 2) AS avg_profit
FROM sales
GROUP BY discount_band
ORDER BY avg_profit DESC;
```

---

## 💡 Business Insights

1. **Technology** drives the highest sales but **Office Supplies** have the most consistent margins
2. **Heavy discounting (40%+) destroys profit** — average profit turns negative beyond 40% discount
3. The **West region** leads in both sales and profit; **Central** underperforms on margin despite decent volume
4. **Q4 consistently peaks** — seasonal demand spike worth targeting with inventory and promotions

---

## 🚀 Deployment

This app is deployed on **Render** as a web service:

1. Push this repo to GitHub
2. Go to [render.com](https://render.com) → New Web Service → Connect your repo
3. Set build command: `pip install -r requirements.txt`
4. Set start command: `streamlit run dashboard/app.py --server.port $PORT --server.address 0.0.0.0`

---

## 📄 Dataset

- **Source:** [Superstore Sales — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Rows:** ~9,994 orders
- **Period:** 2014–2017
- **Features:** 21 columns including Order ID, Customer, Region, Category, Sales, Profit, Discount

---

## 👤 Author

**Devendra**  
[GitHub](https://github.com/your-username) · [LinkedIn](https://linkedin.com/in/your-profile)