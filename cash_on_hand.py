from pathlib import Path
import csv

lis = []

fp_coh = Path.cwd()/"csv_reports"/"Cash-on-hand-usd.csv"

def cashdata(ap):
    with fp_coh.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            lis.append(line)

    count = 0
    for i in range(1, len(lis)):
        if lis[i][1] < lis[i-1][1]:
            lis2 = lis[i]
        elif lis[i][1] > lis[i-1][1]:
            count += 1
            if count == len(lis) - 1:
                print("CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
    ed = float(lis2[1]) * float(ap)
    return ed

# print(cashdata(2))
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