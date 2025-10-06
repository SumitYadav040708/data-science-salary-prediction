# 💼 Data Science Salary Predictor

An end-to-end machine learning application that predicts data science salaries based on various factors like experience level, company size, location, and more. The application is built using Python and deployed with Streamlit.

## 📊 Project Overview

This project aims to help data professionals estimate their market value by predicting salaries based on key factors that influence compensation in the data science field. The model is trained on real-world salary data and provides predictions in USD.

## 🔧 Features

- Predict salaries for various data science roles
- Consider multiple factors:
  - Work year (2020-2023)
  - Experience level (Entry, Mid, Senior, Executive)
  - Employment type (Full-time, Part-time, Contract, Freelance)
  - Company size (Small, Medium, Large)
  - Remote work ratio
  - Job title
  - Company location
  - Employee residence

## 🗂️ Project Structure

```
├── App/
│   ├── requirements.txt      # Python dependencies
│   └── streamlit_app.py     # Streamlit web application
├── Data/
│   └── ds_salaries.csv      # Dataset used for training
├── Model/
│   ├── feature_columns.pkl  # Saved feature columns for prediction
│   └── model.pkl           # Trained machine learning model
└── Notebooks/
    ├── EDA.ipynb           # Exploratory Data Analysis
    └── Modelling.ipynb     # Model development and training
```

## 🚀 Getting Started

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SumitYadav040708/data-science-salary-prediction.git
   cd data-science-salary-prediction
   ```

2. Install required packages:
   ```bash
   pip install -r App/requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   cd App
   streamlit run streamlit_app.py
   ```

## 📝 How to Use

1. Select or enter the following information:
   - Work year
   - Experience level
   - Employment type
   - Company size
   - Remote work ratio (%)
   - Job title
   - Company location (country code)
   - Employee residence (country code)

2. Click the "Predict Salary" button to get the estimated salary in USD.

## 🛠️ Technical Details

- **Framework**: Streamlit
- **Machine Learning**: scikit-learn
- **Data Processing**: pandas, numpy
- **Model Serialization**: joblib

## 📈 Model Information

- The model is trained on real-world data science salary data
- Features are processed using label encoding and one-hot encoding
- Salary predictions are provided in USD

## 📚 Dataset

The dataset (`ds_salaries.csv`) contains information about data science salaries including:
- Work year
- Experience level
- Employment type
- Job title
- Salary in USD
- Company location
- Company size
- Remote work ratio

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/SumitYadav040708/data-science-salary-prediction/issues).

## 📜 License

This project is open source and available under the [MIT License](LICENSE).

## ✨ Acknowledgments

- Dataset source: [Insert dataset source if available]
- Contributors and maintainers
- Open source community

## 📧 Contact

Sumit Yadav - [@GitHub](https://github.com/SumitYadav040708)

Project Link: [https://github.com/SumitYadav040708/data-science-salary-prediction](https://github.com/SumitYadav040708/data-science-salary-prediction)
