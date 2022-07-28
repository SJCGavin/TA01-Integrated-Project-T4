# import re
# exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
# print(exchr[0])


from pathlib import Path
import csv
import re
fp = Path.cwd()/"csv_reports"/"Cash-on-hand-usd.csv"
with fp.open (mode="r", encoding = "UTF-8", newline="") as file1:
    reader= csv.reader(file1)
    for line in reader:
        print(line)
