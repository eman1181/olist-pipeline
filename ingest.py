import sys
import pandas as pd
import subprocess

df = pd.read_csv(sys.argv[1])

df.to_csv("data_raw.csv", index=False)

print(f"✅ Ingest done! Shape: {df.shape}")
print(f"📋 Columns: {list(df.columns)}")

subprocess.run(["python", "preprocess.py", "data_raw.csv"])