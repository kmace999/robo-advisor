
addmore = True
entering = True

#import seaborn as sns

#start copied function from past project readme setups
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#end copied function from past project readme setups


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

    print("-------------------------")
    print(f"SELECTED SYMBOL: {ticker}")
    print("-------------------------")
    print("REQUESTING STOCK MARKET DATA...")

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

        import pandas as pd
        from pandas import DataFrame

        dfrecords = DataFrame(records)
        #print(dfrecords)

        dfrecords.to_csv('data/prices.csv', index = False)


        from datetime import datetime
        thisday = datetime.now()
        requestdate = thisday.strftime("%m/%d/%Y %H:%M")


        #algorithm for recommendation
        explanation = []
        latestclose = dfrecords["close"].values
        closed = latestclose[0]
        recenthigh = dfrecords["high"].max()
        recentlow = dfrecords["low"].min()
        meanclose = dfrecords["close"].mean()
        medclose = dfrecords["close"].median()
        compratio = meanclose/medclose
        #if the stock's latest closing price is less than 20% above its recent low buy, else don't buy (using the recommended method from the README)
        compare1 = 1.2*recentlow
        if closed < compare1:
            rec1 = 1
            explanation.append("The stock or cryptocurrency's latest closing price is less than 20% above its recent low.")
        else:
            rec1 = 0
            explanation.append("The stock or cryptocurrency's latest closing price is greater than 20% above its recent low.")
        #if the stock's latest closing price is more than 30% below it's recent high, don't buy, otherwise buy
        compare2 = .7*recenthigh
        if closed < compare2:
            rec2 = 0
            explanation.append("The stock or cryptocurrency's latest closing price is less than 30% below its recent high.")
        else:
            rec2 = 1
            explanation.append("The stock or cryptocurrency's latest closing price is greater than 30% below its recent high.")

        #compare median and mean to search for outliers
        #if mean/median > 1.1 or mean/median < .9
        if .9 < compratio < 1.1:
            rec3 = 1
            explanation.append("The stock or cryptocurrency's mean to median ratio is between 90% and 110%.")
        else:
            rec3=0
            if compratio > 1.1:
                explanation.append("The stock or cryptocurrency's mean to median ratio is greater than 110%.")
            if compratio < .9:
                explanation.append("The stock or cryptocurrency's mean to median ratio is less than 90%.")

        if (rec3+rec2+rec1)>1:
            recommendation = "BUY!"
        else:
            recommendation = "DON'T BUY"



        print("-------------------------")
        print(f"ADVICE REQUESTED AT: {requestdate}")
        print("-------------------------")
        latestdata = dfrecords["date"].values
        print(f"LATEST DATA FROM: {latestdata[0]}")

        print(f"LATEST CLOSE: {to_usd(latestclose[0])}")

        print(f"RECENT HIGH: {to_usd(recenthigh)}")
        print(f"RECENT LOW: {to_usd(recentlow)}")
        print("-------------------------")
        print(f"RECOMMENDATION: {recommendation}")
        print("EXPLANATION: ")
        for reason in explanation:
            print(reason)
        print("-------------------------")
        print("HAPPY INVESTING :)")
        print("")


        #sns.lineplot(data=dfrecords, x="date", y="close")


        moredatavalidation = True
        while moredatavalidation:
            morestocks = input("Do you wish to receive advice on another stock or cryptocurrency? ['yes'/'no']:")
            if morestocks == "no":
                addmore = False
                moredatavalidation = False
                print("Thank you for using the Robo Advisor!")
            elif morestocks == "yes":
                entering = True
                moredatavalidation = False
            elif morestocks != "yes" and morestocks !="no":
                print("Please enter either 'yes' or 'no'.")




#UNCOMMENT THESE BEFORE YOU TURN IN!!!!!!!
    except:
        print("Oops, that stock symbol was not found. Please try again.")
        entering = True
