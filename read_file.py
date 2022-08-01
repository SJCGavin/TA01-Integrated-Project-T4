# import re
# exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
# print(exchr[0])


from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"Profit-and-loss-usd.csv"
empty_list = []
# def peepee():
#     with fp.open (mode="r", encoding = "UTF-8", newline="") as file1:
#         reader = csv.reader(file1)
#         next(reader)
#         '''
#         Opens file to read data
#         '''
#         days = 0
#         cash = 0
#         '''
        
#         '''
#         data = []
#         for line in reader:
#             if days == 0:
#                 days = float(line[0]) + 1
#                 cash = float(line[3])
#             elif days < float(line[0]) + 1:
#                 if cash > float(line[3]):
#                         return line
#             elif days > float(line[0]) + 1:
#                 if cash < float(line[3]):
#                     data.append(line)
#             elif days < float(line[0]) + 1:
#                 if cash > float(line[3]):
#                     return "None"
#             for line in reader:
#                 empty_list.append(line)
#                 poo = (line[0],line[3])
#                 return poo
# print(peepee())
        
# for list in empty_list:
#     print(list)
list = []
with fp.open (mode="r", encoding = "UTF-8", newline="") as file1:
    reader = csv.reader(file1)
    next(reader)
    for line in reader:
        empty_list.append(line)
        profit_loss = (line[0],line[3])
        list.append(profit_loss)
def profit_loss_data():
    days = 0
    cash=0
    data = []
    for line in list:
        if days == 0:
            days = float(line[0]) + 1
            cash = float(line[1])
        elif days < float(line[0]) + 1:
            if cash > float(line[1]):
                    return line
        elif days > float(line[0]) + 1:
            if cash < float(line[1]):
                data.append(line)
        elif days < float(line[0]) + 1:
            if cash > float(line[1]):
                return "None"
print(profit_loss_data())