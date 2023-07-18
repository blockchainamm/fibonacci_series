import streamlit as st

# --- Hide Streamlit Style ---
hide_st_style = """
                <style>
                #MainMenu {Visibility: hidden;}
                footer {Visibility: hidden;}
                header {Visibility: hidden;}
                </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

st.title("Body Mass Index Calculator")

weight = st.number_input('weight in kgs',step=.1,format="%.2f")
height = st.number_input('height in m',step=.01,format="%.2f")

def bmical():
    bm_index = weight / (height ** 2)
    return bm_index

def bmianalysis(bmi):
    if bmi < 18.5:
        condition = 'Underweight'
    elif bmi >= 18.5 and bmi <= 24.9:
        condition = 'Normal'
    elif bmi >= 25.0  and bmi < 29.9:
        condition = 'Overweight'
    elif bmi >= 30.0:
        condition = 'Obese'
        
    return condition

if weight > 0 and height > 0:
    bmi = bmical()
    #print (f'The body mass index of a person with weight {weight} kgs and height {height} m is {bmi}')
    bmi_condition = bmianalysis(bmi)
    #print (f'Your body mass index is {bmi}, this is considered {bmi_condition}')

    st.write('Body Mass Index')
    st.write(bmi)

    st.write('BMI condition')
    st.write(bmi_condition)