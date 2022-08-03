from pathlib import Path
import csv

def profit_loss_data(forex):
    empty_list_pnl = []
    empty_list_pnl2 = []
    fp_pnl = Path.cwd()/"TA01-Integrated-Project-T4"/"csv_reports"/"Profit-and-loss-usd.csv"
    with fp_pnl.open (mode="r", encoding = "UTF-8", newline="") as file1:
        reader = csv.reader(file1)
        next(reader)
        for line in reader:
            empty_list_pnl.append(line)
            profit_loss = (line[0],line[3])
            empty_list_pnl2.append(profit_loss)
    # print(empty_list_pnl2)
    count = 0
    for i in range(1, len(empty_list_pnl2)):
        if empty_list_pnl2[i][1] < empty_list_pnl2[i-1][1]:
            lis2 = empty_list_pnl2[i]
        elif empty_list_pnl2[i][1] > empty_list_pnl2[i-1][1]:
            count += 1
            if count == len(empty_list_pnl2) - 1:
                empty_list_pnl3 = "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    if empty_list_pnl3 == "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
        return "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    else:
        converted_pnl = float(empty_list_pnl2[1]) * float(forex)
        return converted_pnl

print(profit_loss_data(2))
# def profit_loss_data():
#     days = 0
#     cash=0
#     for line in empty_list_pnl:
#         if days == 0:
#             days = float(line[0]) + 1
#             cash = float(line[1])
#         elif days < float(line[0]) + 1:
#             if cash > float(line[1]):
#                 return "Net profit on each period is higher than the previous period"
#         elif days > float(line[0]) + 1:
#             if cash < float(line[1]):
#                 return line
#         elif days < float(line[0]) + 1:
#             if cash > float(line[1]):
#                 return line

# print(profit_loss_data())