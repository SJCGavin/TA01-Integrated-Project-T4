from pathlib import Path
from winreg import HKEY_LOCAL_MACHINE

from read_file import cashdata

fp = Path.cwd()
fp_txt = Path.cwd()/(r"deficit_report.txt")
fp_txt.touch()
# print(fp_txt.exists())



print(cashdata())