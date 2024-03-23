# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 20:23:38 2024

@author: lucky
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

diabetes_model=pickle.load(open("C:/Users/lucky/OneDrive/Desktop/Jupyter/disease prediction system web app/saved models/diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open("C:/Users/lucky/OneDrive/Desktop/Jupyter/disease prediction system web app/saved models/heart_model.sav",'rb'))
parkinson_disease_model=pickle.load(open("C:/Users/lucky/OneDrive/Desktop/Jupyter/disease prediction system web app/saved models/parkinson_model.sav",'rb'))
#sidebar 

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System',
                         ['Diabetes Prediction',
                          'Heart disease prediction',
                          "Parkinson's disease prediction"]
                         ,icons=['activity','heart','person']
                         ,default_index=0)
    
#Diabetes prediction page

if(selected=='Diabetes Prediction'):
    st.title('Diabetes Prediction using ML')
    
    #getting input data
    
    col1,col2,col3=st.columns(3)
    with col1:
        Pregnancies=st.text_input("Number of pregnancies")
    with col2:
        Glucose=st.text_input("Glucose level")
    with col3:
        BloodPressure=st.text_input("Blood Pressure value")
    with col1:
        SkinThickness=st.text_input("SkinThickness value")
    with col2:
        Insulin=st.text_input("Insulin value")
    with col3:
        BMI=st.text_input("BMI value")
    with col1:
        DiabetesPedegreeFunction=st.text_input("DiabetesPedegreeFunction value")
    with col2:
        Age=st.text_input("Age")
    
    
    
    diab_diagnosis=''
    
    if st.button('Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedegreeFunction,Age]])
        if (diab_prediction[0]==1):
            diab_diagnosis='The person is diabetic'
        else:
            diab_diagnosis="The person is not diabetic"
    st.success(diab_diagnosis)
    
    
# Heart disease prediction page

if(selected=='Heart disease prediction'):
    st.title('Heart disease prediction using ML')
    
    col1,col2,col3=st.columns(3)
    with col1:
        Age=st.text_input("Age")
    with col2:
        Sex=st.text_input("Sex")
    with col3:
        CP=st.text_input("Chest Pain type value")
    with col1:
        trestbps=st.text_input("Resting blood pressure value")
    with col2:
        chol=st.text_input("cholestrol value")
    with col3:
        fbs=st.text_input("fasting bolld sugar>120 mg/dL")
    with col1:
        restecg=st.text_input("resting electrocardiographic result")
    with col2:
        thalach=st.text_input("Maximum heart rate value")
    with col3:
        exang=st.text_input("Exercise Induced Angina")
    with col1:
        oldpeak=st.text_input("ST deperession induced by exercise")
    with col2:
        slope=st.text_input("slope of the peak exercise ST segment")
    with col3:
        ca=st.text_input("Major vessels colored by flourosopy")
    with col1:
        thal=st.text_input("thal: 0=normal; 1=fixed defect; 2=reversable defect")
        
    diab_diagnosis=''
    
    if st.button('Test Result'):
        diab_prediction=heart_disease_model.predict([[float(Age),float(Sex),float(CP),float(trestbps),float(chol),float(fbs),float(restecg),float(thalach),float(exang),float(oldpeak),float(slope),float(ca),float(thal)]])
        if (diab_prediction[0]==1):
            diab_diagnosis='The person have heart disease'
        else:
            diab_diagnosis="The person do not have heart disease"
    st.success(diab_diagnosis)
    
# Parkinson disease prediction page

if(selected=="Parkinson's disease prediction"):
    st.title("Parkinson's disease prediction using ML")
    
    col1,col2,col3=st.columns(3)
    with col1:
        fo=st.text_input("MDVP:Fo(Hz)")
    with col2:
        fhi=st.text_input("MDVP:Fhi(Hz)")
    with col3:
        flo=st.text_input("MDVP:Flo(Hz)")
    with col1:
        jitter_percent=st.text_input("MDVP:Jitter(%)")
    with col2:
        jitter_abs=st.text_input("MDVP:Jitter(Abs)")
    with col3:
        rap=st.text_input("MDVP:RAP")
    with col1:
        ppq=st.text_input("MDVP:PPQ")
    with col2:
        ddp=st.text_input("Jitter:DDP")
    with col3:
        shimmer=st.text_input("MDVP:Shimmer")
    with col1:
        shimmer_db=st.text_input("MDVP:Shimmer(dB)")
    with col2:
        shimmer_apq3=st.text_input("Shimmer:APQ3")
    with col3:
        shimmer_apq5=st.text_input("Shimmer:APQ5")
    with col1:
        apq=st.text_input("MDVP:APQ")
    with col2:
        dda=st.text_input("Shimmer:DDA")
    with col3:
        nhr=st.text_input("NHR")
    with col1:
        hnr=st.text_input("HNR")
    with col2:
        rpde=st.text_input("RPDE")
    with col3:
        dfa=st.text_input("DFA")
    with col1:
        spread1=st.text_input("spread1")
    with col2:
        spread2=st.text_input("spread2")
    with col3:
        d2=st.text_input("D2")
    with col1:
        ppe=st.text_input("PPE")
        
    diab_diagnosis=''
    
    if st.button('Test Result'):
        diab_prediction=parkinson_disease_model.predict([[fo,fhi,flo,jitter_percent,jitter_abs,rap,ppq,ddp,shimmer,shimmer_db,shimmer_apq3,shimmer_apq5,apq,dda,nhr,hnr,rpde,dfa,spread1,spread2,d2,ppe]])
        if (diab_prediction[0]==1):
            diab_diagnosis='The person have parkinson disease'
        else:
            diab_diagnosis="The person do not have parkinson disease"
    st.success(diab_diagnosis)