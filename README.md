# 📊 Poll Results Visualizer

An interactive data analytics dashboard built using **Python and Streamlit** to analyze and visualize survey/poll data in a meaningful and user-friendly way.

---

## 🚀 Project Overview

The **Poll Results Visualizer** helps transform raw survey data into clear insights using visualizations and dashboards.

This project uses the **Stack Overflow Developer Survey dataset** to analyze developer trends such as:

* Most popular programming languages
* Country-wise participation
* Distribution of responses

---

## 🎯 Problem Statement

Raw survey data is difficult to interpret.
Organizations need tools to:

* Understand user preferences
* Identify trends
* Make data-driven decisions

---

## 💡 Solution

This project:

* Cleans and processes raw survey data
* Converts multi-select responses into structured format
* Generates visual insights using charts
* Displays everything in an interactive dashboard

---

## 🛠️ Tech Stack

* **Python**
* **Pandas & NumPy** → Data processing
* **Matplotlib & Seaborn** → Visualization
* **Streamlit** → Dashboard

---

## 📁 Project Structure

```
Poll-Results-Visualizer/
│
├── data/
│   └── survey_results_public.csv
│
├── src/
│   └── data_processing.py
│
├── app.py
├── requirements.txt
└── README.md
```
## Dataset

The dataset used in this project is the Stack Overflow Developer Survey.

Due to GitHub file size limits, the dataset is not included in this repository.

You can download it from:
https://www.kaggle.com/datasets/stackoverflow/stack-overflow-developer-survey

After downloading, place the file inside the `data/` folder:
---

## ⚙️ Installation & Setup

### 1. Clone Repository

```bash
git clone 
cd poll-results-visualizer
```

### 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
streamlit run app.py
```

👉 The dashboard will open in your browser.

---

## 📊 Features

* 📌 Clean and structured survey data
* 📌 Multi-select data handling (important real-world skill)
* 📌 Interactive dashboard
* 📌 Country-based filtering
* 📌 KPI metrics (Top Language, Total Responses, Countries)
* 📌 Bar charts and Pie charts
* 📌 Insight generation

---

## 📈 Key Insights Generated

* Most popular programming language
* Total survey responses analyzed
* Country with highest participation
* Distribution of technology usage

---


## 🧠 What I Learned

* Data cleaning and preprocessing
* Handling multi-value columns
* Data visualization best practices
* Building interactive dashboards
* Real-world dataset handling


---

## 💼 Use Cases

* Survey Analysis
* Customer Feedback Insights
* Market Research
* Employee Satisfaction Studies
* Product Preference Analysis


---


## ⭐ If you like this project

Give it a ⭐ on GitHub and share it!

---
