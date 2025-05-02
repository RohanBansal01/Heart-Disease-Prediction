
# ❤️🩺 Heart Disease Prediction System

A beginner-friendly, Flask-based web application that predicts the risk of heart disease using machine learning models (XGBoost, Scikit-learn). The app is deployed on Render for public access.

![Python](https://img.shields.io/badge/Python-3.9-blue)
![Flask](https://img.shields.io/badge/Flask-2.3-green)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost%2C%20Scikit--learn-orange)
![Status](https://img.shields.io/badge/Status-Live-green)

---

## 🌟 Features

- ✅ User-friendly web interface  
- ✅ Real-time heart disease risk prediction  
- ✅ 85%+ model accuracy (tested on UCI Heart Disease dataset)  
- ✅ Fully responsive design for mobile and desktop  
- ✅ Input validation and secure form handling  
- ✅ Easily customizable for other medical ML projects

---

## 🚀 Live Demo

Check out the deployed app on Render:  
🔗 **[https://heartcure.onrender.com](https://heartcure.onrender.com)**  
> _Note: May take 15–30 seconds to wake up if inactive (Render free tier)_

---

## 📸 Screenshots

> *(Optional: Add screenshots in `/docs` folder and embed them like below)*  
<!-- ![App Screenshot](docs/screenshot1.png) -->

---

## 🛠️ Local Development Setup

### Prerequisites

- Python 3.9  
- [Anaconda](https://www.anaconda.com/) (recommended)  
- Git

### Step-by-Step Guide

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/heartcure.git
   cd heartcure
````

2. **Create a virtual environment using Conda**

   ```bash
   conda create -n heartcure python=3.9
   conda activate heartcure
   ```

3. **Install the required packages**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask app**

   ```bash
   flask run
   ```

   Open your browser and visit: [http://localhost:5000](http://localhost:5000)

---

## 📁 Project Structure

```
heartcure/
├── static/          # CSS, JS, and image assets
├── templates/       # HTML templates (Jinja2)
├── model/           # Trained ML model and preprocessing files
├── app.py           # Main Flask application
├── requirements.txt # Python dependencies
├── Procfile         # Render deployment configuration
└── README.md        # Project documentation
```

---

## 🧠 Machine Learning Model Details

* **Algorithm**: XGBoost Classifier
* **Dataset**: UCI Heart Disease Dataset
* **Features Used**: Age, Sex, Chest Pain Type, Blood Pressure, Cholesterol, etc.
* **Accuracy**: \~85% on validation data
* **Preprocessing**:

  * Missing value handling
  * Label encoding of categorical variables
  * Feature scaling using `StandardScaler`
* **Model Training Notebook**: `model/HeartDiseaseModel.ipynb` *(optional to include)*

---

## 🐞 Troubleshooting

* `ModuleNotFoundError`: Run `pip install -r requirements.txt`
* `gunicorn` errors on Render: Ensure `gunicorn==20.1.0` is in your `requirements.txt`
* App not loading after deployment:

  * Check your `Procfile`
  * Log in to Render dashboard and review build logs


