import requests

def api_exchange():

    try:

        api_key="7NJXMGNT452HK20E"
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}'
        r = requests.get(url)
        data = r.json()
        avg = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        return round(float(avg), 5 )

    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"

print(api_exchange())

gfh