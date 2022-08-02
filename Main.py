# # from api import mean_forex_closing_price
# # from read_file import process_csv_file
# # from write_file import report_deficit
from pathlib import Path
import csv

fp_summarytext = Path.cwd()/"summary_report.txt"
fp_summarytext.touch()
print(fp_summarytext.exists())

# # def main():
# #     avg_cp = mean_forex_closing_price()
# #     days, cash, net_profit, overheads

# from profit_loss import profit_loss_data
# from overheads import overhead
# from cash_on_hand import cashdata

# # # with fp_summarytext.open(mode="w", encoding="UTF-8", newline="") as filetest:
# # #     profit = profit_loss_data
# # #     filetest.write(profit)
# # #     filetest.

# print(profit_loss_data())
# print(overhead)

# empty_list = []
# empty_list.append(profit_loss_data)
# print(empty_list)

import api, cash_on_hand, overheads, profit_loss

def main():

    forex = api
    overheads.overhead(forex)
    cash_on_hand.cashdata(forex)
    profit_loss.profit_loss_data(forex)

print(main())

