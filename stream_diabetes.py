import pickle
import streamlit as st

#membaca model

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#judul web
st.title('Data Mining Prediksi Diabetes')

Pregnancies = st.text_input('Input nilai kehamilan')

Glucose = st.text_input('Input nilai Glukosa')

BloodPressure = st.text_input('Input nilai Tekanan Darah')

SkinThickness = st.text_input('Input nilai Ketebalan Kulit')

Insulin = st.text_input('Input nilai Insulin')

BMI = st.text_input('Input nilai BMI')

DiabetesPedigreeFunction = st.text_input('Input nilai Fungsi silsilah diabtes')

Age = st.text_input('Input nilai Usia')


#code untuk prediksi

diab_diagnosis = ''

#membuat tombol untuk prediksi

if st.button('Test prediksi diabetes'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

    if(diab_prediction[0]==1):
        diab_diagnosis = 'pasien terkena diabetes'
    else:
        diab_diagnosis = 'pasien tidak terkena diabetes'
        
    st.success(diab_diagnosis)