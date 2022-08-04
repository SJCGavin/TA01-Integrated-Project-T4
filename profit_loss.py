from pathlib import Path
import csv

# Opens pathway to Profit-and-loss-usd.csv file
fp_pnl = Path.cwd()/"csv_reports"/"Profit-and-loss-usd.csv"

def profit_loss_data(forex):
    """
    - This function flags the days and deficit amount of current days with net profit is less than previous day
    - This function then converts the deficit amount from USD to SGD
    - One parameter required: forex (the foreign exchange rate between USD and SGD as integer or float)
    """
    try:

        empty_list_pnl = []
        empty_list_pnl2 = []

        # Opens Profit-and-loss-usd.csv file
        with fp_pnl.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                # Appends only the days and net profit into empty_list_pnl
                stuff = (line[0],line[3])
                empty_list_pnl.append(list(stuff))

        count = 1
        # For loop compares current day data with previous day data
        # Counts the days where the net profit is larger than the previous day
        for k in range(1,len(empty_list_pnl)):
            if float(empty_list_pnl[k][1]) >= float(empty_list_pnl[k-1][1]):
                # For every day that net profit is higher than the previous day, count increases by 1
                count += 1

        # Checks if count is equal to the number of variables in the empty_list_pnl
        if count == len(empty_list_pnl):
            # If true, the function returns this
            return "NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"
        else:
            # If count is not equal to the number of variables in empty_list_pnl, function continues here
            for i in range(1,len(empty_list_pnl)):
                # Compares current day cash to previous day cash
                if float(empty_list_pnl[i][1]) < float(empty_list_pnl[i-1][1]):
                    # Appends days with deficit values into empty list empty_list_pnl2
                    empty_list_pnl2.append(empty_list_pnl[i])
                else:
                    pass
            # Floats data
            for days_and_money in empty_list_pnl2:
                days_and_money[0] = float(days_and_money[0])
                # Converts USD data into SGD
                days_and_money[1] = float(days_and_money[1]) * float(forex)

            # Returns finished data
            return empty_list_pnl2

    # except stops the code from crashing and provides a message for the error
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"