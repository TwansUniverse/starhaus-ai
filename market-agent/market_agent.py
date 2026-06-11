import yfinance as yf
import ta

ticker = yf.Ticker("SPY")

df = ticker.history(period="3mo")

df["EMA20"] = ta.trend.ema_indicator(df["Close"], window=20)
df["EMA50"] = ta.trend.ema_indicator(df["Close"], window=50)
df["RSI"] = ta.momentum.rsi(df["Close"], window=14)

#print("Rows:", len(df))
#print(df.head())


latest = df.iloc[-1]

#print(df[["Close", "EMA20", "EMA50", "RSI"]].tail())

print("\n=== Market Analysis===")

print(f"Price: ${latest['Close']:.2f}")
print(f"EMA20: ${latest['EMA20']:.2f}")
print(f"EMA50: ${latest['EMA50']:.2f}")
print(f"RSI: {latest['RSI']:.2f}")

if latest["Close"] > latest["EMA20"]:
    print("Trend: Bullish")

else:
    print("Trend: Bearish")


