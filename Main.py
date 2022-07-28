from pathlib import Path
import csv
import re

fp = Path.cwd()
print(fp.exists())
fp_txt = Path.cwd()/(r"deficit_report.txt")
fp_txt.touch()
print(fp_txt.exists())

exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
print(exchr[0])

