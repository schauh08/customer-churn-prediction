import os
import joblib
import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression

from src.features.pipeline import loading_model_df

df = loading_model_df()
X_df = df.drop(columns=['customerID', 'churn_flag'])
y    = df['churn_flag'].values

numeric_features = ['tenure', 'MonthlyCharges', 'TotalCharges', 'avg_monthly_charge']
categorical_features = [
    'InternetService','Contract','PaymentMethod','tenure_bucket',
    'OnlineSecurity','OnlineBackup','DeviceProtection',
    'TechSupport','StreamingTV','StreamingMovies'
]

preprocessor = ColumnTransformer([
    
    ('num', Pipeline([
        ('impute', SimpleImputer(strategy='median')),
        ('scale',  StandardScaler())
    ]), numeric_features),
    ('cat', OneHotEncoder(drop='first', sparse_output=False), categorical_features),
])

preprocessor.feature_names_in_ = X_df.columns.to_list()

pipeline = Pipeline([
    ('preprocessor', preprocessor),
    ('classifier',   LogisticRegression(
                        max_iter=1000,
                        class_weight='balanced',
                        random_state=42
                    ))
])

pipeline.fit(X_df, y)

os.makedirs('models', exist_ok=True)

output_path = os.path.join('models', 'churn_pipeline.pkl')
joblib.dump(pipeline, output_path)
print(f"Saved full pipeline (preprocessor + model) to {output_path}")
