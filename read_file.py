# import re
# exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
# print(exchr[0])


from pathlib import Path
import csv
# empty_list = []
# fp = Path.cwd()/"csv_reports"/"Profit-and-loss-usd.csv"
# list = []
# with fp.open (mode="r", encoding = "UTF-8", newline="") as file1:
#     reader = csv.reader(file1)
#     next(reader)
#     for line in reader:
#         empty_list.append(line)
#         profit_loss = (line[0],line[3])
#         list.append(profit_loss)

# def profit_loss_data():
#     days = 0
#     cash=0
#     data = []
#     for line in list:
#         if days == 0:
#             days = float(line[0]) + 1
#             cash = float(line[1])
#         elif days < float(line[0]) + 1:
#             if cash > float(line[1]):
#                     return line
#         elif days > float(line[0]) + 1:
#             if cash < float(line[1]):
#                 data.append(line)
#         elif days < float(line[0]) + 1:
#             if cash > float(line[1]):
#                 return "Net profit on each period is higher than the previous period"
# print(profit_loss_data())


# listy = []
# fp1 = Path.cwd()/"csv_reports"/"Overheads-day-45.csv"
# def overheady():
#     with fp1.open(mode="r", encoding="UTF-8", newline="") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for line in reader:
#             lines = float(line[1])
#             listy.append(lines)
#         listy.sort()
#         print(listy[-1])
# print(overheady())
        
fp = Path.cwd()/"csv_reports"/"Cash-on-hand-usd.csv"
def cashdata():
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        '''
        Opens file to read data
        '''
        days = 0
        cash = 0
        '''
        
        '''
        data = []
        for line in reader:
            if days == 0:
                days = float(line[0]) + 1
                cash = float(line[1])
            elif days < float(line[0]) + 1:
                if cash > float(line[1]):
                    return line
            elif days > float(line[0]) + 1:
                if cash < float(line[0]):
                    data.append(line)
