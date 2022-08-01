# import re
# exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
# print(exchr[0])





# listy = []
# fp1 = Path.cwd()/"csv_reports"/"Overheads-day-45.csv"
# def overheady():
#     with fp1.open(mode="r", encoding="UTF-8", newline="") as file:
#         reader = csv.reader(file)
#         next(reader)
#         for line in reader:
#             lines = float(line[1])
#             listy.append(lines)
#         listy.sort()
#         print(listy[-1])
# print(overheady())
        
fp = Path.cwd()/"csv_reports"/"Cash-on-hand-usd.csv"
def cashdata():
    with fp.open(mode="r", encoding="UTF-8", newline="") as file:
        reader = csv.reader(file)
        next(reader)
        '''
        Opens file to read data
        '''
        days = 0
        cash = 0
        '''
        
        '''
        data = []
        for line in reader:
            if days == 0:
                days = float(line[0]) + 1
                cash = float(line[1])
            elif days < float(line[0]) + 1:
                if cash > float(line[1]):
                    return line
            elif days > float(line[0]) + 1:
                if cash < float(line[0]):
                    data.append(line)
