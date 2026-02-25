
# 💻 Laptop Price Predictor

A Machine Learning web application built using **Streamlit** that predicts laptop prices based on user-selected configurations.

---

## 🚀 Live Demo
(Deploy on Streamlit Cloud and paste link here)

---

## 📌 Project Overview

This project is an end-to-end Machine Learning solution that predicts laptop prices based on hardware specifications.

The system includes:
- Data Cleaning & Feature Engineering
- Model Training using Scikit-learn Pipeline
- Log Transformation of Target Variable
- Streamlit Web App Deployment

---

## 🧠 Features Used for Prediction

- Brand (Company)
- Type of Laptop
- RAM (GB)
- Weight (kg)
- Touchscreen (Yes/No)
- IPS Display (Yes/No)
- Screen Size (inches)
- Screen Resolution (used to calculate PPI)
- CPU Brand
- HDD Storage
- SSD Storage
- GPU Brand
- Operating System

---

## 📊 Machine Learning Details

- Model Type: Regression Model
- Pipeline: Scikit-learn Pipeline
- Feature Engineering:
  - PPI calculation from screen resolution
  - Categorical encoding
  - Log transformation of price
- Libraries Used:
  - Pandas
  - NumPy
  - Scikit-learn
  - Streamlit

---

## 🗂 Project Structure

Laptop-Price-Predictor/
│
├── app/
│   ├── app.py
│   ├── pipe.pkl
│   └── df.pkl
│
├── data/
│   └── laptop_data.csv
│
├── notebooks/
│   └── laptop_predictor.ipynb
│
├── requirements.txt
└── README.md

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository

git clone https://github.com/your-username/Laptop-Price-Predictor.git  
cd Laptop-Price-Predictor

### 2️⃣ Install Dependencies

pip install -r requirements.txt

### 3️⃣ Run Streamlit App

cd app  
streamlit run app.py

---

## 🌐 Deployment Options

This application can be deployed using:

- Streamlit Cloud
- Render
- Railway

---

## 🎯 Why This Project?

This project demonstrates:

✔ End-to-end ML workflow  
✔ Feature Engineering  
✔ Model Deployment  
✔ Real-world UI integration  
✔ Production-ready folder structure  

It is portfolio-ready and suitable for showcasing ML deployment skills.

---

## 👨‍💻 Author

SYED TAIYABULLAH  
Aspiring Data Scientist | Machine Learning Enthusiast 🚀  

---

## ⭐ If You Like This Project

Give it a star on GitHub and feel free to fork it!
