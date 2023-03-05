import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf
# import boto
import altair as alt



st.title('Techniator 💻 Fake News Detector')

st.markdown("""
This app receive a news article from the client and detect whether this news is fake or real by using machine learning
* **Python libraries:** pandas, streamlit, numpy, matplotlib, seaborn, scikit-learn
* **Data source:** [Kaggle - Fake and real news dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset).
""")

st.sidebar.header('User Input Features')
st.sidebar.markdown("<Pending>")

