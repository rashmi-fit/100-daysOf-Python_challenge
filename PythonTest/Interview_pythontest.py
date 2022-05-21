'''The objective is to read, and parse a given Excel file, using the “xlrd” module. 
Note:- If you are using Python3 then use xlrd==1.2.0'''
import xlrd
import json
# import excel2json
from xlrd import open_workbook

location= "ToParse_Python .xlsx"
open_workbook = xlrd.open_workbook(location)
# print (open_workbook.nsheets)
# print (open_workbook.sheet_names())
sheet = open_workbook.sheet_by_index(0)

#  read all the data from the xcel sheet as it is
# for i in range(sheet.nrows):
#     row = sheet.row_values(i)       
#     for cell in row:
#         print(cell)

# ''' The result should be nicely printed as a Dict (JSON)'''

for s in open_workbook.sheets():
    #print 'Sheet:',s.name
    values = []
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
# print(values)
print(json.dumps(values))

data = []
keys = ['Quote Number', 'Ship To', 'Date','Name','LineNumber','PartNumber','Description','Item Type','Price']
teams = []

for row_number in range(sheet.nrows):
    if row_number == 0:
        continue
    row_data = {}
    empty = False

    team = {}
    list = sheet.row(0)

    for col_number, cell in enumerate(sheet.row(row)):

        if col_number == 0 and cell.value == '':
                empty = True
        elif col_number == 0:
            empty = False
            teams.clear()

        if col_number == 1 and ( empty is True or cell.value != '(All)'):
            team[keys[0]] = sheet.row(row)

            teams.append(cell.value)
            print(teams)
        elif col_number == 1 and cell.value == '(All)':
            continue

            # skip the number of rows since it does not have to be in JSON file
        if (col_number == 3):
                continue

        if col_number == 1:
            if teams.__len__() > 0:
                    row_data[keys[col_number]] = teams
        elif col_number == 0 and cell.value == '':
            continue
        else:
            row_data[keys[col_number]] = cell.value

        if 'title' in row_data:
            data.append(row_data)

print(json.dumps(data))