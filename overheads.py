from bdb import effective
from curses import erasechar
from decimal import ROUND_HALF_EVEN
from distutils.util import rfc822_escape
from errno import EEXIST
from multiprocessing import Event
from multiprocessing.sharedctypes import RawValue
from pathlib import Path
import csv
import re
from socket import EAI_SERVICE
from tabnanny import verbose
from tkinter import E

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
