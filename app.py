import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import seaborn as sns
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import mplfinance as mpf
from scipy.signal import argrelextrema


icon ="./leaf-xxl.png"
st.set_page_config(page_icon=icon,layout="wide")

data=pd.DataFrame({
    'Wastewater treatment and discharge': [310941,324857,339323,341389,396711,411902,448001,433773,0,0,0],
    'Incineration and open burning of waste': [34193,35231,36290,37371,40596,41797,43029,44290,0,0,0],
    'Solid Waste Disposal':[ 1083489,1206148,1326882,1445929,1751143,1881488,2010743,2139163,2266978,2124312,1990623 ],
    'year':[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]
})

st.markdown("<br>", unsafe_allow_html=True)
st.image(icon, width=80)

st.title('Its Time To Green Up')
st.write("Climate change is affecting all of us, what are you doing about it?")



left_column, right_column = st.columns(2)


fig = px.line(data, x="year")

right_column.write(fig)
left_column.write(data)




from datetime import datetime

df = pd.read_csv('BTCUSDT-5m-2021-06.csv',names=["Date", "Open", "High", "Low", "Close", "Volume", "Close time",
                      "Quote asset volume", "Number of trades", "Taker buy base asset volume",
                      "Taker buy quote asset volume", "Ignore"],parse_dates=True)
df['Date'] = pd.to_datetime(df['Date'])
df.set_index(df["Date"],inplace=True)
df=df.head(500)

maxima=argrelextrema(np.array(df["Close"]), np.greater,0,3)
minima=argrelextrema(np.array(df["Close"]), np.less,0,2)
updated_maxima = []
maxima_time = []
for point in maxima[0]:
    updated_maxima.append(df["Close"][point])
    maxima_time.append(df.index[point])


updated_minima = []
minima_time = []
for point in minima[0]:
    updated_minima.append(df["Close"][point])
    minima_time.append(df.index[point])





candlestick = go.Candlestick(
                            x=df.index,
                            open=df['Open'],
                            high=df['High'],
                            low=df['Low'],
                            close=df['Close']
                            )

fig = go.Figure(data=candlestick)


fig.add_trace(
    go.Scatter(
        x=maxima_time,
        y=updated_maxima,
        )
)

"""fig.add_trace(
    go.Scatter(
        x=minima_time,
        y=updated_minima,
        )
)"""

fig.update_layout(
    width=800, height=600,
)

st.write(fig)


#mpf.plot(df.head(100),type='candle')



  