from pathlib import Path
import csv

empty_list_overhead = []
fp1 = Path.cwd()/"csv_reports"/"Overheads-day-45.csv"

def overhead():
    with fp1.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            lines = float(line[1])
            empty_list_overhead.append(lines)
            empty_list_overhead.sort()
            return empty_list_overhead[-1]
            
print(overhead())