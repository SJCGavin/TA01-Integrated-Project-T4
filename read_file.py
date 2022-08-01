# import re
# exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
# print(exchr[0])


from pathlib import Path
import csv
fp = Path.cwd()/"csv_reports"/"Profit-and-loss-usd.csv"
empty_list = []
with fp.open (mode="r", encoding = "UTF-8", newline="") as file1:
    reader= csv.reader(file1)
    next(reader)
    for line in reader:
        empty_list.append(line)
        print(line[0],line[3])

        
# for list in empty_list:
#     print(list)
