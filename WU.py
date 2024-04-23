import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import re 

st.set_page_config(page_title="WU Directory", layout="wide")

st.title('Another Directory at Westminster University')
st.write("This is an enhanced alternative to the employee [directory](https://westminsteru.edu/campus-directory/index.html) at Westminster University." )

data = pd.read_csv('WU_directory.csv') 

department = st.selectbox(
    'Choose a department:',
    np.insert(np.sort(data['department'].unique()),0,"All Departments"))

# col4 is empty 
col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.text("Type of Role:") # add a text 
with col2:
    role_faculty = st.checkbox('Faculty', value=1, key='faculty_checkbox')
    
with col3:
    role_staff = st.checkbox('Staff', value=1, key='staff_checkbox')
    

     
## filter the data for the choice only
if department != "All Departments":
    data = data.query("department == '{}'".format(department))
    ##mask = data['department'] ==  department
    ##data = data[mask]


if not role_faculty:
    data = data.query("role != 'Faculty'")

if not role_staff:
    data = data.query("role != 'Staff'")


st.dataframe(data, hide_index=True)

 

