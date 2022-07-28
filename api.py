import requests
from pathlib import Path
import re

api_key="7NJXMGNT452HK20E"
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
print(data)
data_str = str(data)

fp = Path.cwd()
print(fp.exists())
fp_txt = Path.cwd()/(r"deficit_report.txt")
fp_txt.touch()
print(fp_txt.exists())

exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
print(exchr[0])