# 🚀 Medipolicy_Predict

## 📌 Overview

Medipolicy_Predict is a machine learning project aimed at predicting medical policies using Random Forest. The project follows a structured approach, including data preprocessing, exploratory data analysis (EDA), model building, and deployment via Streamlit. It also incorporates a CI/CD pipeline for automatic updates.

## 📂 Project Structure

```bash
Medipolicy_Predict/
├── .github/                # 🚀 CI/CD pipeline for Streamlit Cloud model updates
├── Data/                   # 📊 Contains datasets for the project
├── EDA/                    # 🔍 Code for exploratory data analysis and report (PDF)
├── RandomForest/           # 🤖 Model building code and accuracy report (PDF)
├── streamlit_app/          # 🌐 Streamlit UI app and tests for CI/CD
│   ├── app.py              # 🎨 Main UI file for Streamlit
│   ├── tests/              # ✅ Test cases for CI/CD pipeline
```

## ✨ Features

- 📌 Data Preprocessing: Cleaning and transforming the dataset.

- 🔍 Exploratory Data Analysis (EDA): Understanding data patterns and trends.

- 🤖 Model Building: Uses Random Forest for predictions.

- 📊 Model Evaluation: Performance metrics and accuracy reports.

- 🌐 Streamlit UI: Interactive web app for predictions.

- 🚀 CI/CD Integration: Automates model deployment using GitHub Actions.

## ⚙️ Installation

* Clone the repository:
```bash
git clone https://github.com/Josephvarghes/Medipolicy_Predict
cd Medipolicy_Predict
```
* Install dependencies:
```bash
pip install -r requirements.txt
```
* Run the Streamlit app:
```bash
streamlit run streamlit_app/app.py
```
## 🎯 Usage

- 📈 Perform EDA to analyze trends.

- 🤖 Train the model using the Random Forest algorithm.

- 📊 View predictions and accuracy reports.

- 🚀 Deploy updates automatically using the CI/CD pipeline.