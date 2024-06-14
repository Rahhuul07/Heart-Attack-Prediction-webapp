import streamlit as st
import pickle
import numpy as np


def load_model():
    with open('saved_steps.pkl', 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

model_loaded = data["model"]
age = data["age"]
gender= data['gender']
impluse = data["impluse"]
pressurehight = data["pressurehight"]
pressurelow = data["pressurelow"]
glucose = data["glucose"]
kcm = data["kcm"]
troponin = data['troponin']

def show_predict_page():
    st.title("Heart Attack Risk Prediction")

    st.write("""### We need some information to predict.""")

    gender = (
        "Male",
        "Female",
        )

    age = st.number_input("Enter your age.",0)

    sex = st.selectbox("Select your gender.",gender)
    sex1=0
    if sex=="Male":
        sex1 = 1
    else:
        sex1 = 0

    imp = st.number_input("Enter your heart rate.", 0,key="pres_input1")

    preh = st.number_input("Enter your systolic BP.", 0,key="pres_input2")

    prel = st.number_input("Enter your diastolic BP.", 0,key="pres_input3")

    glu = st.number_input("Enter your blood sugar levels.", 0.00,key="pres_input4")

    kc = st.number_input("Enter your CK-MB levels.", 0.00,key="pres_input5")

    troponin = st.number_input("Enter your Test-Troponin levels.", 0.000,key="pres_input6")



    ok = st.button("Predict")

    if ok:
        X_res = np.array([[age,sex1,imp,preh,prel,glu,kc,troponin]])

        pred = model_loaded.predict(X_res)

        if pred[0] == 'positive':
            st.subheader("Prediction is positive. Consult heart specialist.")
        else:
            st.subheader("Prediction is negative. Hurahh!! your heart is healthy.")

        #st.write("Prediction is ",pred[0])

