import streamlit as st
import pandas as pd


def run_the_app():
    
    @st.cache
    def get_data():
       df = pd.read_csv('./data_in/학교현황(학급수)(초,중,고,그외).csv', encoding='cp949') 
       return df
        
    st.title('교육')
    df = get_data()
    st.dataframe(df)

if __name__ == "__main__":
    run_the_app()
