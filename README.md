🎓 Admission Predictor

This project is a machine learning application that predicts a student's chance of admission to a graduate program based on various academic and profile features.

📁 Project Files

- `Project.ipynb` – Jupyter Notebook with data exploration, visualization, and model training.
- `Admission_Predict.csv` – Dataset used to train the model.
- `admission_model1.pkl` – Trained ML model saved using Pickle.
- `app.py` – Python script (can be a Flask app) for deploying the model.
- `templates/` – Folder for HTML templates if a web interface is used.

📊 Dataset Features

The dataset includes the following features:

- GRE Score
- TOEFL Score
- University Rating
- SOP (Statement of Purpose Strength)
- LOR (Letter of Recommendation Strength)
- CGPA (Undergraduate GPA)
- Research (0 or 1)
- Chance of Admit (target variable)

🧠 Model Overview

A regression model was trained using scikit-learn to predict the `Chance of Admit` based on the input features. The final model is serialized and saved as `admission_model1.pkl`.
