import streamlit as st
import pandas as pd
import os



st.sidebar.page_link('pages/0_generate_invoice.py',        label="Generate Invoice",               icon="🏡")
st.sidebar.page_link('pages/1_list_of_clients_projects.py',label="List of Clients / Projects List",icon="📓")    
st.sidebar.page_link('pages/2_add_new_client_project.py',  label="Add New Client/Project record",  icon="✒️")  


def load_dataframe(file_path, worksheet_name):
    try:
        df = pd.read_excel(file_path, sheet_name= worksheet_name)
        return df
    except FileNotFoundError:
        st.write(f"File {file_path} not found.")
        exit()

try:
    file_path = os.path.join(os.getcwd(), 'InvoiceLogTemplate.xlsx')  # Full file path
    worksheet_name_1 = "InvoiceLogTemplate"
    df_1 = load_dataframe(file_path, worksheet_name_1)


    worksheet_name_2 = "Clients"
    df_2 = load_dataframe(file_path, worksheet_name_2)

    file_path_csv = 'new_record.csv'
    new_data = pd.read_csv(file_path_csv)


    col1, col2, col3 = st.columns([1,1,2])
    with col1:
        display_full_data = st.checkbox("Show DataFrame", value=True)
    with col2:    
        display_new_record = st.checkbox("New Record")
    with col3:
        pass

    if display_full_data:
        st.dataframe(df_1)

    if display_new_record:
        st.dataframe(df_2)

except:
    pass