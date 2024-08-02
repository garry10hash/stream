import streamlit as st
st.title('Loan Approval App')
st.write('Check your eligibility')
c=st.number_input('Enter your credit score')
s=st.number_input('Enter your salary')
st.button('Check')
if s>=50000 and c>=500:
    st.write('Congratulations you are eligible')
    st.balloons()
else:
    st.write('Sorry! you are not eligible')
