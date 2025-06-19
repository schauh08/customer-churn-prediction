# customer-churn-predication

Customer Churn Prediction & Segmentation

Project Overview
This repository contains an end-to-end solution for predicting customer churn and segmenting customers into actionable cohorts for targeted retention campaigns. Leveraging SQL, Python, and scikit-learn, the project includes data ingestion, feature engineering, modeling, clustering, and a deployed API prototype.

Key Features

ETL Pipeline: Ingest raw CSV into SQLite and build a modeling_churn table with clean, derived features.

Feature Engineering: Automated pipeline for numeric imputation, scaling, and one-hot encoding.

Churn Modeling: Logistic Regression baseline with ROC-AUC 0.82, precision-recall analysis, and feature interpretation.

Customer Segmentation: K-Means clustering (k=4) with cluster profiling and retention tactics.

API Deployment: Flask service exposing /predict endpoint for real-time scoring.

Repository Structure

customer-churn-prediction/
├── README.md
├── LICENSE
├── requirements.txt
├── data/
│   ├── raw/             # Original CSV
├── src/
│   ├── etl/
│   │   ├── ingest_raw.py
│   │   └── build_features.sql
│   ├── features/
│   │   └── pipeline.py
│   ├── modeling
│   │   └── save_pipeline.py
│   └── api/
│       └── app.py
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_model_training.ipynb
│   └── 03_clustering.ipynb
├── models/
│   └── churn_pipeline.pkl
├── reports/
│   └── churn_report.pdf


Setup & Installation

1. Clone the repo

git clone https://github.com/schauh08/customer-churn-prediction.git
cd customer-churn-prediction

2. Create & activate virtual environment

python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate   # macOS/Linux

3. Install dependencies

pip install -r requirements.txt

4. Ingest raw data & build features

python src/etl/ingest_raw.py
sqlite3 churn.db < src/etl/build_features.sql

5. Train & serialize pipeline

python src/modeling/save_pipeline.py

6. Run the API

python src/api/app.py

Usage

Notebooks: Explore notebooks/ for detailed EDA, model evaluation, and clustering workflows.

Batch Scoring: Use scripts/batch_score.py to score a CSV of new customers.

API: Send POST requests to http://127.0.0.1:5000/predict with customer JSON payload.

Contributing

Contributions welcome! Please fork, create a feature branch, and submit a pull request.

License

This project is licensed under the MIT License.
