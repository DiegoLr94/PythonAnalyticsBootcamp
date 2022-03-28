import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt # Graficos de datos


st.title('Reporte de EDA sobre accidentes de tránsito')

uploaded_file=st.file_uploader("Choose a file")

if uploaded_file is not None:
  data_accidente = pd.read_csv(uploaded_file)
  st.write(data_accidente)
data_accidente.head()


    
modalidad_count=data_accidente['MODALIDAD'].value_counts()
modalidad_count

modalidad_count.sort_values(ascending=False).plot(kind='bar')

    
conteo_región_x_modalidad=(data_accidente[['DEPARTAMENTO', 'MODALIDAD']]
                         .groupby(['DEPARTAMENTO', 'MODALIDAD']).size()
                         .reset_index()
                         .rename({0: 'conteo'}, axis=1))

g = sns.catplot(
    data=conteo_región_x_modalidad, kind="bar",
    x="DEPARTAMENTO", y="conteo", hue="MODALIDAD",
    height=5,aspect=2

)

g.set_xticklabels(rotation=90)
plt.show()

departamento_count=data_accidente['DEPARTAMENTO'].value_counts()
departamento_count

departamento_count.sort_values(ascending=False).plot(kind='bar')