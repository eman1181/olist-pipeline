import sys
import pandas as pd
import subprocess

df = pd.read_csv(sys.argv[1])

print("🔄 Generating insights...")

# Average price and freight value 
avg_price = df["price"].mean()
avg_freight = df["freight_value"].mean()

insight1 = f"""E-Commerce Price Insights
==========================
- Average product price (normalized): {avg_price:.4f}
- Average freight value (normalized): {avg_freight:.4f}
- This suggests freight cost is {'high' if avg_freight > avg_price else 'low'} relative to product price.
"""

with open("insight1.txt", "w") as f:
    f.write(insight1)
print("✅ insight1.txt saved!")

# Review score distribution
review_mean = df["review_score"].mean()
review_std = df["review_score"].std()

insight2 = f"""Customer Review Score Insights
================================
- Average review score (normalized): {review_mean:.4f}
- Standard deviation: {review_std:.4f}
- Customer satisfaction is {'high' if review_mean > 0.6 else 'moderate' if review_mean > 0.4 else 'low'}.
"""

with open("insight2.txt", "w") as f:
    f.write(insight2)
print("✅ insight2.txt saved!")

#  Top product categories 
top_categories = df["product_category_name"].value_counts().head(5)

insight3 = f"""Top Product Categories
=======================
The 5 most ordered product categories (encoded values):
{top_categories.to_string()}

- The most dominant category code is: {top_categories.idxmax()}
- It accounts for {top_categories.max()} orders in the dataset.
"""

with open("insight3.txt", "w") as f:
    f.write(insight3)
print("✅ insight3.txt saved!")

subprocess.run(["python", "visualize.py", "data_preprocessed.csv"])