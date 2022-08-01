from pathlib import Path
import csv
empty_list_pnl = []
fp_pnl = Path.cwd()/"TA01-Integrated-Project-T4"/"csv_reports"/"Profit-and-loss-usd.csv"
with fp_pnl.open (mode="r", encoding = "UTF-8", newline="") as file1:
    reader = csv.reader(file1)
    next(reader)
    for line in reader:
        empty_list_pnl.append(line)
        profit_loss = (line[0],line[3])
        empty_list_pnl.append(profit_loss)

def profit_loss_data():
    days = 0
    cash=0
    data = []
    for line in empty_list_pnl:
        if days == 0:
            days = float(line[0]) + 1
            cash = float(line[1])
        elif days < float(line[0]) + 1:
            if cash > float(line[1]):
                return line
        elif days > float(line[0]) + 1:
            if cash < float(line[1]):
                return line
        elif days < float(line[0]) + 1:
            if cash > float(line[1]):
                return "Net profit on each period is higher than the previous period"
print(profit_loss_data())