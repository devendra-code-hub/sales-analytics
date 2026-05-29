# load_data.py
import pandas as pd
from sqlalchemy import create_engine
import os

# Create database folder if it doesn't exist
os.makedirs("database", exist_ok=True)


df = pd.read_csv("data/raw/superstore.csv", encoding="latin-1")
engine = create_engine("sqlite:///database/sales.db")
df.to_sql("sales", engine, if_exists="replace", index=False)
print(f"✅ Loaded {len(df)} rows into sales.db")