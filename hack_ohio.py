import collections
import openpyxl
import re

compare1 = 2;
compare2 = 5;
compare_amount = 40;

wb = openpyxl.load_workbook('officialRemovedFillerX.xlsx')
wb.get_sheet_names()
sheet = wb.get_sheet_by_name('Sheet1')

major_computer = {'technology','computer','science','engineer','data','analytics','analytic','analysis','internet','IT','software','programmer','program'}

master_list = collections.namedtuple('Player', 'score name')
d = {'Instantiate':0}

for j in range(1,263):
    words = sheet.cell(row = j, column = 5).value
    words = words.split()
    for each in words:
        each = re.sub('[^0-9a-zA-Z]+', '', each)
        if each != '':
            if each.lower() in d:
                d[each.lower()] += 1
            else:
                d[each.lower()] = 1

ordered_master_list = sorted([master_list(v,k) for (k,v) in d.items()], reverse=True)
for each in range(0,compare_amount):
    print ordered_master_list[each]




###########################################