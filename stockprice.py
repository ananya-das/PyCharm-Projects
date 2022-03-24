import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""

    # Simple stock price prediction application
     Shown is the stock closing price and volume of google!
     
    """)
# define the ticker symbol
tickerSymbol = 'GOOGL'

# AAPL for apple, MSFT Microsoft, GOOGL for google

# get data to this ticker
tickerData = yf.Ticker(tickerSymbol)

# get the historical price for this ticker
tickerDf = tickerData.history(period='1d', start='2011-5-31', end='2022-2-28')

# Open High low close Volume Dividends stock splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

tickerData.recommendations
tickerData.calendar



