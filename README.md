

# ❤️ Heart Disease Prediction Web Application

A beginner-friendly **Flask-based web application** that predicts the risk of heart disease using **machine learning models (XGBoost, Scikit-learn)**.  
The app is built with **Python**, designed for simplicity and accuracy, and **deployed on Render** for public access.

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-green?logo=flask)
![Machine Learning](https://img.shields.io/badge/ML-XGBoost%2C%20Scikit--learn-orange)
![Status](https://img.shields.io/badge/Status-Live-success)
![License](https://img.shields.io/badge/License-MIT-yellow)



---

## 🧠 Overview

This project uses a **pre-trained machine learning model** to predict whether a person is at risk of heart disease based on input parameters such as age, blood pressure, cholesterol levels, and more.  
It provides a **clean, responsive, and easy-to-use web interface** powered by **Flask** and a **trained ML model** built using **XGBoost** and **Scikit-learn**.

You can test the app live on **Render** (if deployed).

---

## 🌟 Features

✅ User-friendly web interface  
✅ Real-time heart disease risk prediction  
✅ 99%+ model accuracy (tested on UCI Heart Disease dataset)  
✅ Fully responsive design for mobile and desktop  
✅ Input validation and secure form handling  
✅ Built using **XGBoost**, **Scikit-learn**, and **Flask**  
✅ Easily customizable for other medical ML projects  
✅ Deployed publicly on **Render**

---

## 📑 Table of Contents

- [🚀 Getting Started](#-getting-started)
- [📂 Project Structure](#-project-structure)
- [💻 Machine Learning Model](#-machine-learning-model)
- [🎨 Frontend Details](#-frontend-details)
- [🧪 How to Use](#-how-to-use)
- [🚀 Deployment](#-deployment)
- [📝 License](#-license)

---

## 🚀 Getting Started

Follow these steps to set up and run the project locally.

### ✅ Prerequisites

- **Python 3.9+** installed on your system  
- The required Python libraries listed in `requirements.txt`

---

### ⚙️ Installation & Setup

1. **Clone the repository**

   ```bash
   git clone <your-repo-url>
   cd Heart\ Data
````

2. **Create and activate a virtual environment** (recommended)

   ```bash
   python -m venv venv
   # Activate the virtual environment
   source venv/bin/activate      # For Linux/macOS
   .\venv\Scripts\activate       # For Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask application**

   ```bash
   python app.py
   ```

   The app will start on **[http://127.0.0.1:5000/](http://127.0.0.1:5000/)** — open this in your browser.

---

## 📂 Project Structure

| File/Directory                  | Description                                                       |
| :------------------------------ | :---------------------------------------------------------------- |
| `app.py`                        | Main **Flask application** — handles routes and predictions       |
| `Heart Disease Detection.ipynb` | **Jupyter Notebook** — data analysis, model training & evaluation |
| `heart_disease.pickle.dat`      | Saved **machine learning model** used for inference               |
| `heartnew.csv`                  | **Dataset** used for model training and testing                   |
| `dataset info.docx`             | Documentation explaining dataset features                         |
| `static/`                       | Contains **CSS**, **JS**, **images**, and other frontend assets   |
| `templates/`                    | Contains **HTML templates** (Flask views)                         |
| `requirements.txt`              | Python dependencies required to run the project                   |

---

## 💻 Machine Learning Model

The predictive engine behind this app is a **supervised learning model** trained on the **UCI Heart Disease dataset**.
Model development, training, and evaluation are performed in the Jupyter notebook:

* **Training Notebook:** `Heart Disease Detection.ipynb`
* **Model File:** `heart_disease.pickle.dat`

### ⚙️ Model Highlights

* Algorithms: **XGBoost**, **Scikit-learn**
* Accuracy: **99%+ (tested on validation data)**
* Serialization: Done using **pickle** for integration with Flask

---

## 🎨 Frontend Details

The frontend is built using **HTML**, **CSS**, and **JavaScript**, ensuring a simple yet responsive user experience.

* **Templates:** Flask-rendered HTML pages (`/templates/`)
* **Styles:** Bootstrap + custom styles (`/static/css/`)
* **Scripts:** Client-side JS (`/static/js/`)
* **Images:** Stored in `/static/images/` (e.g., `happy.jpg`, `sad.png`, etc.)

---

## 🧪 How to Use

1. Open the web app in your browser (`http://127.0.0.1:5000/`).
2. Enter the required clinical parameters (age, cholesterol, blood pressure, etc.).
3. Click **Predict**.
4. The model will instantly display whether the person is at risk of heart disease.

---

## 🚀 Deployment

This project can be deployed easily using **Render**, **Heroku**, or **Railway**.

### Example (Render Deployment Steps):

1. Push your code to GitHub.
2. Connect your GitHub repo to **Render**.
3. Set the **start command** as:

   ```bash
   gunicorn app:app
   ```
4. Render will automatically build and host your Flask app.

---

## 📝 License

This project is licensed under the **MIT License**.
See the [LICENSE](./LICENSE) file for more information.

---

<div align="center">
  <sub>Made with ❤️ using Python, Flask, and XGBoost</sub>
</div>
```

---
