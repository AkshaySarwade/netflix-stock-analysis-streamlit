#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Netflix Stock Analysis", layout="wide")
st.title("📈 Netflix Stock Price Analysis")

# ---------------------------------
# Load dataset
# ---------------------------------
@st.cache_data
def load_data():
    df = pd.read_csv("NFLX.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    return df.sort_values("Date")

data = load_data()

st.subheader("📄 Dataset Preview")
st.dataframe(data.head())

# ---------------------------------
# Closing price trend
# ---------------------------------
st.subheader("📉 Closing Price Trend")

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(data["Date"], data["Close"])
ax.set_xlabel("Date")
ax.set_ylabel("Closing Price ($)")
ax.set_title("Netflix Closing Price Over Time")

st.pyplot(fig)

# ---------------------------------
# Moving averages
# ---------------------------------
st.subheader("📊 Moving Averages")

short_window = st.slider("Short Moving Average (days)", 5, 50, 20)
long_window = st.slider("Long Moving Average (days)", 50, 200, 100)

data["MA_Short"] = data["Close"].rolling(short_window).mean()
data["MA_Long"] = data["Close"].rolling(long_window).mean()

fig2, ax2 = plt.subplots(figsize=(8, 4))
ax2.plot(data["Date"], data["Close"], label="Close Price")
ax2.plot(data["Date"], data["MA_Short"], label=f"{short_window}-Day MA")
ax2.plot(data["Date"], data["MA_Long"], label=f"{long_window}-Day MA")
ax2.legend()
ax2.set_title("Netflix Price with Moving Averages")

st.pyplot(fig2)

# ---------------------------------
# Insights
# ---------------------------------
st.subheader("🧠 Insights")
st.write(
    "Moving averages help identify trends and potential crossover signals. "
    "This app allows dynamic exploration of Netflix stock behavior over time."
)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




