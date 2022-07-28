from audioop import avg
import requests
from pathlib import Path
import re

api_key="7NJXMGNT452HK20E"
url = 'https://www.alphavantage.co/query?function=FX_WEEKLY&from_symbol=USD&to_symbol=SGD&apikey={api_key}'
r = requests.get(url)
data = r.json()
#print(data)
data_str = str(data)

excravg = re.findall(pattern = "'4. close': '[0-9].[0-9]+'", string = data_str)
excravg_new = str(excravg)
excravg_strip = excravg_new.replace("'4. close': '", "")
excravg_strip_1 = excravg_strip.replace("'", "")
#print(excravg_strip_1)

#empty_list=[]
# for number in excravg_strip_1:
#     empty_list.append(excravg_strip_1)
# sum(empty_list)
# def weekly_mean():
#     """
#     - function to calculate average weekly forex
#     """
#     total = 0 
#     for avg in empty_list:
#         empty_list.append(data)
#         total += avg / len(empty_list)
#         return (total)
    # return (f"Aveage weekly forex':{total}")
# print (weekly_mean)
turnlist = list(excravg_strip_1.split(" "))
#print(turnlist)

