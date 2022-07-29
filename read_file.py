# import re
# exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
# print(exchr[0])


from pathlib import Path
import csv
import re
fp = Path.cwd()/"TA01-Integrated-Project-T4"/"csv_reports"/"Cash-on-hand-usd.csv"
empty_list = []
with fp.open (mode="r", encoding = "UTF-8", newline="") as file1:
    reader= csv.reader(file1)
    next(reader)
    for line in reader:
        empty_list.append(line)
for list in empty_list:
    print(list[1])
    # for line in reader:
    #     print(line)

    
