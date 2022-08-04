import requests

def api_exchange():
    """
    - This function finds and returns the foreign exchange rate between USD and SGD based on real time
    - No parameters required
    """
    try:
        # The api_key allows access to vanatge.api for the currency exchange
        api_key="7NJXMGNT452HK20E"

        # The url is to the currency exchange
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}'

        # r gets the information from the currency exchange
        r = requests.get(url)

        # Used to read and wriyes it as a string in data
        data = r.json()

        # avg is the foreign exchange rate between USD and SGD read from data
        avg = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

        # returns the data as a decimel rounded to 5 decimel place
        return round(float(avg), 5 )

    # except stops the code from crashing and provides a message for the error
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"