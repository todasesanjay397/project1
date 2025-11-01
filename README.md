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

## Project Overview
This is our PCOS-ML based project

Team name: Innovators
Team Member Name: 1.Asmita Sanjay Todase
                  2.Anushka Hanmant Sonwane
Frontend: HTML
Backend: Python, API flask
MODEL: RANDOM FOREST

## Technical Implementation

### 1. Project Architecture
```
project1/
├── app.py                 # Flask application server
├── train_save.py         # Model training script
├── requirements.txt      # Python dependencies
├── pcod 2.csv           # Dataset
├── rf_model.joblib      # Trained Random Forest model
├── scaler.joblib        # StandardScaler for data normalization
├── static/
│   ├── main.js          # Frontend JavaScript
│   └── styles.css       # CSS styles
└── templates/
    └── index.html       # Main web interface
```

### 2. Technical Stack
- **Backend Framework**: Flask (Python)
- **Machine Learning**: scikit-learn
- **Model**: Random Forest Classifier
- **Data Processing**: pandas, numpy
- **Model Serialization**: joblib
- **Frontend**: HTML, CSS, JavaScript
- **CORS Support**: flask-cors

### 3. Model Details
- **Algorithm**: Random Forest Classifier
- **Features**:
  - Beta HCG I (First measurement)
  - Beta HCG II (Second measurement)
  - AMH (Anti-Mullerian Hormone)
- **Target Variable**: PCOS (Positive/Negative)
- **Data Preprocessing**: StandardScaler
- **Model Performance**:
  - Training Accuracy: 98.38%
  - Testing Accuracy: 70.37%

### 4. API Endpoints
1. **Home Page**
   - Route: `/`
   - Method: GET
   - Returns: Web interface

2. **Prediction API**
   - Route: `/predict`
   - Method: POST
   - Input JSON Format:
     ```json
     {
       "beta_hcg_i": float,
       "beta_hcg_ii": float,
       "amh": float
     }
     ```
   - Response Format:
     ```json
     {
       "prediction": int,       // 0 or 1
       "label": string,        // "PCOS Negative" or "PCOS Positive"
       "probability": float    // Confidence score
     }
     ```

### 5. Dataset Statistics
- Total Samples: 540
- Features Distribution:
  ```
  Beta HCG I:
    Mean: 665.70
    Median: 19.38
    Range: 1.30 to 32,460.97
  
  Beta HCG II:
    Mean: 238.67
    Median: 1.99
    Range: 0.11 to 25,000.00
  
  AMH:
    Mean: 5.62
    Median: 3.70
    Range: 0.10 to 66.00
  ```
- Class Distribution:
  - PCOS Negative: 67.22%
  - PCOS Positive: 32.78%

### 6. Implementation Notes
- Model uses stratified sampling to handle class imbalance
- CORS enabled for API access
- Comprehensive error handling for invalid inputs
- Lazy loading of model and scaler
- Real-time predictions with confidence scores
- Standardized data preprocessing pipeline
