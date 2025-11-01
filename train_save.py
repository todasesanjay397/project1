import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import joblib
import os

CSV = "pcod 2.csv"  # place CSV here or update path

print(f"Reading CSV file: {CSV}")
try:
    df = pd.read_csv(CSV)
    print("Successfully read CSV file")
    df.columns = [c.strip() for c in df.columns]
    print("Column names:", df.columns.tolist())
except Exception as e:
    print(f"Error reading CSV file: {str(e)}")
    exit(1)

# Adjust column mapping if your CSV has different names
df = df.rename(columns={
    'I   beta-HCG(mIU/mL)': 'Beta_HCG_I',
    'II    beta-HCG(mIU/mL)': 'Beta_HCG_II',
    'AMH(ng/mL)': 'AMH',
    'PCOS (Y/N)': 'PCOS'
})

df = df[['Beta_HCG_I', 'Beta_HCG_II', 'AMH', 'PCOS']].apply(pd.to_numeric, errors='coerce').dropna()
df['PCOS'] = df['PCOS'].astype(int)

X = df[['Beta_HCG_I', 'Beta_HCG_II', 'AMH']].values
y = df['PCOS'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save
try:
    print("Saving model files...")
    joblib.dump(model, "rf_model.joblib")
    joblib.dump(scaler, "scaler.joblib")
    print(f"Successfully saved files:")
    print(f"  - rf_model.joblib (size: {os.path.getsize('rf_model.joblib')} bytes)")
    print(f"  - scaler.joblib (size: {os.path.getsize('scaler.joblib')} bytes)")
    
    # Print model details and data summary
    print("\nData Summary:")
    print(f"Total number of samples: {len(df)}")
    print("\nFeature statistics:")
    print(df[['Beta_HCG_I', 'Beta_HCG_II', 'AMH']].describe())
    print(f"\nPCOS Distribution:")
    print(df['PCOS'].value_counts(normalize=True).mul(100).round(2).astype(str) + '%')
    
    # Model performance
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    print(f"\nModel Performance:")
    print(f"Training accuracy: {train_score:.2%}")
    print(f"Testing accuracy: {test_score:.2%}")
    
except Exception as e:
    print(f"Error saving model files: {str(e)}")
    exit(1)
