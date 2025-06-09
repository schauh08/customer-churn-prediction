import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import os 

def loading_model_df():

    script_dir = os.path.dirname(__file__)
    project_root = os.path.abspath(os.path.join(script_dir, os.pardir, os.pardir))
    db_path = os.path.join(project_root,'churn.db')
    engine = create_engine(f'sqlite:///{db_path}', echo=False)
    return pd.read_sql_table('modeling_churn', engine)
    
    
def build_manual_pipeline(df):

    numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'avg_monthly_charge']
    categorical_features = ['InternetService','Contract', 'PaymentMethod', 'tenure_bucket', 'OnlineSecurity', 'OnlineBackup', 'DeviceProtection', 'TechSupport',           'StreamingTV', 'StreamingMovies']

    print(df[numeric_features].dtypes)

    for col in numeric_features:
        bad = df[col].apply(lambda x: isinstance(x,str))
        if bad.any():
            print(f"Non-numeric values in {col}:\n", df. loc[bad, col].unique())

    df[numeric_features] = (
        df[numeric_features]
        .applymap(lambda x: str(x).strip())
        .applymap(pd.to_numeric, error ='coerce')
    )
    
    
    df.dropna(subset=numeric_features)

    scaler = StandardScaler()
    num_arr = scaler.fit_transform(df[numeric_features])


    encoder = OneHotEncoder(drop='first', sparse_output='False')
    cat_arr = encoder.fit_transform(df[categorical_features].isna().sum())
    
    x = np.hstack([num_arr, cat_arr])
    feature_names = numeric_features + list(encoder.get_features_names_out(categorical_features))
    return X, feature_names

    
