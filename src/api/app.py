import joblib
import pandas as pd
from flask import Flask, request, jsonify
from src.features.pipeline import build_manual_pipeline

app = Flask(__name__)

artefact = joblib.load('model/churn_pipeline.pk1')
model = artefact['model']
feature_names = artefact['feature_names']

def predict():

    data = request.get_json()
    if not data:
        return jsonify({'Error': 'Invalid or Missing JSON Payload'}), 400

    df = pd.DataFrame([data])

    X, _ = build_manual_pipeline(df)

    proba = model.predict_proba(X)[0,1]


    return jsonify({
        'churn_probability': float(proba)
    })

if __name__ = '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

