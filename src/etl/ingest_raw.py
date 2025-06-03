import pandas as pd
from sqlalchemy import create_engine
import os

script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
csv_path = os.path.join(project_root, 'data', 'raw', 'WA_Fn-UseC_-Telco-Customer-Churn.csv')

db_path = os.path.join(project_root, 'churn.db')
engine = create_engine('sqlite:///churn.db', echo=False)

churn_df = pd.read_csv(csv_path)

churn_df.to_sql('raw_churn', engine, if_exists='replace', index=False)

print(f"Ingested {len(churn_df)} rows into raw_churn")
