import requests
from pathlib import Path
import re

api_key="7NJXMGNT452HK20E"
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(data)
data_str = str(data)