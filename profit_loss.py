from pathlib import Path
import csv

fp_pnl = Path.cwd()/"csv_reports"/"Profit-and-loss-usd.csv"

def profit_loss_data(forex):
    """
    
    """
    #
    try:
    #
        empty_list_pnl = []
        empty_list_pnl2 = []
    #
        with fp_pnl.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                stuff = (line[0],line[3])
                empty_list_pnl.append(list(stuff))

        count = 1
        for k in range(1,len(empty_list_pnl)):
            if float(empty_list_pnl[k][1]) >= float(empty_list_pnl[k-1][1]):
                count += 1

        if count == len(empty_list_pnl):
            return "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        else:
            for i in range(1,len(empty_list_pnl)):
                if float(empty_list_pnl[i][1]) < float(empty_list_pnl[i-1][1]):
                    empty_list_pnl2.append(empty_list_pnl[i])
                else:
                    pass

            for days_and_money in empty_list_pnl2:
                days_and_money[0] = float(days_and_money[0])
                days_and_money[1] = float(days_and_money[1]) * float(forex)

            return empty_list_pnl2

    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"
