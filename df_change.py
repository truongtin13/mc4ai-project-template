import numpy as np
import pandas as pd
import streamlit as st

def df_change():
  df = pd.read_csv("py4ai-score.csv", low_memory=False)
  dfmid = df.copy()
  COLS = dfmid.columns.values.tolist().copy()
  def gen(row):
    if row[COLS[1]] == 'M':
      return 'Nam'
    else:
      return 'Nữ'
  dfmid['Gen'] = dfmid.apply(gen, axis=1)
  subjects = np.array([['Anh','CA', 'ts'],
             ['Hoá','CH','ts'],
             ['Lý', 'CL','ts'],
             ['Sinh','CS','ts'],
             ['Toán','CT','ts'],
             ['Tin','CTIN','ts'],
             ['Trung - Nhật','CTRN','ts'],
             ['Văn', 'CV','ts'],
             ['Tích hợp / Song ngữ', 'TH','SN'],
             ['Khác', 'A', 'B'],
             ['Sử - Địa', 'CSĐ','ts']])
  def subject(row):
    r = ''.join(re.findall('\D', row[COLS[2]]))
    for i in subjects:
      if r == i[1] or r == i[2]:
        return i[0]
  dfmid['Subject'] = dfmid.apply(subject, axis=1)
  
  st.write(dfmid)
  st.write(np.unique(dfmid[COLS[2]]))
  
df_change()
