import streamlit as st
import pickle
import pandas as pd

def run():
    st.header('Welcome to Model Section')
    # Load All Files

    with open('all_process.pkl', 'rb') as file_1:
        all_process = pickle.load(file_1)



    guestroom = st.selectbox('Whether the house has an guest room',('no','yes'))
    airconditioning= st.selectbox('Whether the house has an air conditioning system',('no','yes'))
    prefarea= st.selectbox('Whether the house is located in a preferred area',('no','yes'))
    furnishingstatus= st.selectbox('Please enter furnishing status of the house',('unfurnished','semi-furnished','furnished'))
    area= st.number_input('Please enter total area of the house in square feet', min_value=0, step=1)
    bedrooms= st.number_input('Please enter number of bedrooms in the house', min_value=0,max_value=6, step=1)
    bathrooms= st.number_input('Please enter number of bathrooms in the house', min_value=0, max_value=4,step=1)
    stories= st.number_input('Please enter number of stories in the house', min_value=0,max_value=4,step=1)
    parking= st.number_input('Please enter number of parking spaces available within the house', min_value=0, max_value=3,step=1)



    data_inf = pd.DataFrame({
        'area': area,
        'bedrooms': bedrooms,
        'bathrooms' : bathrooms,
        'stories': stories,
        'parking': parking,
        'guestroom' : guestroom,
        'airconditioning': airconditioning,
        'prefarea': prefarea,
        'furnishingstatus': furnishingstatus,
        
    }, index =[0])

    st.table(data_inf)


    if st.button(label='predict'):
        
        # Predict Inference-Set

        y_pred_inf = all_process.predict(data_inf)

        st.write("Hasil Prediksi:", y_pred_inf)