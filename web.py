import os
import pickle 
import streamlit as st    
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
diabetes_model_path = os.path.join(BASE_DIR, "models", "diabetes_model.sav")
heart_disease_model_path = os.path.join(BASE_DIR, "models", "heart_model.sav")
parkinsons_model_path = os.path.join(BASE_DIR, "models", "parkinsons_model.sav")

# Load models from these relative paths
diabetes_model = pickle.load(open(diabetes_model_path, 'rb'))
heart_disease_model = pickle.load(open(heart_disease_model_path, 'rb'))
parkinsons_model = pickle.load(open(parkinsons_model_path, 'rb'))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI  value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of the person')

    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
                        BMI, DiabetesPedigreeFunction, Age]
        user_input= [float(x) for x in user_input]
        diab_prediction= diabetes_model.predict([user_input])
        if diab_prediction[0]==1:
            diab_diagnosis= 'The person is diabetic'
        else:
            diab_diagnosis= 'The person is not diabetic'
        st.success(diab_diagnosis)


#heart
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex (0 = Female, 1 = Male)', [0, 1])
    with col3:
        cp = st.text_input('CP-Chest Pain Type (0-3)')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
    with col2:
        chol = st.text_input('Cholesterol Level (mg/dl)')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl (1 = Yes, 0 = No)', [0, 1])
    
    with col1:
        restecg = st.text_input('(Restecg)-Resting Electrocardiographic Results (0-2)')
    with col2:
        thalach = st.text_input('(Thalach)-Maximum Heart Rate Achieved')
    with col3:
        exang = st.selectbox('(Exang)-Exercise Induced Angina (1 = Yes, 0 = No)', [0, 1])
    
    with col1:
        oldpeak = st.text_input('(Oldpeak)-ST Depression Induced by Exercise')
    with col2:
        slope = st.text_input('Slope of Peak Exercise ST Segment (0-2)')
    with col3:
        ca = st.text_input('(Ca)-Number of Major Vessels (0-4)')

    with col1:
        thal = st.text_input('(Thal)-Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)')


    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        
        heart_prediction = heart_disease_model.predict([user_input])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is likely to have heart disease'
        else:
            heart_diagnosis = 'The person is unlikely to have heart disease'

        st.success(heart_diagnosis)

#parkinsons
if selected == 'Parkinsons prediction':
    st.title('Parkinsons Disease Prediction using ML')
    
    
    col1, col2, col3 = st.columns(3)
    
   
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
    
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shim = st.text_input('MDVP:Shimmer')
    
    with col1:
        MDVP_Shim_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    
    with col1:
        PPE = st.text_input('PPE')
    
    
    parkinsons_diagnosis = ''
    
   
    if st.button('Parkinsons Test Result'):
       
        user_input = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_percent, MDVP_Jitter_Abs,
                      MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shim, MDVP_Shim_dB,
                      Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE,
                      DFA, spread1, spread2, D2, PPE]
        
       
        user_input = [float(x) for x in user_input]
        
        
        parkinsons_prediction = parkinsons_model.predict([user_input])
        
       
        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = 'The person has Parkinsons disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinsons disease'
        
       
        st.success(parkinsons_diagnosis)