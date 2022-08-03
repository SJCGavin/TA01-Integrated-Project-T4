from pathlib import Path
import csv

empty_list_coh = []
lis = []

fp_coh = Path.cwd()/"csv_reports"/"Cash-on-hand-usd.csv"

def cashdata(forex):
    with fp_coh.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            empty_list_coh.append(line)

    count = 0
    for i in range(1, len(empty_list_coh)):
        if empty_list_coh[i][1] < empty_list_coh[i-1][1]:
            empty_list_coh2 = (empty_list_coh[i])
        elif empty_list_coh[i][1] > empty_list_coh[i-1][1]:
            count += 1
            if count == len(empty_list_coh):
                empty_list_coh2 = "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    if empty_list_coh2 == "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
        return "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    else:
        converted_coh = float(empty_list_coh2[1]) * float(forex)
        return round(float(empty_list_coh2[0]), 1), round(converted_coh, 1)