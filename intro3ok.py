import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Korelasi BOR dengan Jumlah Kematian Covid-19", layout="wide")

df = pd.read_excel("TgsDQlab.xlsx")
df1= pd.read_excel("TgsDQlab1.xlsx")

st.title("Korelasi BOR dengan Jumlah Kematian Covid-19")
st.subheader("Apa itu BOR?")
st.write ("Bed Occupancy Rate (BOR) adalah Persentase penggunaan tempat tidur yang ada di rumah sakit. Rumus BOR yaitu BOR= Hari Perawatan/(Jumlah tempat tidur*Jumlah hari)*100%. Menurut Depkes BOR Ideal antara 60-85%. Disisi lain, Pandemi Covid-19 di Indonesia mulai Maret 2020")
c1,c2, c3= st.columns(3)
with c1:
    #st.subheader("Persentase BOR (%) Provinsi Jawa Timur")
    plot = px.line(df,x='Tahun', y='BOR (%)',title="Persentase BOR (%) Provinsi Jawa Timur tahun 2010-2021", 
    text='BOR (%)',color_discrete_sequence=['#F63366']*len(df), template='plotly_white')
    st.plotly_chart(plot)
with c3:
    st.subheader("Korelasi BOR (%) dan Jumlah Kematian Covid-19 Provinsi Jawa Timur")
    st.metric(label="P-value Korelasi Pearson", value="0.156")
    st.write ("Persentase BOR di Jawa Timur selama pandemi justru mengalami penurunan, dimana tren BOR turun dari tahun 2010-2021. Hasil Uji Korelasi Pearson BOR dengan Jumlah kematian Covid19 diketahui p.value = 0,156 > 0,05 sehingga tidak ada hubungan antara BOR dan jumlah kematian Covid-19")

c4,c5,c6 = st.columns(3)
with c4:
    #st.subheader("Distribusi BOR (%) dan Jumlah Kematian Covid-19 Provinsi Jawa Timur")
    plot1 = px.scatter(df1,x='BOR(%)', y='Jumlah Kematian Covid-19', hover_name='Kota/Kab', title="Distribusi BOR (%) dan Jumlah Kematian Covid-19 Provinsi Jawa Timur")
    st.plotly_chart(plot1)
with c6:
    st.subheader("                   ")
    st.subheader("                   ")
    st.subheader("                   ")
    st.subheader("                   ")
    st.write ("Dari distribusi BOR dan jumlah kematian Covid-19 tampak BOR disekitar 40-50% baik jumlah kematian tinggi maupun rendah di kab/kota Prov Jawa Timur.")

