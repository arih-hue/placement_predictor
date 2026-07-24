# 🎓 Student Placement & Salary Prediction

An end-to-end Machine Learning project that predicts:

- 🎯 Whether a student will be placed
- 💰 Expected salary package (LPA)

The project uses **XGBoost Classifier** for placement prediction and **XGBoost Regressor** for salary prediction. It also includes an interactive **Streamlit dashboard** for data exploration and prediction.

---

## 📸 Application Preview

> Add screenshots after completing the dashboard.

### Home Page

![Home](../assets/Home.png)

### Dashboard

![Dashboard](../assets/Dashboard.png)

### Prediction

![Prediction](../assets/Prediction.png)

---

# 🚀 Features

- End-to-End Machine Learning Pipeline
- Interactive Streamlit Dashboard
- Placement Prediction
- Salary Prediction
- Feature Engineering
- Exploratory Data Analysis
- Model Performance Visualization
- Feature Importance Analysis

---

# 📂 Project Structure

```
Student-Placement-Predictor/

│── app.py

│── pages/
│     ├── Dashboard.py
│     ├── EDA.py
│     ├── Model Performance.py
│     └── Prediction.py

│── assets/

│── data/
│     └── student_placement.csv

│── models/
│     ├── placement_model.pkl
│     ├── salary_model.pkl
│     ├── branch_encoder.pkl
│     └── tier_encoder.pkl

│── notebooks/
│     └── EDA.ipynb

│── src/
│     ├── config.py
│     ├── feature_engineering.py
│     ├── predict.py
│     ├── preprocessing.py
│     ├── train_classifier.py
│     ├── train_regressor.py
│     └── utils.py

│── requirements.txt

└── README.md
```

---

# 📊 Dataset

The dataset contains academic, technical, and extracurricular information of students.

### Features

- CGPA
- Backlogs
- Coding Skills
- DSA Score
- Aptitude Score
- Communication Skills
- ML Knowledge
- System Design
- Internships
- Projects Count
- Hackathons
- Open Source Contributions
- Branch
- College Tier

### Target Variables

Classification

- Placement Status

Regression

- Salary Package (LPA)

---

# ⚙️ Feature Engineering

Additional features were created to improve model performance.

- Technical Score
- Experience Score
- Academic Score
- DSA × Coding Score
- Resume Strength

---

# 🤖 Machine Learning Models

## Placement Prediction

Model:

- XGBoost Classifier

Predicts whether a student is likely to be placed.

---

## Salary Prediction

Model:

- XGBoost Regressor

Predicts the expected salary package of placed students.

---

# 📈 Exploratory Data Analysis

The project includes analysis such as:

- Placement Distribution
- CGPA Distribution
- Placement Rate by Branch
- Placement Rate by College Tier
- Average Salary by Branch
- Average Salary by College Tier
- Placement Rate vs CGPA
- Coding Skills vs Salary
- DSA Score vs Salary
- Communication Skills vs Salary
- Correlation Heatmap

---

# 📊 Streamlit Dashboard

The application consists of four sections.

### 🏠 Home

Project Overview

---

### 📊 Dashboard

- Dataset Statistics
- Placement Overview
- Salary Overview

---

### 📈 Exploratory Data Analysis

Interactive visualization of the dataset.

---

### 🤖 Model Performance

- Classification Accuracy
- Regression Metrics
- Feature Importance
- Confusion Matrix

---

### 🎯 Prediction

Enter student information and predict

- Placement Status
- Placement Probability
- Expected Salary Package

---

# 📦 Installation

Clone the repository

```bash
git clone https://github.com/your-username/student-placement-predictor.git
```

Move into the project directory

```bash
cd student-placement-predictor
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run Home.py
```

---

# 🛠️ Technologies Used

### Programming Language

- Python

### Machine Learning

- Scikit-learn
- XGBoost

### Data Analysis

- Pandas
- NumPy

### Visualization

- Matplotlib
- Seaborn

### Deployment

- Streamlit

---

# 📈 Results

### Classification

- XGBoost Classifier

Accuracy: **(Add your final accuracy here)**

---

### Regression

- XGBoost Regressor

R² Score: **(Add your final R² here)**

MAE: **(Add your MAE here)**

RMSE: **(Add your RMSE here)**

---

# 🔮 Future Improvements

- SHAP Explainability
- Hyperparameter Optimization
- Docker Support
- FastAPI Deployment
- Cloud Deployment
- CI/CD Pipeline

---

# 👨‍💻 Author

**Arihant Yadav**

GitHub: https://github.com/your-github

LinkedIn: https://linkedin.com/in/your-linkedin

---

⭐ If you found this project useful, consider giving it a star.
