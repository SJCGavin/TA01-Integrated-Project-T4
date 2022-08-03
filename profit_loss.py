from pathlib import Path
import csv

empty_list_pnl = []
empty_list_pnl2 = []
empty_list_pnl3 = []
fp_pnl = Path.cwd()/"csv_reports"/"Profit-and-loss-usd.csv"

# def profit_loss_data(forex):
#     empty_list_pnl = []
#     empty_list_pnl2 = []
#     fp_pnl = Path.cwd()/"csv_reports"/"Profit-and-loss-usd.csv"
#     with fp_pnl.open (mode="r", encoding = "UTF-8", newline="") as file1:
#         reader = csv.reader(file1)
#         next(reader)
#         for line in reader:
#             empty_list_pnl.append(line)
#             profit_loss = (line[0],line[3])
#             empty_list_pnl2.append(profit_loss)
#     # print(empty_list_pnl2)
#     count = 0
#     for i in range(1, len(empty_list_pnl2)):
#         if empty_list_pnl2[i][1] < empty_list_pnl2[i-1][1]:
#             final_ans_pnl = empty_list_pnl2[i]
#         elif empty_list_pnl2[i][1] > empty_list_pnl2[i-1][1]:
#             count += 1
#             if count == len(empty_list_pnl2) - 1:
#                 final_ans_pnl = "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
#     if final_ans_pnl == "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
#         return "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
#     else:
#         converted_pnl = float(final_ans_pnl[1]) * float(forex)
#         return round(float(final_ans_pnl[0]), 1), round(converted_pnl, 1)

def profit_loss_data(forex):
    with fp_pnl.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            empty_list_pnl.append(line)
            profit_loss = (line[0],line[3])
            empty_list_pnl2.append(list(profit_loss))
        reader_helper = list(empty_list_pnl2)

    count = 1
    for k in range(1,len(reader_helper)):
        if float(reader_helper[k][1]) >= float(reader_helper[k-1][1]):
            count += 1

    if count == len(reader_helper):
        return "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
    else:
        for i in range(1,len(reader_helper)):
            if float(reader_helper[i][1]) < float(reader_helper[i-1][1]):
                empty_list_pnl3.append(reader_helper[i])
            else:
                pass

        for days_and_money in empty_list_pnl3:
            days_and_money[0] = float(days_and_money[0])
            days_and_money[1] = float(days_and_money[1]) * float(forex)

        # for j in range(0,len(empty_list_pnl3)):
        #     empty_list_pnl3[j] = tuple(empty_list_pnl3[j])
        return empty_list_pnl3
print(profit_loss_data(1))