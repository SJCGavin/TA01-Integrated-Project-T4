import requests

# api_key="7NJXMGNT452HK20E"
# url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}'
# r = requests.get(url)
# data = r.json()
# data_str = str(data)
# avg = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

# print(f"1 USD = {avg} SGD")

def api_exchange():
    api_key="7NJXMGNT452HK20E"
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}'
    r = requests.get(url)
    data = r.json()
    avg = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    return avg

print(api_exchange())