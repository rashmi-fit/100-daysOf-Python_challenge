'''The objective is to read, and parse a given Excel file, using the “xlrd” module. 
Note:- If you are using Python3 then use xlrd==1.2.0'''
import xlrd
import os

location= "https://github.com/rashmi-fit/100-daysOf-Python_challenge/blob/main/PythonTest/ToParse_Python.xlsx"
open_workbook = xlrd.open_workbook(location)

sheet = open_workbook.sheet_by_index(0)
 
# For row 0 and column 0
sheet.cell_value(0, 0)
 
for i in range(sheet.ncols):
    print(sheet.cell_value(0, i))