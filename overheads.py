from pathlib import Path
import csv

empty_list_overhead = []
fp_overhead = Path.cwd()/"csv_reports"/"Overheads-day-45.csv"

def overhead(forex):
    """
    -
    """

    try:
        with fp_overhead.open(mode="r", encoding="UTF-8", newline="") as file:
            reader = csv.reader(file)
            next(reader)
            for line in reader:
                lines = float(line[1])
                empty_list_overhead.append(lines)
                empty_list_overhead.sort()
                highest_overhead = empty_list_overhead[-1]

                converted_overhead = float(highest_overhead) * float(forex)
                return line[0], round(converted_overhead, 1)
    
    except Exception as e:
        return f"AN ERROR HAS OCCURED. \nREASON: {e}"

        celeste