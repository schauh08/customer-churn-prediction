import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///churn.db')

churn_df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

churn_df.to_sql('raw_churn', engine, if_exists='replace', index=false)

print(f"Ingested {len(df)} rows into raw_churn")
