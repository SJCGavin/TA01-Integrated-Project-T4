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
        overhead_values = []
        # Opens Overheads-day-45.csv file
        with fp_overhead.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for l in reader:
                # Append data from Overheads-day-45.csv file into empty_list_overhead
                empty_list_overhead.append(l)

            for k in range(len(empty_list_overhead)):
                # Floats the values
                empty_list_overhead[k][1] = float(empty_list_overhead[k][1])
                # Append only the values in empty_list_overhead into overhead_values
                overhead_values.append(empty_list_overhead[k][1])

            # Sorts the values in ascending order
            overhead_values.sort()
            # Assigns the largest value to highest_overhead
            highest_overhead = overhead_values[-1]
            # Converts largest value from USD to SGD
            converted_overhead = round(highest_overhead * float(forex), 1)
            
            for h in range(len(empty_list_overhead)):
                # Checks what the index of the highest_overhead is in empty_list_overhead
                if float(empty_list_overhead[h][1]) == highest_overhead:
                    # Assigns the name of the largest value to highest_overhead_name
                    highest_overhead_name =  empty_list_overhead[h][0]
                else:
                    pass
            
            # Returns the largest value with its name
            return highest_overhead_name, converted_overhead
                
    # except stops the code from crashing and provides a message for the error
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"