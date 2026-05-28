https://ai-grievance-flask.onrender.com

# AI Grievance Routing System

An AI-powered web application that automatically classifies user complaints into the appropriate department using Machine Learning and Natural Language Processing (NLP).

---

## Features

- Complaint classification using NLP
- Automatic department prediction
- Flask-based web application
- Machine Learning model deployment
- Clean and responsive frontend
- Real-time predictions

---

## Departments Supported

- Electricity Department
- Water Department
- Road Maintenance
- Internet Services
- Banking Support
- College Administration

---

## Tech Stack

| Technology | Usage |
|---|---|
| Python | Backend Programming |
| Flask | Web Framework |
| Pandas | Data Handling |
| Scikit-learn | Machine Learning |
| CountVectorizer | Text Vectorization |
| Logistic Regression | Classification Model |
| HTML/CSS | Frontend |
| Gunicorn | Deployment Server |

---

## Project Structure

```text
AI-Grievance-System/
│
├── templates/
│   └── index.html
│
├── static/
│
├── app.py
├── grievance_model.pkl
├── vectorizer.pkl
├── label_encoder.pkl
├── grievance_dataset.csv
├── requirements.txt
├── Procfile
└── README.md
```

---

## How It Works

```text
User Complaint
      ↓
CountVectorizer
      ↓
Machine Learning Model
      ↓
Department Prediction
```

---

## Machine Learning Workflow

1. Load dataset using Pandas
2. Preprocess complaint text
3. Convert text into numerical vectors using CountVectorizer
4. Train Logistic Regression model
5. Save trained model using Pickle
6. Deploy model with Flask


## Deployment

Deployed using Render

---

## Example Complaints

| Complaint | Predicted Department |
|---|---|
| No electricity in my locality | Electricity |
| Water leakage near road | Water |
| Road damaged due to rain | Road |
| Internet disconnects frequently | Internet |
| Money deducted but payment failed | Banking |
| Attendance portal not working | College |

