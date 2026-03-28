#  Olist E-Commerce Big Data Pipeline
## Big Data Assignment 1

### Team Members
- Eman Mohammed 222000058
- Ahmed Ismail 23100854


---

## 📦 Dataset
**Brazilian E-Commerce by Olist**  
Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce  
Files used: orders, customers, order items, products, reviews

---

## 🔄 Execution Flow
```
olist_merged.csv
      ↓
ingest.py        → data_raw.csv
      ↓
preprocess.py    → data_preprocessed.csv
      ↓
analytics.py     → insight1.txt, insight2.txt, insight3.txt
      ↓
visualize.py     → summary_plot.png
      ↓
cluster.py       → clusters.txt
```

---

## 🐳 Docker Commands

### Build the image:
```bash
docker build -t olist-pipeline .
```

### Run the full pipeline:
```bash
./summary.sh
```

---

## 📁 Project Structure
```
customer-analytics/
├── Dockerfile
├── ingest.py
├── preprocess.py
├── analytics.py
├── visualize.py
├── cluster.py
├── summary.sh
├── README.md
└── results/
    ├── data_preprocessed.csv
    ├── insight1.txt
    ├── insight2.txt
    ├── insight3.txt
    ├── summary_plot.png
    └── clusters.txt
```

---

## 📊 Sample Outputs

### Insights:
- Average product price and freight value analysis
- Customer review score distribution
- Top product categories by order count

### Clustering:
- K-Means with 3 clusters on price, freight, and review score
```

---

