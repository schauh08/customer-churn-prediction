import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
import os 

def loading_model_df():

    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
    db_path = os.path.join(project_root,'churn.db')
    engine = create_engine(f'sqlite:///{db_path}', echo=False)
    return pd.read_sql_table('modeling_churn', engine)
    
    
def build_manual_pipeline(df):

    numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'avg_monthly_charge']
    categorical_features = ['InternetService','Contract', 'PaymentMethod', 'tenure_bucket', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',               'TechSupport','StreamingTV', 'StreamingMovies']

    for col in numeric_features:
        df[col] = pd.to_numeric(df[col].astype(str).str.strip(), errors='coerce')

    
    imputer = SimpleImputer(strategy='median')
    num_imputed = imputer.fit_transform(df[numeric_features])
    

    scaler = StandardScaler()
    num_arr = scaler.fit_transform(num_imputed)


    encoder = OneHotEncoder(drop='first', sparse_output=False)
    cat_arr = encoder.fit_transform(df[categorical_features])
    
    X = np.hstack([num_arr, cat_arr])
    feature_names = numeric_features + list(encoder.get_feature_names_out(categorical_features))
    return X, feature_names

    
