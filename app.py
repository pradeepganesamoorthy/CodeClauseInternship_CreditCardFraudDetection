import joblib
import streamlit as st
import requests

# logistic_l2 = joblib.load('l2logistic_cc_predict.pkl')
XGB_model = joblib.load('XGB_cc_predict.pkl')
st.title('Credict Card Fraud Detection')
v1=st.number_input('Enter value of v1')
v2=st.number_input('Enter value of v2')
v3=st.number_input('Enter value of v3')
v4=st.number_input('Enter value of v4')
v5=st.number_input('Enter value of v5')
v6=st.number_input('Enter value of v6')
v7=st.number_input('Enter value of v7')
v8=st.number_input('Enter value of v8')
v9=st.number_input('Enter value of v9')
v10=st.number_input('Enter value of v10')
v11=st.number_input('Enter value of v11')
v12=st.number_input('Enter value of v12')
v13=st.number_input('Enter value of v13')
v14=st.number_input('Enter value of v14')
v15=st.number_input('Enter value of v15')
v16=st.number_input('Enter value of v16')
v17=st.number_input('Enter value of v17')
v18=st.number_input('Enter value of v18')
v19=st.number_input('Enter value of v19')
v20=st.number_input('Enter value of v20')
v21=st.number_input('Enter value of v21')
v22=st.number_input('Enter value of v22')
v23=st.number_input('Enter value of v23')
v24=st.number_input('Enter value of v24')
v25=st.number_input('Enter value of v25')
v26=st.number_input('Enter value of v26')
v27=st.number_input('Enter value of v27')
v28=st.number_input('Enter value of v28')
v29=st.number_input('Enter value of v29')
v30=st.number_input('Enter value of v30')




# def predict():
#     prediction = XGB_model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30]])
    
#     if prediction == 1:
#         st.error("Fraud Transaction :rage:")
#     else:
#         st.success("Normal Transaction :grinning:")
    

pred = st.button('Predict')

if pred:
    prediction = XGB_model.predict([[v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30]])
    if prediction == 1:
        st.error("Fraud Transaction :rage:")
    else:
        st.success("Normal Transaction :grinning:")