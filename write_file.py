from pathlib import Path
from winreg import HKEY_LOCAL_MACHINE
fp = Path.cwd()
print(fp.exists())
fp_txt = Path.cwd()/(r"deficit_report.txt")
fp_txt.touch()
print(fp_txt.exists())
print("hello")