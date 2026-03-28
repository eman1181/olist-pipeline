import sys
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from sklearn.decomposition import PCA
import subprocess

df = pd.read_csv(sys.argv[1])

print("🔄 Starting preprocessing...")
print(f"Original shape: {df.shape}")

#1. Data Cleaning 
# Drop duplicates
df.drop_duplicates(inplace=True)

# Drop columns with too many missing values (>50%)
threshold = len(df) * 0.5
df.dropna(thresh=threshold, axis=1, inplace=True)

# Fill missing numeric values with median
for col in df.select_dtypes(include=np.number).columns:
    df[col].fillna(df[col].median(), inplace=True)

# Fill missing text values with "unknown"
for col in df.select_dtypes(include="object").columns:
    df[col].fillna("unknown", inplace=True)

print(f"After cleaning: {df.shape}")

#2. Feature Transformation 
# Encode categorical columns
le = LabelEncoder()
cat_cols = ["order_status", "customer_state", "product_category_name"]
for col in cat_cols:
    if col in df.columns:
        df[col] = le.fit_transform(df[col].astype(str))

# Scale numeric columns
num_cols = ["price", "freight_value", "review_score", "payment_value"]
num_cols = [c for c in num_cols if c in df.columns]
scaler = MinMaxScaler()
df[num_cols] = scaler.fit_transform(df[num_cols])

print("✅ Feature transformation done!")

# 3. Dimensionality Reduction
# Keep only useful columns
keep_cols = [
    "order_status", "customer_state", "price",
    "freight_value", "review_score", "product_category_name"
]
keep_cols = [c for c in keep_cols if c in df.columns]
df = df[keep_cols]

print(f"✅ After dimensionality reduction: {df.shape}")

# 4. Discretization 
# Bin price into 3 categories
if "price" in df.columns:
    df["price_category"] = pd.cut(
        df["price"],
        bins=3,
        labels=["budget", "mid-range", "premium"]
    )

print("Discretization done!")

# Save result
df.to_csv("data_preprocessed.csv", index=False)
print("Saved as data_preprocessed.csv")

# Call next script
subprocess.run(["python", "analytics.py", "data_preprocessed.csv"])