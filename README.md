# 🔍 Bank Transaction Fraud Detection

---

## 📊 Overview

This project implements a production-ready fraud detection system using unsupervised machine learning. It combines three complementary anomaly detection algorithms with comprehensive feature engineering and statistical feature selection to identify potentially fraudulent bank transactions.

**Key Results:**
- ✅ Ensemble of 3 models (Isolation Forest, LOF, One-Class SVM)
- ✅ 44% feature reduction (80 → 45 features) via 6 statistical methods
- ✅ Multiple confidence levels for prioritized investigation
- ✅ Geographic and temporal pattern analysis

---

## 🎯 Approach

### 1. Feature Engineering (20+ Features)
- **Customer Behavior**: Spending patterns, deviations from normal
- **Merchant Analysis**: Rare merchants, first-time interactions
- **Temporal Patterns**: Unusual hours, rapid transactions, velocity
- **Interactions**: Amount × time, amount × merchant type

### 2. Statistical Feature Selection
Six methods with ensemble voting:
- Variance threshold & correlation filtering
- VIF (multicollinearity detection)
- Mutual Information & F-test
- Recursive Feature Elimination (RFE)

### 3. Anomaly Detection Ensemble
| Model | Strength |
|-------|----------|
| **Isolation Forest** | Global outliers, fast |
| **Local Outlier Factor** | Local density anomalies |
| **One-Class SVM** | High-dimensional boundaries |

**Strategy**: "Any model" voting maximizes recall (catch all potential fraud)

---

## 🚀 Quick Start

### Installation
```bash
# Install dependencies
pip install -r requirements.txt

# Launch notebook
jupyter notebook fraud_detection_enhanced.ipynb
```

### Data Requirements
Place in `data/` folder:
- `bank_transactions_data.csv` - Transaction data
- `gz_2010_us_040_00_5m.json` - US states GeoJSON
- `us_cities.csv` - City coordinates

**Source**: [Kaggle Bank Transaction Dataset](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)

---

## 📁 Project Structure

```
bank_fraud_dataset/
├── artifacts
│   ├── geopandas
│   │   └── gz_2010_us_040_00_5m.json
│   └── results
│       ├── feature_selection_voting.csv
│       ├── flagged_fraud_transactions.csv
│       ├── fraud_detection_results.csv
│       └── high_confidence_fraud.csv
├── data
│   └── bank_transactions_data.csv
├── notebooks
│   └── fraud_detection.ipynb
├── README.md
└── requirements.txt
```

---

## 📈 Notebook Sections

1. **Setup & Imports** - Configuration
2. **Data Loading** - Read and prepare data
3. **EDA** - Comprehensive exploratory analysis
4. **Feature Engineering** - Create 20+ features
5. **Feature Selection** - Statistical reduction (6 methods)
6. **Preprocessing** - Scaling and preparation
7. **Model Training** - Ensemble of 3 algorithms
8. **Results Analysis** - Fraud patterns and insights
9. **Export** - Generate output files
10. **Conclusions** - Findings and recommendations

**Runtime**: ~10-15 minutes

---

## 📊 Outputs

The notebook generates:

| File | Contents |
|------|----------|
| `fraud_detection_results.csv` | All transactions with fraud scores |
| `flagged_fraud_transactions.csv` | High-risk transactions only |
| `high_confidence_fraud.csv` | 2+ model agreement (highest priority) |
| `feature_selection_voting.csv` | Feature selection details |

---

## 🔧 Key Parameters

```python
# Model configuration
CONTAMINATION = 0.05          # Expected fraud rate (5%)
MIN_VOTES_REQUIRED = 1        # Models needed to flag (1-3)

# Feature selection
MI_TOP_K = 50                 # Top features by Mutual Information
F_TEST_TOP_K = 50             # Top features by F-test
RFE_N_FEATURES = 40           # RFE target features

# Ensemble voting
HIGH_CONFIDENCE_THRESHOLD = 2  # Models for high confidence
```

---

## 💡 Technical Highlights

### Feature Selection Pipeline
```
80 features
  ↓ Variance filter
  ↓ Correlation filter (>0.9)
  ↓ VIF filter (>10)
  ↓ MI + F-test + RFE
  ↓ Ensemble voting
45 final features (44% reduction)
```

### Top Fraud Indicators
1. Large deviation from customer's normal spending
2. Transactions with rare merchants
3. Unusual transaction timing (late night/early morning)
4. Rapid consecutive transactions (<30 min)
5. High amounts on weekends

---

## 📦 Dependencies

```
pip install -r requirements.txt
```

---

## 📊 Sample Results

**Typical Detection**:
- Total Transactions Analyzed: 2,464
- Fraud Detected (High Recall): 254 (10.31%)
- High Confidence Fraud (3+ votes): 19 (0.77%)

---

## 🚧 Limitations

- Small sample size
- No ground truth labels (unsupervised approach)
- High recall → more false positives to review
- Requires manual investigation of flagged transactions
- Model needs retraining as fraud patterns evolve

---


---

## 👤 Author

**Stéphan Grigorescu**
Data Scientist | Machine Learning Engineer

- 🌐 Portfolio: [stephan-gs.work](https://stephan-gs.work)
- 💼 LinkedIn: [https://www.linkedin.com/in/st%C3%A9phan-grs/]
- 📧 Email: stephan.grigorescu@gmail.com

---

## 🙏 Acknowledgments

- Dataset: [Kaggle Bank Transaction Dataset](https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection)

---

## 📝 License

MIT License - Free to use with attribution

---
