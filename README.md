# 🎓 Student Dropout Risk Prediction using Multimodal Machine Learning

## 1. Project Overview

**Project Name:** Student Dropout Risk Prediction System

**One-Liner:** AI-powered multimodal system that predicts student dropout risk using academics, attendance trends, and counsellor insights.

### Problem Statement

Educational institutions often struggle to identify students who may be at risk of dropping out before it becomes too late. Academic decline, irregular attendance, and behavioural indicators are often scattered across different systems, making early intervention difficult.

Our solution combines academic records, attendance history, and counsellor notes into a single AI-powered prediction system that classifies students into:

* Low Risk (0)
* Medium Risk (1)
* High Risk (2)

This allows faculty members and counsellors to take proactive action and provide timely support.

---

## 2. Technical Architecture

### Cloud Provider

Kaggle Notebooks (Model Development & Training)

### Frontend

Not Applicable (Model Development Project)

### Backend

Python

### Machine Learning Stack

* CatBoost
* LightGBM
* XGBoost
* Scikit-Learn
* Pandas
* NumPy

### NLP Stack

* TF-IDF Vectorization
* Truncated SVD

### Database

Competition Dataset Provided by Organizers

---

## 3. Project Pipeline

### Step 1: Data Sources

We combined three modalities:

#### Tabular Data

* Branch
* Gender
* Family Income
* Parent Education
* Scholarship Status
* Part-time Job Status
* Screen Time
* Commute Time

#### Attendance Time-Series

* Semester-wise attendance
* Attendance trend
* Attendance consistency
* Attendance slope

#### Counsellor Notes (Text)

Unstructured counselling observations and student feedback.

---

### Step 2: Feature Engineering

#### Academic Features

* CGPA Mean
* CGPA Standard Deviation
* CGPA Trend

#### Backlog Features

* Total Backlogs
* Average Backlogs
* Backlog Trend

#### Attendance Features

* Attendance Mean
* Attendance Standard Deviation
* Attendance Range
* Attendance Trend
* Attendance Slope
* Semester-wise Attendance Metrics

---

### Step 3: NLP Processing

Counsellor notes were transformed into numerical features using:

1. TF-IDF Vectorization
2. Truncated SVD

This reduced text dimensionality while preserving meaningful semantic information.

---

### Step 4: Model Training

Three separate models were trained using Stratified 5-Fold Cross Validation:

#### CatBoost

Strong performance on mixed numerical and categorical features.

#### LightGBM

Fast gradient boosting model.

#### XGBoost

Robust tree-based ensemble learner.

---

### Step 5: Ensemble Learning

Probability outputs from all three models were combined using:

Final Ensemble:

* CatBoost: 70%
* LightGBM: 15%
* XGBoost: 15%

---

### Step 6: Threshold Optimization

Class probabilities for minority classes were adjusted to maximize Macro F1 Score.

Optimized Threshold Multipliers:

* Class 1: 1.30
* Class 2: 1.30

---

## 4. Model Performance

### Best Validation Performance

| Model                             | Macro F1   |
| --------------------------------- | ---------- |
| CatBoost                          | 0.6991     |
| LightGBM                          | 0.6887     |
| XGBoost                           | 0.6927     |
| Ensemble                          | 0.7017     |
| Ensemble + Threshold Optimization | **0.7072** |

### Evaluation Metric

Macro F1 Score

This metric was chosen because it equally weights all classes and handles class imbalance effectively.

---

## 5. Key Insights

Feature importance analysis showed that the following factors had the strongest influence on dropout prediction:

* Screen Time
* Family Income
* Attendance Behaviour
* CGPA Consistency
* Academic Trend
* Parent Education
* Counsellor Notes

The NLP features extracted from counsellor notes significantly improved overall performance.

---

## 6. Challenges Faced

* Handling noisy and repetitive counsellor notes.
* Engineering meaningful attendance trend features.
* Preventing train-test feature mismatches.
* Balancing performance across all three dropout categories.
* Optimizing Macro F1 instead of accuracy.

---

## 7. What We Learned

This project helped us gain practical experience in:

* Multimodal Machine Learning
* Feature Engineering
* Natural Language Processing
* Ensemble Learning
* Cross Validation
* Model Evaluation using Macro F1

We learned that high-quality features often contribute more than simply choosing a more complex model.

---

## 8. Future Scope

Potential improvements include:

* Real-time student monitoring dashboards
* Deep-learning text embeddings
* Explainable AI recommendations
* Personalized intervention suggestions
* Integration with Learning Management Systems (LMS)

---

## 9. Proof of Zero-Cost Usage

### Free Resources Used

* Kaggle Notebooks
* Kaggle Dataset Storage
* Open-source ML Libraries
* Scikit-Learn
* CatBoost
* LightGBM
* XGBoost

### Scalability Approach

The solution is model-agnostic and can be deployed as a cloud API where predictions can be generated on-demand for large student populations.

---

## 10. Important Links

### GitHub Repository

(https://github.com/adarsh3908/RetinaAI)

### Competition Submission

submission_v1.csv

---

## Authors

Adarsh Prakash Singh
