## STEP 1: `project01.py` 
Use [https://www.alphavantage.co](https://www.alphavantage.co)  
When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then `print("Get News")`.

## STEP 2: `project02.py` 
Use [https://newsapi.org](https://newsapi.org)
Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: `project.py` 
Use [https://www.twilio.com](https://www.twilio.com)
Send a separate message with the percentage change and each article's title and description to your phone number. 

Format the SMS message like this: 
```
"""
TSLA: (arrow up emoji) 2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: (arrow down emoji) 5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
```
