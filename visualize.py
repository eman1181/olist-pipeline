import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import subprocess

df = pd.read_csv(sys.argv[1])

print("Generating plots...")

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("E-Commerce Data Summary", fontsize=16, fontweight="bold")

# Price Distribution Histogram 
axes[0].hist(df["price"], bins=30, color="steelblue", edgecolor="black")
axes[0].set_title("Price Distribution")
axes[0].set_xlabel("Price (normalized)")
axes[0].set_ylabel("Frequency")

#  Review Score Distribution 
axes[1].hist(df["review_score"], bins=20, color="coral", edgecolor="black")
axes[1].set_title("Review Score Distribution")
axes[1].set_xlabel("Review Score (normalized)")
axes[1].set_ylabel("Frequency")

#  Correlation Heatmap 
num_df = df.select_dtypes(include="number")
sns.heatmap(
    num_df.corr(),
    ax=axes[2],
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    linewidths=0.5
)
axes[2].set_title("Correlation Heatmap")

plt.tight_layout()
plt.savefig("summary_plot.png", dpi=150)
plt.close()

print("summary_plot.png saved!")


subprocess.run(["python", "cluster.py", "data_preprocessed.csv"])