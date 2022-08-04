from pathlib import Path

fp_summarytext = Path.cwd()/"summary_report.txt"
fp_summarytext.touch()

import api, cash_on_hand, overheads, profit_loss

def main():
    """
    - 
    """
    try:
        coh_value2 = []
        pnl_value2 = []

        forex = api.api_exchange()
        overhead_value = overheads.overhead(forex)
        coh_value = cash_on_hand.cashdata(forex)
        pnl_value = profit_loss.profit_loss_data(forex)

        if pnl_value == "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
            pnl_value2.append(f"\n[PROFIT SURPLUS] {pnl_value}")
        else:
            for i in range(len(pnl_value)):
                pnl_value2.append(f"\n[PROFIT DEFICIT] DAY: {pnl_value[i][0]} AMOUNT: SGD{pnl_value[i][1]}")
        if coh_value == "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY":
            coh_value2.append(f"\n[CASH SURPLUS] {coh_value}")
        else:
            for k in range(len(coh_value)):
                coh_value2.append(f"\n[CASH DEFICIT] DAY: {coh_value[k][0]} AMOUNT: SGD{coh_value[k][1]}")
        first = f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{forex}"
        second = f"\n[HIGHEST OVERHEADS] {overhead_value[0]}: SGD{overhead_value[1]}"
        list = [first, second]
        list.extend(coh_value2)
        list.extend(pnl_value2)
        return list
    
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"
        

print(main())

with fp_summarytext.open(mode="w", encoding="UTF-8", newline="") as file:
    file.writelines(main())





welkrjvaesbieblsebv;oae;oiv