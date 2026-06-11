#supervisors job - read news sentiment; read market indicators; ask ollama for a conclusion; produce a daily trade thesis
#i will first hardcode values, then we will complicate it"
import requests 

OLLAMA_URL = "http://localhost:11434/api/generate"

news_sentiment = 7

news_summary = """ Positive earnings reports across the semiconductor sector. Strong AI demand continues to drive growth."""

price = 737.76
ema20 = 728.10
ema50 = 710.25
rsi = 62.4

prompt = f""" You are a financial analyst. 

News Analysis:
Sentiment Score: {news_sentiment}

Summary:
{news_summary}

Market Analysis:
Current Price: {price}
EMA20: {ema20}
EMA50: {ema50}
RSI: {rsi}


Provide:
1. Market Outlook
2. Risks
3. Opportunities
4. Recommendation (BUY, SELL, HOLD)
5. Confidence Score (1-100)

Format clearly.
"""

response = requests.post(
    OLLAMA_URL, 
    json={
        "model": "llama3.2:3b",
        "prompt": prompt,
        "stream": False
    }
)


print("\n===== SUPERVISOR REPORT =====\n")
print(response.json()["response"])
