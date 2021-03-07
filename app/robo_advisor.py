# print("-------------------------")
# print("SELECTED SYMBOL: XYZ")
# print("-------------------------")
# print("REQUESTING STOCK MARKET DATA...")
# print("REQUEST AT: 2018-02-20 02:00pm")
# print("-------------------------")
# print("LATEST DAY: 2018-02-20")
# print("LATEST CLOSE: $100,000.00")
# print("RECENT HIGH: $101,000.00")
# print("RECENT LOW: $99,000.00")
# print("-------------------------")
# print("RECOMMENDATION: BUY!")
# print("RECOMMENDATION REASON: TODO")
# print("-------------------------")
# print("HAPPY INVESTING!")
# print("-------------------------")


addmore = True
entering = True


while addmore:

    while entering:
        ticker = input("Please enter the ticker symbol of one stock or cryptocurrency:")

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
                entering = False


    #THIS BELOW CODE IS FROM THE CLASS COLAB FOR THIS ROBO-ADVISOR project
    #https://colab.research.google.com/drive/1EH3xNXPrO4dniIW12X9ATDz1lMyMBREb?usp=sharing#scrollTo=LY1po1fUMtW8


    import os
    from getpass import getpass
    from dotenv import load_dotenv
    #https://github.com/theskumar/python-dotenv

    load_dotenv()
    #API key
    API_KEY = os.getenv("ALPHAVANTAGE_API_KEY")
    #API_KEY = "abc123"
    #API_KEY = getpass("Please input your API key:")


    #fetching data


    import requests
    import json
    records = []

    request_url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}"

    try:

        response = requests.get(request_url)
        parsed_response = json.loads(response.text)

        for date, daily_data in parsed_response["Time Series (Daily)"].items():

            record = {
                "date": date,
                "open": float(daily_data["1. open"]),
                "high": float(daily_data["2. high"]),
                "low": float(daily_data["3. low"]),
                "close": float(daily_data["4. close"]),
                "volume": int(daily_data["5. volume"]),
            }
            records.append(record)

        #END CODE FROM CLASS COLAB

        from pandas import DataFrame

        dfrecords = DataFrame(records)
        print(dfrecords)

        morestocks = input("Do you wish to receive advice on another stock or cryptocurrency? ['yes'/'no']:")
        if morestocks != "yes" and morestocks !="no":
            print("Please enter either 'yes' or 'no'.")
        elif morestocks == "no":
            addmore = False
            print("Thank you for using the Robo Advisor!")
        elif morestocks == "yes":
            entering = True

    except:
        print("Oops, that stock symbol was not found. Please try again.")
        entering = True
