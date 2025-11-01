# PCOS Predictor — Flask + Random Forest (VS Code Ready)

## What's included
- `train_save.py` — train and save Random Forest model & scaler (produces rf_model.joblib & scaler.joblib)
- `app.py` — Flask backend (serves frontend and /predict API)
- `templates/index.html` — frontend
- `static/main.js` — frontend JS
- `static/styles.css` — frontend CSS
- `requirements.txt` — pip dependencies

## Quick start (local)
1. Copy `pcod 2.csv` into project root.
2. Create virtual env: `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. Install deps: `pip install -r requirements.txt`
4. Train model: `python train_save.py` (creates rf_model.joblib & scaler.joblib)
5. Run server: `python app.py`
6. Open `http://127.0.0.1:5000` in browser.

**Note:** This tool is a predictive aid — not a medical diagnosis. Add disclaimer before use.

This is our PCOS-ML based project

Team name: Innovators
Frontend:HTML
Backend:Python,API flask
MODEL:RANDOM FOREST
