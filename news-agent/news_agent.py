import feedparser
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

RSS_FEED = "https://feeds.marketwatch.com/marketwatch/topstories/"

feed = feedparser.parse(RSS_FEED)

for entry in feed.entries[:5]:
    headline = entry.title
    prompt = f"""
    Analyze this financial headline.

    Headline: {headline}
    Give:
    1. Summary
    2. Market Sentiment (Bullish, Bearish, Neutral)
    3. Potential Sectors affected
    """

    response = requests.post(
       OLLAMA_URL,
       json={
           "model": "llama3.2:3b",
           "prompt": prompt,
           "stream": False
       }
    )

   # print(response.text)

    print("\n========================")
    print("HEADLINE:")
    print(headline)

    print("\nAI ANALYSIS:")
   # print(result)
   # print("STATUS:", response.status_code)
   # print("RAW RESPONSE:")
    print(response.text)
#    print("OLLAMA_URL =", repr(OLLAMA_URL))
