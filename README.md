# 🌾 OptiCrop - Smart Agricultural Production Optimization Engine

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Flask-Web%20Application-black?logo=flask" />
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/badge/Status-Completed-brightgreen" />
</p>

<p align="center">
  <b>🌱 AI-powered Crop Recommendation System using Machine Learning</b><br>
  Helping farmers choose the most suitable crop based on soil nutrients and climatic conditions.
</p>

---

# 📖 About the Project

OptiCrop is a Machine Learning-powered web application that recommends the most suitable crop for cultivation based on soil nutrients and environmental conditions.

The user provides:

- 🌿 Nitrogen (N)
- 🌿 Phosphorus (P)
- 🌿 Potassium (K)
- 🌡 Temperature
- 💧 Humidity
- ⚖ Soil pH
- 🌧 Rainfall

The trained Random Forest model analyzes these parameters and predicts the crop that is most likely to produce the best yield.

---

# 🎯 Problem Statement

Farmers often rely on traditional farming practices or regional assumptions while selecting crops. However, soil composition and climatic conditions vary significantly even within the same region.

Choosing an unsuitable crop can result in:

- ❌ Lower productivity
- ❌ Poor soil utilization
- ❌ Higher farming costs
- ❌ Reduced profitability

OptiCrop addresses this challenge by leveraging Machine Learning to provide data-driven crop recommendations based on actual field conditions.

---

# ✨ Features

✅ Crop Recommendation

✅ Machine Learning Prediction

✅ Simple User Interface

✅ Flask Web Application

✅ Fast Response Time

✅ High Prediction Accuracy

✅ Responsive Design

---

# 🛠 Tech Stack

| Category | Technologies |
|----------|--------------|
| Programming | Python |
| Backend | Flask |
| Machine Learning | Scikit-Learn |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model | Random Forest Classifier |
| Frontend | HTML, CSS |
| IDE | Jupyter Notebook |

---

# 📊 Dataset

**Source**

🔗 https://www.kaggle.com/datasets/chitrakumari25/smart-agricultural-production-optimizing-engine

### Dataset Information

| Attribute | Description |
|------------|-------------|
| Total Records | 2200 |
| Crop Classes | 22 |
| Samples per Crop | 100 |
| Features | 7 |
| Target | Crop Name |

### Input Features

| Feature | Description |
|----------|-------------|
| N | Nitrogen |
| P | Phosphorus |
| K | Potassium |
| Temperature | °C |
| Humidity | % |
| pH | Soil pH |
| Rainfall | mm |

---

# 🤖 Machine Learning Model

### Algorithm Used

🌳 Random Forest Classifier

### Preprocessing

- StandardScaler
- LabelEncoder

### Model Accuracy

🎯 **99.55%**

---

# 📂 Repository Structure

```text
OptiCrop/
│
├── app.py                     # Main Flask application
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── .gitignore
│
├── data/
│   └── Crop_recommendation.csv
│
├── model/
│   ├── model.pkl
│   ├── scaler.pkl
│   └── label_encoder.pkl
│
├── notebooks/
│   └── EDA_and_Model_Training.ipynb
│
├── templates/
│   ├── home.html
│   ├── about.html
│   └── find_your_crop.html
│
└── static/
    └── style.css
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/neelimavana/OptiCrop.git
```

## Navigate

```bash
cd OptiCrop
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Run Application

```bash
python app.py
```

---

# 🚀 Usage

1. Open the application in your browser.
2. Enter soil nutrient values.
3. Enter temperature, humidity, pH, and rainfall.
4. Click **Predict**.
5. View the recommended crop.

---

# 🔄 Project Workflow

```text
User Input
      │
      ▼
Input Validation
      │
      ▼
Feature Scaling
      │
      ▼
Random Forest Model
      │
      ▼
Crop Prediction
      │
      ▼
Display Result
```

---

# 🏗 System Architecture

```text
              User
                │
                ▼
        Flask Web Application
                │
                ▼
      Data Preprocessing
                │
                ▼
     Random Forest Classifier
                │
                ▼
      Recommended Crop
```

---

# 📸 Application Screenshots

> Add your screenshots in a `screenshots/` folder and update the paths below.

| Home Page | Crop Prediction |
|------------|-----------------|
| ![](screenshots/home.png) | ![](screenshots/predict.png) |

| Result | About Page |
|---------|------------|
| ![](screenshots/result.png) | ![](screenshots/about.png) |

---

# 📈 Model Performance

| Metric | Value |
|--------|-------|
| Accuracy | 99.55% |
| Algorithm | Random Forest |
| Classes | 22 |
| Dataset Size | 2200 Samples |

---

# 🔮 Future Enhancements

- 🌦 Real-time weather integration
- 📍 GPS-based recommendations
- 🌾 Fertilizer recommendation
- 🦠 Crop disease prediction
- 📱 Android application
- ☁ Cloud deployment
- 🌍 Multi-language support

---

# 👩‍💻 Author

**Neelima Vana**

- GitHub: https://github.com/neelimavana
- LinkedIn: https://linkedin.com/in/neelima-vana

---

# ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

# 📄 License

This project is licensed under the MIT License.
