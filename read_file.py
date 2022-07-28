# import re
# exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
# print(exchr[0])

def api():
    from pathlib import Path
    import csv
    import re
    fp = Path.cwd()
    for file in fp.glob("*.csv"):
        with file.open (mode="r", encoding = "UTF-8") as file:
            text = file.read()
        print (text)
