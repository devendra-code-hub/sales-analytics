# dashboard/app.py
import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

st.set_page_config(page_title="Sales Analytics", layout="wide")
st.title("📊 Sales Analytics Dashboard")

@st.cache_data
def load():
    engine = create_engine("sqlite:///database/sales.db")
    return pd.read_sql("SELECT * FROM sales", engine)

df = load()
df["Order Date"] = pd.to_datetime(df["Order Date"])

# ── Sidebar filters ──────────────────────────────────────────
st.sidebar.header("Filters")
years     = sorted(df["Order Date"].dt.year.unique())
regions   = ["All"] + sorted(df["Region"].unique())
sel_year  = st.sidebar.selectbox("Year", ["All"] + years)
sel_region = st.sidebar.selectbox("Region", regions)

filtered = df.copy()
if sel_year   != "All": filtered = filtered[filtered["Order Date"].dt.year == sel_year]
if sel_region != "All": filtered = filtered[filtered["Region"] == sel_region]

# ── KPI row ──────────────────────────────────────────────────
k1, k2, k3, k4 = st.columns(4)
k1.metric("Total Sales",    f"${filtered['Sales'].sum():,.0f}")
k2.metric("Total Profit",   f"${filtered['Profit'].sum():,.0f}")
k3.metric("Avg Margin",     f"{(filtered['Profit']/filtered['Sales'].replace(0,1)).mean()*100:.1f}%")
k4.metric("Orders",         f"{filtered['Order ID'].nunique():,}")

st.divider()

# ── Charts ───────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sales by Category")
    cat = filtered.groupby("Category")["Sales"].sum().reset_index()
    fig = px.bar(cat, x="Category", y="Sales", color="Category",
                 color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Profit by Region")
    reg = filtered.groupby("Region")["Profit"].sum().reset_index()
    fig = px.pie(reg, names="Region", values="Profit",
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Monthly Sales Trend")
monthly = filtered.copy()
monthly["Month"] = monthly["Order Date"].dt.to_period("M").astype(str)
monthly = monthly.groupby("Month")["Sales"].sum().reset_index()
fig = px.line(monthly, x="Month", y="Sales", markers=True)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 10 Sub-Categories by Sales")
sub = filtered.groupby("Sub-Category")["Sales"].sum().nlargest(10).reset_index()
fig = px.bar(sub, x="Sales", y="Sub-Category", orientation="h",
             color="Sales", color_continuous_scale="teal")
st.plotly_chart(fig, use_container_width=True)