import re
exchr = re.findall(pattern = "[0-9].[0-9]+", string = data_str)
print(exchr[0])