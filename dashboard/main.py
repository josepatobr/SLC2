import streamlit as st
import numpy as np
import pandas as pd

def dashboard():
    chart_data = pd.DataFrame(
        np.random.randn(13, 3),
        columns=['quantidades', 'preço', 'vendas'])
    


    st.line_chart(chart_data)

dashboard()