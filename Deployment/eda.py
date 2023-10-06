import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


def eda1():
       df = pd.read_csv('Housing.csv')
       skewness = df['price'].skew()
       st.write(f'Histogram of price')
       fig1, ax = plt.subplots()
       sns.histplot(data=df, x='price', kde=True, ax=ax)
       plt.title(f'Histogram of price (Skewness: {skewness:.2f})')
       st.pyplot(fig1)
       with st.expander('Explanation'):
              st.markdown('Dapat dilihat dari gambar bahwa distribusi data price tidak normal dengan nilai skewnya 1.21')

       skewness = df['area'].skew()
       st.write(f'Histogram of area')
       fig2, ax = plt.subplots()
       sns.histplot(data=df, x='area', kde=True, ax=ax)
       plt.title(f'Histogram of area (Skewness: {skewness:.2f})')
       st.pyplot(fig2)
       with st.expander('Explanation'):
              st.markdown('Dapat dilihat dari gambar bahwa distribusi data area tidak normal dengan nilai skewnya 1.32')


def eda2():
       df = pd.read_csv('Housing.csv')
       fig3, ax = plt.subplots()
       barplots = sns.countplot(data=df,x='bedrooms', ax=ax)
       for ix in barplots.containers:
              barplots.bar_label(ix)     
       plt.title(f'Bar plot of bedrooms')
       plt.show()
       st.pyplot(fig3)
       with st.expander('Explanation'):
              st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah mempunyai 3 kamar tidur pada rumahnya dengan jumlah 300 rumah')

       fig4, ax = plt.subplots()
       barplots = sns.countplot(data=df,x='bathrooms', ax=ax)
       for ix in barplots.containers:
              barplots.bar_label(ix)     
       plt.title(f'Bar plot of bathrooms')
       plt.show()
       st.pyplot(fig4)
       with st.expander('Explanation'):
              st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah mempunyai 1 kamar mandi pada rumahnya dengan jumlah 401 rumah')

       fig5, ax = plt.subplots()
       barplots = sns.countplot(data=df,x='stories', ax=ax)
       for ix in barplots.containers:
              barplots.bar_label(ix)     
       plt.title(f'Bar plot of stories')
       plt.show()
       st.pyplot(fig5)
       with st.expander('Explanation'):
              st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah mempunyai 2 lantai pada rumahnya dengan jumlah 238 rumah')

       fig6, ax = plt.subplots()
       barplots = sns.countplot(data=df,x='parking', ax=ax)
       for ix in barplots.containers:
              barplots.bar_label(ix)     
       plt.title(f'Bar plot of parking')
       plt.show()
       st.pyplot(fig6)
       with st.expander('Explanation'):
              st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah tidak mempunyai parkir pada rumahnya dengan jumlah 299 rumah')

def eda3():
       df = pd.read_csv('Housing.csv')
       cat_col_ohe = ['mainroad','guestroom','basement','hotwaterheating','airconditioning','prefarea','furnishingstatus']
       selected_column = st.sidebar.selectbox("Select a categorical column", cat_col_ohe)

       # Calculate category counts
       category_counts = df[selected_column].value_counts()

       # Create a pie chart
       st.write(f'**Pie Chart of {selected_column}**')
       fig, ax = plt.subplots()
       ax.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140)
       ax.set_title(f'Pie Chart of {selected_column}')
       st.pyplot(fig)

       with st.expander('Explanation'):
              if selected_column == 'mainroad':
                     st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah terhubung dengan jalan utama dengan persentase 85.9%')
              elif selected_column == 'guestroom':
                     st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah tidak memiliki kamar tamu dengan persentase 82.2%')
              elif selected_column == 'basement':
                     st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah tidak memiliki basement dengan persentase 65%')
              elif selected_column == 'hotwaterheating':
                     st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah tidak memiliki sistem pemanas air dengan persentase 95.4%')
              elif selected_column == 'airconditioning':
                     st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah tidak memiliki AC dengan persentase 68.4%')
              elif selected_column == 'prefarea':
                     st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah berlokasi di area yang tidak diinginkan dengan persentase 76.5%')
              elif selected_column == 'furnishingstatus':
                     st.markdown('Dapat dilihat dari gambar bahwa mayoritas rumah memiliki sebagian perabotan saja dengan persentase 41.7%')

def run():
    st.header('Welcome to EDA Section')


    pilih = st.selectbox(label='Select EDA', options=['EDA 1', 'EDA 2', 'EDA 3'])

    if pilih == 'EDA 1':
        eda1()

    elif pilih == 'EDA 2':
        eda2()

    elif pilih == 'EDA 3':
        eda3()

if __name__ == '__main__':
    run()