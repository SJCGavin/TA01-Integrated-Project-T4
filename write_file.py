from pathlib import Path
fp = Path.cwd()
print(fp.exists())
fp_txt = Path.cwd()/(r"deficit_report.txt")
fp_txt.touch()
print(fp_txt.exists())