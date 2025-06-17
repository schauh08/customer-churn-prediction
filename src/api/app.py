import os, sys, joblib, pandas as pd
from flask import Flask, request, jsonify

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..','..'))
sys.path.insert(0, project_root)

app = Flask(__name__)
pipeline = joblib.load(os.path.join(project_root, 'models', 'churn_pipeline.pkl'))

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    df_new = pd.DataFrame([data])
    proba = pipeline.predict_proba(df_new)[0,1]
    return jsonify({'churn_probability': float(proba)})

if __name__ == '__main__':
    app.run(debug=True)

