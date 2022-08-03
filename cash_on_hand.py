from pathlib import Path
import csv

empty_list_coh = []

fp_coh = Path.cwd()/"TA01-Integrated-Project-T4"/"csv_reports"/"Cash-on-hand-usd.csv"

def cashdata(ap):
    with fp_coh.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            empty_list_coh.append(line)

    count = 0
    for i in range(1, len(empty_list_coh)):
        if empty_list_coh[i][1] < empty_list_coh[i-1][1]:
            empty_list_coh2 = empty_list_coh[i]
        elif empty_list_coh[i][1] > empty_list_coh[i-1][1]:
            count += 1
            if count == len(empty_list_coh) - 1:
                empty_list_coh2 = "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    if empty_list_coh2 == "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
        return "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    else:
        converted_coh = float(empty_list_coh2[1]) * float(ap)
        return converted_coh

