from pathlib import Path
import csv

fp_coh = Path.cwd()/"csv_reports"/"Cash-on-hand-usd.csv"

def cashdata(forex):

    try:

        empty_list_coh = []
        reader_helper = []
        with fp_coh.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for stuff in reader:
                reader_helper.append(stuff)
        
        count = 1
        for k in range(1, len(reader_helper)):
            if float(reader_helper[k][1]) >= float(reader_helper[k-1][1]):
                count += 1

        if count == len(reader_helper):
            return "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        else:
            for i in range(1,len(reader_helper)):
                if float(reader_helper[i][1]) < float(reader_helper[i-1][1]):
                    empty_list_coh.append(reader_helper[i])
                else:
                    pass

            for days_and_money in empty_list_coh:
                days_and_money[0] = float(days_and_money[0])
                days_and_money[1] = float(days_and_money[1]) * float(forex)

            return empty_list_coh

    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"