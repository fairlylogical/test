from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import os
import csv
import dateutil.parser


def generate_files():
    _max_offset = float(max_offset.get())
    _min_offset = float(min_offset.get())
    diff_offset = _max_offset - _min_offset
    last_year=ref_date.year
    start_year=last_year - int(years_generate.get());
    for i in range(start_year, last_year):
        date_iter=ref_date.replace(year=i)
        with open("out_test_{}.csv".format(i), 'w', newline='') as fout:
            writer = csv.DictWriter(fout, headers)
            for row in csv_reader:
                row[numerical_header.get()] = str(float(row[numerical_header.get()]) + diff_offset)
                row[date_header.get()]=date_iter.strftime("%d/%m/%Y")
                writer.writerow(row)

def selectNumericalHeader(value):
    print("yyy")

def selectDateHeader(value):
    first_date = '31/12/2020'
    global ref_date
    try:
        ref_date=dateutil.parser.parse(first_date)
        print(ref_date)
    except ValueError:
        ref_date=None
        print("Looks like selected header '{}' isnt date (tried to parse header ' {} ')".format(first_date, value))

def openfile():
    global csv_reader
    global numerical_header
    global debug_str
    global headers
    file = filedialog.askopenfile('r', defaultextension='.csv')
    if file is not None:
        debug_str = 'iii'
        csv_reader = csv.DictReader(file, delimiter=delimiter.get())
        headers = csv_reader.fieldnames
        ttk.Label(frm, text="Template file : {}".format(file.name)).grid(column=2, row=0)
        ttk.Label(frm, text="Numerical header").grid(column=0, row=1)
        opt = OptionMenu(frm, numerical_header, *headers, command=selectNumericalHeader)
        opt.config(bg='black')
        opt.grid(column=1, row=1)

        ttk.Label(frm, text="Min offset").grid(column=0, row=2)
        Entry(frm, textvariable=min_offset).grid(column=1, row=2)

        ttk.Label(frm, text="Max offset").grid(column=0, row=3)
        Entry(frm, textvariable=max_offset).grid(column=1, row=3)

        ttk.Label(frm, text="Date column header").grid(column=0, row=4)
        opt_date = OptionMenu(frm, date_header, *headers, command=selectDateHeader)
        opt_date.config(bg='black')
        opt_date.grid(column=1, row=4)

        ttk.Label(frm, text="Nb of years to generate data for ").grid(column=0, row=5)
        Entry(frm, textvariable=years_generate).grid(column=1, row=5)

        ttk.Button(frm, text="Generate the CSV", command=generate_files).grid(column=0, row=6)


COMMA = ","
SEMICOLON = ";"
DELIMITERS = [COMMA, SEMICOLON]
csv_reader = None
csv_first_row = None
headers = ['']
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
delimiter = StringVar(frm)
delimiter.set(",")
numerical_header = StringVar(frm)
numerical_header.set("mulah")
date_header = StringVar(frm)
date_header.set("Some date")
min_offset = StringVar(frm)
min_offset.set(20)
max_offset = StringVar(frm)
max_offset.set(50)
years_generate = StringVar(frm)
years_generate.set(5)
ref_date=None
ttk.Label(frm, text="Delimiter").grid(column=0, row=0)
opt_delim = OptionMenu(frm, delimiter, *DELIMITERS)
opt_delim.config(bg='black')
opt_delim.grid(column=1, row=0)
debug_str = None
ttk.Button(frm, text="Select template file {} ".format('' if debug_str is None else 'coucou'), command=openfile).grid(column=3, row=0)
root.mainloop()