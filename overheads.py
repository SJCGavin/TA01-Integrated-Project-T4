from pathlib import Path
import csv

# Opens pathway to Overheads-day-45.csv file
fp_overhead = Path.cwd()/"csv_reports"/"Overheads-day-45.csv"

def overhead(forex):
    """
    - This function finds the highest overhead expense
    - This function then converts the data from USD to SGD
    - One parameter required: forex (the foreign exchange rate between USD and SGD as integer or float)
    """
    try:
        empty_list_overhead = []
        # Opens Overheads-day-45.csv file
        with fp_overhead.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                # Floats the data in the file
                lines = float(line[1])
                # Appends floated data into empty_list_overhead
                empty_list_overhead.append(lines)
                # Sorts the the data in ascending order
                empty_list_overhead.sort()
                # Moves the largest overhead expense into variable highest_overhead
                highest_overhead = empty_list_overhead[-1]

                # Converts the highest overhead from USD to SGD
                converted_overhead = float(highest_overhead) * float(forex)
                # Returns converted_head with the name of it's expense
                return line[0], round(converted_overhead, 1)
                
    # except stops the code from crashing and provides a message for the error
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"