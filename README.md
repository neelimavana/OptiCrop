# OptiCrop — Smart Agricultural Production Optimization Engine

OptiCrop is a machine-learning powered web app that recommends the most suitable
crop for a given set of soil and climate conditions. A user enters Nitrogen (N),
Phosphorous (P), Potassium (K), temperature, humidity, pH, and rainfall values,
and the app returns the crop best suited to those exact conditions.

**Live repository**: https://github.com/neelimavana/OptiCrop

## Problem statement

Farmers often choose crops based on tradition or general regional advice rather
than the actual measured soil and climate conditions on their land, which leads
to lower yields and wasted resources. OptiCrop replaces that guesswork with a
trained classifier that maps soil/climate inputs directly to a crop recommendation.

## Tech stack

- **ML**: NumPy, Pandas, Scikit-learn, SciPy
- **Visualization**: Matplotlib, Seaborn
- **Web**: Flask
- **Dataset**: [Crop Recommendation Dataset](https://www.kaggle.com/datasets/chitrakumari25/smart-agricultural-production-optimizing-engine) — N, P, K, temperature, humidity, ph, rainfall → label (22 balanced crop classes, 100 samples each)

## Repository structure

The OptiCrop repository is organized as follows:

OptiCrop/
├── app.py	← Main Flask application (routes, prediction logic)
├── requirements.txt	← All Python dependencies
├── README.md	← Setup instructions and project overview
├── .gitignore
├── data/
│ └── Crop_recommendation.csv ← Training dataset (2,200 rows, 22 crops)
├── model/
│  ├── model.pkl	← Trained Random Forest classifier (99.55% accuracy)
│  ├── scaler.pkl	← Fitted StandardScaler
│  └── label_encoder.pkl	← LabelEncoder for crop name decoding
├── notebooks/
│ └── EDA_and_Model_Training.ipynb ← Full ML pipeline notebook
├── templates/
│  ├── home.html
│ ├── about.html
│  └── find_your_crop.html
└── static/
└── style.css
