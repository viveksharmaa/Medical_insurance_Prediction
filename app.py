#importing Necessary Libraries
import numpy as np
import pandas as pd
import pickle as pkl 
import streamlit as st

model = pkl.load(open('MLProjectFinal.pkl', 'rb'))

st.header('Medical Insurance Premium Predictor')

age = st.slider('Enter Age', 5 , 80)
gender = st.selectbox('2. Choose Gender',['Female','Male'])
bmi = st.slider('Enter BMI', 5 , 100)
weight = st.slider('4. Enter your Weight',0,100)
hereditary_diseases = st.selectbox('5. Choose Disease',['Alzheimer','Arthritis','Cancer','Diabetes','Epilepsy','EyeDisease','HeartDisease','High BP','NoDisease','Obesity'])
children = st.slider('6. Choose No of Childrens', 0, 5)
smoker = st.selectbox('7. Are you a smoker ?',['Yes','No'])
bloodpressure = st.slider('8. BloodPressure',60,140 )
diabetes = st.selectbox('9. Diabetes ?', ['Yes','No'])
regular_ex = st.selectbox('10. Regular Exercise ?', ['Yes','No'])
job_title = st.selectbox('11. What is your Job Title?',['Actor', 'Engineer', 'Academician', 'Chef', 'HomeMakers', 'Dancer',
 'Singer', 'DataScientist', 'Police', 'Student', 'Doctor',
 'Manager', 'Photographer', 'Beautician', 'CA', 'Blogger', 'CEO',
 'Labourer', 'Accountant', 'FilmDirector', 'Technician',
 'FashionDesigner', 'Architect', 'HouseKeeper', 'FilmMaker',
 'Buisnessman', 'Politician', 'DefencePersonnels', 'Analyst',
 'Clerks', 'ITProfessional', 'Farmer', 'Journalist', 'Lawyer',
 'GovEmployee'])
region = st.selectbox('12. Select Your Region',['Southern','West','North-East','Mid-West'])




if st.button('Predict'):
    if gender == 'Female':
     gender = 0
    else:
        gender = 1
    # For hereditary_diseases
    if hereditary_diseases == 'Alzheimer':
            hereditary_diseases = 0
    elif hereditary_diseases == 'Arthritis' :
        hereditary_diseases = 1        
    elif hereditary_diseases == 'Cancer' :
        hereditary_diseases = 2
    elif hereditary_diseases == 'Diabetes' :
        hereditary_diseases = 3
    elif hereditary_diseases == 'Epilepsy' :
        hereditary_diseases = 4
    elif hereditary_diseases == 'EyeDisease' :
        hereditary_diseases = 5 
    elif hereditary_diseases == 'HeartDisease' :
        hereditary_diseases = 6
    elif hereditary_diseases == 'High BP' :
        hereditary_diseases = 7                 
    elif hereditary_diseases == 'NoDisease' :
        hereditary_diseases = 8
    else  :
        hereditary_diseases = 9  

    #For Smokers 
    if smoker == 'Yes':
        smoker = 1
    else :
        smoker = 0
    if diabetes == 'Yes':
        diabetes = 1
    else:
        diabetes = 0
    #Regular exercise
    if regular_ex == 'Yes':
        regular_ex=1
    else:
        regular_ex = 0


    # region
    if region =='Mid-West'  :
        region = 0

    elif region  == 'North-East':
        region = 1

    elif region == 'Southern'   :
        region = 2

    else:
        region = 3   

    # Job Title 
    if job_title == "Actor":
      job_title = 0
    elif job_title == "Engineer":
      job_title = 1
    elif job_title == "Academician":
      job_title = 2
    elif job_title == "Chef":
      job_title = 3
    elif job_title == "HomeMakers":
      job_title = 4
    elif job_title == "Dancer":
      job_title = 5
    elif job_title == "Singer":
      job_title = 6
    elif job_title == "DataScientist":
      job_title = 7
    elif job_title == "Police":
      job_title = 8
    elif job_title == "Student":
      job_title = 9
    elif job_title == "Doctor":
      job_title = 10
    elif job_title == "Manager":
        job_title = 11
    elif job_title == "Photographer":
      job_title = 12
    elif job_title == "Beautician":
      job_title = 13
    elif job_title == "CA":
      job_title = 14
    elif job_title == "Blogger":
      job_title = 15
    elif job_title == "CEO":
      job_title = 16
    elif job_title == "Labourer":
      job_title = 17
    elif job_title == "Accountant":
      job_title = 18
    elif job_title == "FilmDirector":
      job_title = 19
    elif job_title == "Technician":
      job_title = 20
    elif job_title == "FashionDesigner":
      job_title = 21
    elif job_title == "Architect":
      job_title = 22
    elif job_title == "HouseKeeper":
      job_title = 23
    elif job_title == "FilmMaker":
      job_title = 24
    elif job_title == "Buisnessman":
      job_title = 25
    elif job_title == "Politician":
      job_title = 26
    elif job_title == "DefencePersonnels":
      job_title = 27
    elif job_title == "Analyst":
      job_title = 28
    elif job_title == "Clerks":
      job_title = 29
    elif job_title == "ITProfessional":
      job_title = 30
    elif job_title == "Farmer":
      job_title = 31
    elif job_title == "Journalist":
      job_title = 32
    elif job_title == "Lawyer":
       job_title = 33
    elif job_title == "GovEmployee":
      job_title = 34
    else:
      job_title = -1  # default if not matched



    input_data = (age, gender,weight, bmi, hereditary_diseases,children,smoker, bloodpressure,diabetes,regular_ex,job_title,region)
    input_data_array = np.asarray(input_data)
    input_data_array = input_data_array.reshape(1,-1)
    predicted_prem = model.predict(input_data_array)

    display_string = 'Insurance Premium will be '+ str(round(predicted_prem[0],2)) + ' Indian Rupees'

    st.markdown(display_string)

