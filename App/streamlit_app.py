import streamlit as st
import pandas as pd
import joblib
import numpy as np 

st.title("💼 Data Science Salary Predictor")

# 1) Load your trained model AND the list of feature columns
model = joblib.load('Model/model.pkl')
feature_columns = joblib.load('model/feature_columns.pkl')

# 2) Get user inputs
work_year = st.selectbox("Work Year", [2020, 2021, 2022, 2023])
experience = st.selectbox("Experience Level", ["EN", "MI", "SE", "EX"])
employment_type = st.selectbox("Employment Type", ["FT", "PT", "CT", "FL"])
company_size = st.selectbox("Company Size", ["S", "M", "L"])
remote_ratio = st.slider("Remote Ratio (%)", 0, 100, 100)
job_title = st.text_input("Job Title", "Data Scientist")
company_location = st.text_input("Company Location (ISO Code)", "US")
employee_residence = st.text_input("Employee Residence (ISO Code)", "US")

if st.button("Predict Salary"):
    # 3) Build a one-row DataFrame exactly as you did during training
    df = pd.DataFrame([{
        'work_year': work_year,
        'experience_level': experience,
        'employment_type': employment_type,
        'company_size': company_size,
        'remote_ratio': remote_ratio,
        'job_title': job_title,
        'company_location': company_location,
        'employee_residence': employee_residence
    }])
    
    # 4) Apply the same label encoding + one-hot encoding
    # (for brevity, using pandas.get_dummies to replicate training)
    df = pd.get_dummies(df,
        columns=['job_title','company_location','employee_residence'],
        drop_first=False
    )
    
    # 5) Align to the training columns, filling missing dummies with 0
    df = df.reindex(columns=feature_columns, fill_value=0)
    
    # 6) Map your small categorical columns if you used LabelEncoder
    experience_map = {'EN':0,'MI':1,'SE':2,'EX':3}
    employment_map = {'PT':0,'FT':1,'CT':2,'FL':3}
    size_map = {'S':0,'M':1,'L':2}
    
    # 6) Map your small categorical columns
    df['experience_level'] = df['experience_level'].map(experience_map)
    df['employment_type']  = df['employment_type'].map(employment_map)
    df['company_size']     = df['company_size'].map(size_map)
    
    # 7) Predict
    pred = model.predict(df)
    
    # 8) Squeeze out a Python scalar from the returned array
    salary = float(np.array(pred).flatten()[0])
    
    # 9) Display
    st.subheader(f"💰 Predicted Salary: ${salary:,.0f} USD")
