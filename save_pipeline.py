import joblib
from src.features.pipeline import build_manual_pipeline, loading_model_df
from sklearn.linear_model import LogisticRegression

df = loading_model_df()
X_df = df.drop(columns=['customerID','churn_flag'])

X, feature_names = build_manual_pipeline(X_df)
y = df['churn_flag'].values

model = LogisticRegression(max_iter=1000, class_weight = 'balanced')
model.fit(X,y)

joblib.dump({  
  'imputer': imputer,
  'scaler':   scaler,
  'encoder':  encoder,
  'model':    model
}, 'models/prepro_pipeline.pkl')