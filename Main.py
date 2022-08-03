# # from api import mean_forex_closing_price
# # from read_file import process_csv_file
# # from write_file import report_deficit
from pathlib import Path
import csv

fp_summarytext = Path.cwd()/"summary_report.txt"
fp_summarytext.touch()
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

    forex = api.api_exchange()
    overhead_value = overheads.overhead(forex)
    coh_value = cash_on_hand.cashdata(forex)
    pnl_value = profit_loss.profit_loss_data(forex)
    if pnl_value == "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
        pnl_value2 = f"[PROFIT SURPLUS] {pnl_value}"
    else:
        pnl_value2 = f"[PROFIT DEFICIT] DAY: {pnl_value[0]} AMOUNT: SGD{pnl_value[1]}"
    if coh_value == "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
        coh_value2 = f"[CASH SURPLUS] {coh_value}"
    else:
        coh_value2 = f"[CASH DEFICIT] DAY: {coh_value[0]} AMOUNT: SGD{coh_value[1]}"
    return f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}\n[HIGHEST OVERHEADS] {overhead_value[0]}: SGD{overhead_value[1]}\n{coh_value2}\n{pnl_value2}"
    


print(main())

with fp_summarytext.open(mode="w", encoding="UTF-8", newline="") as file:
    file.write(main())