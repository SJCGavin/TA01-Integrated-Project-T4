from pathlib import Path
import csv

# Opens pathway to Cash-on-hand-usd.csv file
fp_coh = Path.cwd()/"csv_reports"/"Cash-on-hand-usd.csv"

def cashdata(forex):
    """
    - This function flags the days and deficit amount of current days with cash is lower than previous day
    - This function then converts the deficit amount from USD to SGD
    - One parameter required: forex (the foreign exchange rate between USD and SGD as integer or float)
    """
    try:

        empty_list_coh = []
        reader_helper = []

        # Opens Cash-on-hand-usd.csv file
        with fp_coh.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for r in reader:
                # Appends data from Cash-on-hand-usd.csv file into empty list reader_helper
                reader_helper.append(r)
        
        count = 1
        # For loop compares current day data with previous day data
        # Counts the days where the cash is larger than the previous day
        for k in range(1, len(reader_helper)):
            if float(reader_helper[k][1]) >= float(reader_helper[k-1][1]):
                # For every day that cash is higher than the previous day, count increases by 1
                count += 1

        # Checks if count is equal to the number of variables in the reader_helper
        if count == len(reader_helper):
            # If true, the function returns this
            return "CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        else:
            # If count is not equal to the number of variables in reader_helper, function continues here
            for i in range(1,len(reader_helper)):
                # Compares current day cash to previous day cash
                if float(reader_helper[i][1]) < float(reader_helper[i-1][1]):
                    # Appends days with deficit values into empty list empty_list_coh
                    empty_list_coh.append(reader_helper[i])
                else:
                    pass
            
            # Floats data
            for days_and_money in empty_list_coh:
                days_and_money[0] = float(days_and_money[0])
                # Converts USD data into SGD
                days_and_money[1] = round(float(days_and_money[1]) * float(forex), 1)

            # Returns finished data
            return empty_list_coh

    # except stops the code from crashing and provides a message for the error
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"