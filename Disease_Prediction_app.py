import os
import pickle
import streamlit as st  # type: ignore
from streamlit_option_menu import option_menu  # type: ignore

# Set page Configuration
st.set_page_config(
    page_title="Prediction of Disease Outbreaks",
    layout="wide",
    page_icon="🧑"
)

# Getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# Loading the saved models
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.pkl', 'rb'))
heart_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))
parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Prediction of Disease Outbreaks System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction'],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col2:
        Glucose = st.text_input('Glucose Level')

    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')

    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col3:
        BMI = st.text_input('BMI Value')

    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')

    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ' '

    # Creating button for Prediction
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.selectbox('Sex - Male-1, Female-0', [1, 0])

    with col3:
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')

    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl : Yes-1, No-0', options=['1', '0'])

    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results: Normal-0, ST-T wave abnormality-1, Left ventricular hypertrophy-2', options=['0', '1', '2'])

    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')

    with col3:
        exang = st.selectbox('Exercise Induced Angina : Yes-1, No-0', options=['1', '0'])

    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')

    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=['0', '1', '2'])  # Added missing feature

    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Flourosopy', options=['0', '1', '2', '3'])

    with col1:
        thal = st.selectbox('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect', options=['0', '1', '2'])

    # Code for Heart Prediction
    heart_diagnosis = ' '

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        cp_mapping = {
            'Typical Angina': 0,
            'Atypical Angina': 1,
            'Non-anginal Pain': 2,
            'Asymptomatic': 3
        }
        cp_numeric = cp_mapping[cp]

        fbs_mapping = {'1': 1, '0': 0}
        fbs_numeric = fbs_mapping[fbs]

        restecg_mapping = {
            '0': 0,
            '1': 1,
            '2': 2
        }
        restecg_numeric = restecg_mapping[restecg]

        exang_mapping = {'1': 1, '0': 0}
        exang_numeric = exang_mapping[exang]

        # Collect user input values
        user_input = [age, sex, cp_numeric, trestbps, chol, fbs_numeric, restecg_numeric, thalach, exang_numeric, oldpeak, slope, ca, thal]

        # Ensure the length of user_input matches the number of features expected by the model
        if len(user_input) != 13:
            st.error(f"Expected 13 features, but got {len(user_input)} features. Please check the input data.")
        else:
            user_input = [float(x) for x in user_input]
            heart_prediction = heart_model.predict([user_input])

            if heart_prediction[0] == 1:
                heart_diagnosis = 'The Person is having heart disease'
            else:
                heart_diagnosis = 'The Person does not have any heart disease'

    st.success(heart_diagnosis)


# Parkinson's Prediction Page
if selected == "Parkinsons Disease Prediction":
    # Page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('Shimmer:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # Code for Parkinson's Prediction
    parkinsons_diagnosis = ' '

    # Creating a Button For Prediction
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, 
                      Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The Person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The Person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)