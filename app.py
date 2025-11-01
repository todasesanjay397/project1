from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import joblib
import numpy as np
import os

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

MODEL_PATH = "rf_model.joblib"
SCALER_PATH = "scaler.joblib"

# Do not fail on startup if model isn't present; show helpful message
model = None
scaler = None
if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
else:
    print("Warning: rf_model.joblib or scaler.joblib not found. Run train_save.py to generate them.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return jsonify({'error': 'Model not available on server. Please run train_save.py to generate rf_model.joblib and scaler.joblib.'}), 500
    data = request.get_json(force=True)
    try:
        b1 = float(data.get('beta_hcg_i'))
        b2 = float(data.get('beta_hcg_ii'))
        amh = float(data.get('amh'))
    except Exception:
        return jsonify({'error': 'Invalid input. Provide numeric beta_hcg_i, beta_hcg_ii, amh.'}), 400

    X = np.array([[b1, b2, amh]])
    Xs = scaler.transform(X)
    pred = int(model.predict(Xs)[0])
    prob = None
    if hasattr(model, 'predict_proba'):
        prob = float(model.predict_proba(Xs)[0].max())

    label = 'PCOS Positive' if pred == 1 else 'PCOS Negative'
    result = {'prediction': pred, 'label': label}
    if prob is not None:
        result['probability'] = round(prob, 4)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
