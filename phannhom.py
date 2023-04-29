import streamlit as st
import numpy as np
import plotly.express as px
from df_change import df_change
from sklearn.cluster import KMeans

def phannhom():
  dfmid = df_change()
  dfmid.rename(columns={'S6' : 'Midterm Exam','S10' : 'Final Exam'}, inplace=True)
  slider = st.slider('Số nhóm:', min_value = 2, max_value = 5, step = 1)
  kmeans = KMeans(n_clusters=slider, n_init='auto')
  X = np.stack((dfmid['Homework'],dfmid['Midterm Exam'],dfmid['Final Exam'])).T
  kmeans.fit(X)
  st.write(px.scatter_3d(dfmid, x = 'Homework', y = 'Midterm Exam', z = 'Final Exam', color = kmeans.labels_))
  
  labels = np.array(['Nhóm '+str(i+1) for i in np.unique(kmeans.labels_)])
  radio = st.radio('Chọn nhóm:', labels, horizontal=True)
  kmeans.labels_ = np.array([str(i) for i in kmeans.labels_])
  df_need = dfmid.loc[kmeans.labels_==str(int(radio[-1])-1)]
  df_new = df_need[['NAME', 'CLASS', 'Homework', 'Midterm Exam', 'Final Exam', 'GPA']]
  
  new = df_new['GPA']
  st.write(radio+': GPA cao nhất',new.max(),', thấp nhất',new.min(),', trung bình',new.mean())
  st.write(df_new)
  
phannhom()