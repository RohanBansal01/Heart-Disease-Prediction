# Heart Disease Prediction Web Application

A beginner-friendly Flask-based web application that predicts the risk of heart disease using machine learning models (XGBoost, Scikit-learn).
The app is built with Python, designed for simplicity and accuracy, and deployed on Render for public access.

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-green?logo=flask)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost%2C%20Scikit--learn-orange)
![Status](https://img.shields.io/badge/Status-Live-success)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 1. Overview

1.1 This project uses a pre-trained machine learning model to predict whether a person is at risk of heart disease based on input parameters such as age, blood pressure, cholesterol levels, and more.

1.2 It provides a clean, responsive, and easy-to-use web interface powered by Flask and a trained ML model built using XGBoost and Scikit-learn.

1.3 You can test the app live on Render (if deployed).

---

# 2. Features

2.1 User-friendly web interface

2.2 Real-time heart disease risk prediction

2.3 99%+ model accuracy (tested on UCI Heart Disease dataset)

2.4 Fully responsive design for mobile and desktop

2.5 Input validation and secure form handling

2.6 Built using XGBoost, Scikit-learn, and Flask

2.7 Easily customizable for other medical ML projects

2.8 Deployed publicly on Render

---

# 3. Table of Contents

3.1 Getting Started

3.2 Project Structure

3.3 Machine Learning Model

3.4 Frontend Details

3.5 How to Use

3.6 Deployment

3.7 Live Demo of Website

3.8 License

---

# 4. Getting Started

4.1 Follow these steps to set up and run the project locally.

## 4.1.1 Prerequisites

* Python 3.9+ installed on your system
* The required Python libraries listed in `requirements.txt`

---

## 4.1.2 Installation & Setup

### 4.1.2.1 Clone the repository

```bash
git clone <your-repo-url>
cd Heart\ Data
```

### 4.1.2.2 Create and activate a virtual environment (recommended)

```bash
python -m venv venv

# Activate the virtual environment
source venv/bin/activate      # For Linux/macOS
.\venv\Scripts\activate       # For Windows
```

### 4.1.2.3 Install dependencies

```bash
pip install -r requirements.txt
```

### 4.1.2.4 Run the Flask application

```bash
python app.py
```

The app will start on `http://127.0.0.1:5000/` — open this in your browser.

---

# 5. Project Structure

| File/Directory                  | Description                                                   |
| :------------------------------ | :------------------------------------------------------------ |
| `app.py`                        | Main Flask application — handles routes and predictions       |
| `Heart Disease Detection.ipynb` | Jupyter Notebook — data analysis, model training & evaluation |
| `heart_disease.pickle.dat`      | Saved machine learning model used for inference               |
| `heartnew.csv`                  | Dataset used for model training and testing                   |
| `dataset info.docx`             | Documentation explaining dataset features                     |
| `static/`                       | Contains CSS, JS, images, and other frontend assets           |
| `templates/`                    | Contains HTML templates (Flask views)                         |
| `requirements.txt`              | Python dependencies required to run the project               |

---

# 6. Machine Learning Model

6.1 The predictive engine behind this app is a supervised learning model trained on the UCI Heart Disease dataset.

6.2 Model development, training, and evaluation are performed in the Jupyter notebook:

* Training Notebook: `Heart Disease Detection.ipynb`
* Model File: `heart_disease.pickle.dat`

## 6.2.1 Model Highlights

* Algorithms: XGBoost, Scikit-learn
* Accuracy: 99%+ (tested on validation data)
* Serialization: Done using pickle for integration with Flask

---

# 7. Frontend Details

7.1 The frontend is built using HTML, CSS, and JavaScript, ensuring a simple yet responsive user experience.

## 7.1.1 Frontend Components

* Templates: Flask-rendered HTML pages (`/templates/`)
* Styles: Bootstrap + custom styles (`/static/css/`)
* Scripts: Client-side JS (`/static/js/`)
* Images: Stored in `/static/images/` (e.g., `happy.jpg`, `sad.png`, etc.)

---

# 8. How to Use

8.1 Open the web app in your browser (`http://127.0.0.1:5000/`).

8.2 Enter the required clinical parameters (age, cholesterol, blood pressure, etc.).

8.3 Click Predict.

8.4 The model will instantly display whether the person is at risk of heart disease.

---

# 9. Deployment

9.1 This project can be deployed easily using Render, Heroku, or Railway.

## 9.1.1 Example (Render Deployment Steps)

### 9.1.1.1 Push your code to GitHub.

### 9.1.1.2 Connect your GitHub repository to Render.

### 9.1.1.3 Set the start command as:

```bash
gunicorn app:app
```

### 9.1.1.4 Render will automatically build and host your Flask app.

---

# 10. Live Demo of Website

10.1 [https://heart-disease-prediction-4go2.onrender.com/](https://heart-disease-prediction-4go2.onrender.com/)

10.2 This is the live demo link of the website.

10.3 Note: As this is deployed on the free tier of Render, it can take about 2–3 minutes to open.

---

# 11. License

11.1 This project is licensed under the MIT License.

11.2 See the `LICENSE` file for more information.

---

<div align="center">
  <sub>Made with Python, Flask, and XGBoost</sub>
</div>

---
