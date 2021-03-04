print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm")
print("-------------------------")
print("LATEST DAY: 2018-02-20")
print("LATEST CLOSE: $100,000.00")
print("RECENT HIGH: $101,000.00")
print("RECENT LOW: $99,000.00")
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")



searchtickers = []
entering = True

while entering:
    ticker = input("Please enter the ticker symbol of one stock or cryptocurrency (or enter 'finished' if done):")

    if ticker == 'finished':
        entering = False

    nonumbers=True
    tickerlist = list(ticker)
    for i in tickerlist:
        if i == "0" or i =="1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
            print("Please enter a correctly formatted symbol like 'MSFT' (between 1 to 5 digits, does not include numeric digits).")
            print("Please try again. ")
            nonumbers = False
            break

    if nonumbers:
        if (len(ticker) > 5 or len(ticker) == 0) and ticker != 'finished':
            print("Please enter a correctly formatted symbol like 'MSFT' (between 1 to 5 digits).")
            print("Please try again.")

        elif len(ticker) > 0 and len(ticker) <= 5:
            ticker = ticker.upper()
            searchtickers.append(ticker)



#API key# API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
#API_KEY = "abc123"
#API_KEY = getpass("Please input your API key:")



import os
from getpass import getpass
from dotenv import load_dotenv
#https://github.com/theskumar/python-dotenv

load_dotenv()

APIKEY = os.getenv("USER_NAME", default="Player One")



#fetching data


import requests
import json

for symbol in searchtickers:
    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={API_KEY}"
    response = requests.get(request_url)
    parsed_response = json.loads(response.text)
