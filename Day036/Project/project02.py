import os
import json
import html
import requests
from newsapi import NewsApiClient

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHAVANTAGE_URL = "https://www.alphavantage.co/query"
YESTERDAY = "2020-12-17"
TODAY = "2020-12-18"
NEWS_URL = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": os.environ["ALPHAVANTAGE_API_KEY"]
}

response = requests.get(ALPHAVANTAGE_URL, params=stock_params)
response.raise_for_status()
stock_data = response.json()

close_yesterday = float(stock_data["Time Series (Daily)"][YESTERDAY]["4. close"])
close_today = float(stock_data["Time Series (Daily)"][TODAY]["4. close"])
abs_percentage = abs((close_today - close_yesterday) * 100 / close_yesterday)
if abs_percentage >= 5:
    news_api = NewsApiClient(api_key=os.environ["NEWS_API_KEY"])
    all_articles = news_api.get_everything(q=COMPANY_NAME, from_param=YESTERDAY,
                                           to=TODAY, language='en')

    articles = all_articles["articles"][:3]

    for article in articles:
        headline = html.unescape(article["title"])
        brief = html.unescape(article["description"])
        print(f"HEADLINE: {headline}")
        print(f"BRIEF: {brief}")
        print()
