from audioop import avg
import requests
from pathlib import Path
import re

api_key="7NJXMGNT452HK20E"
url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=demo{api_key}'
r = requests.get(url)
data = r.json()
# print(data)
data_str = str(data)
# print(data_str)
print(data)
avg = data["Realtime Currency Exchange Rate"]["5. Exchange Rate"]

print(f"1 USD = {avg} SGD")


def data():
    """
    """
    for num in data:
        print(data["Realtime Currency Exchange Rate"]["5. Exchange Rate"])






# def data():
#     """
#     """
#     empty_list= {}
#     total = 0
#     empty_list_1 = empty_list.keys()
#     for items in empty_list_1:
#         total += data["Exchange Rate"]
#         return (total)
#     print(total)
# # print(data())





    
# all = re.findall(pattern = "'4. close': '[0-9].[0-9]+'", string = data_str)
# all = str(all)
# all_1 = all.replace("'4. close': '", "")
# all_2 = all_1.replace("'", "")
# print(all_2)


# print(float(all_2))

# empty_list=[]
# for num in range(0, len(data_str)):
#     data_str[num] = float(data_str[num])
#     print(data_str)







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
# turnlist = list(excravg_strip_1.split(" "))
# # print(turnlist)

# print(float(turnlist))
# print(type(turnlist[0]))
# print([float(num) for num in turnlist])