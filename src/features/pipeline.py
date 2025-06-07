import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os 

script_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
db_path = os.path.join(project_root,'churn.db')
engine = create_engine(f'sqlite:///{db_path}', echo=False)

def loading_model_df():

    df = pd.read_sql_table('modeling_churn', engine)
    return df

def build_feature_pipeline():

    numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'avg_monthly_charge']
    categorical_features = ['InternetService','Contract', 'PaymentMethod', 'tenure_bucket', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(drop='first',sparse_output=False)

    preprocessor = ColumnTransformer(transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat',categorical_transformer,categorical_features)
    ])
    return preprocessor


if __name__ == '__main__':

    df = loading_model_df()
    X = df.drop(columns=['customerID', 'churn_flag'])
    y = df['churn_flag'].values

    pipeline = build_feature_pipeline()
    X_transformed = pipeline.fit_transform(X)

    
    print("Original shape:", X.shape)
    print("Transformed shape:", X_transformed.shape)
