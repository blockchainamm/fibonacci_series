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
st.title("Fibonacci numbers")

nos = st.number_input(label="Enter the number of terms",step=1)

n1, n2 = 0, 1
i = 0

if nos > 0:
    st.write(f'The following is the series of fibonacci numbers for {nos} values')

while i < nos:
    #print(n1)
    st.write(n1)
    new_nm = n1 + n2
    n1 = n2
    n2 = new_nm 
    i += 1
