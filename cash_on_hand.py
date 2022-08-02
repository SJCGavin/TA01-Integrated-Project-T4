from pathlib import Path
import csv

lis = []

fp_coh = Path.cwd()/"TA01-Integrated-Project-T4"/"csv_reports"/"Cash-on-hand-usd.csv"

with fp_coh.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader)
    for line in reader:
        lis.append(line)
for i in range(1, len(lis)-1):
    if lis[i][1] < lis[i-1][1]:
        print(lis[i])



#         '''
#         Opens file to read data
#         '''
#         days = 0
#         cash = 0
#         '''
        
#         '''
#         empty_list_coh = []
#         for line in reader:
#             if days == 0:
#                 days = float(line[0]) + 1
#                 cash = float(line[1])
#             elif days < float(line[0]) + 1:
#                 if cash > float(line[1]):
#                     return line
#             elif days > float(line[0]) + 1:
#                 if cash < float(line[0]):
#                     empty_list_coh.append(line)
# print(cashdata())