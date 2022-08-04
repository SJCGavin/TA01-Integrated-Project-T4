from asyncio import wait_for
from bdb import effective
from collections import deque
from colorsys import rgb_to_yiq, yiq_to_rgb
from ctypes import wstring_at
from curses import erasechar
from decimal import ROUND_HALF_EVEN
from distutils.util import rfc822_escape
from errno import EEXIST, EPWROFF
from fcntl import F_GETFD
from lib2to3.pgen2 import driver
from lib2to3.pgen2.pgen import DFAState
from locale import ERA_D_FMT
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
from multiprocessing import Event
from multiprocessing.sharedctypes import RawValue
from os import removexattr
from pathlib import Path
import csv
import re
from readline import read_history_file
from socket import EAI_SERVICE, TIPC_CFG_SRV
from socketserver import DatagramRequestHandler
from sys import _enablelegacywindowsfsencoding
from tabnanny import verbose
from tkinter import E, W
from typing import ForwardRef
from urllib.request import FTPHandler
from wave import WAVE_FORMAT_PCM
import weakref
from winreg import REG_NOTIFY_CHANGE_ATTRIBUTES
from wsgiref.util import FileWrapper
from xml.dom.expatbuilder import theDOMImplementation
from xml.sax.handler import feature_external_ges

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

