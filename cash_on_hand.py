from pathlib import Path
import csv

fp = Path.cwd()/"TA01-Integrated-Project-T4"/"csv_reports"/"Cash-on-hand-usd.csv"
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
print(cashdata())