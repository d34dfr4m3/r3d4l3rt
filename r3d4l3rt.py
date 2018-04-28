#!/usr/bin/python3
import sys
import xlsxwriter
# Log Facility
logtype=['alarm',
        'availability',
        'degraded',
        'recovered',
        'sync',
        'usage']
# Xls Stuff
sys.argv[2]=sys.argv[2]+'.xlsx'
workbook = xlsxwriter.Workbook(sys.argv[2])
worksheet = workbook.add_worksheet()
row = 0
col = 0
# Go Go Cows!
F = open(sys.argv[1],'r')
for line in F:
    checklog=line.split()
    print(checklog)
    for i in range(len(checklog)):
        try:
            getindex=logtype.index(checklog[i].lower())
            worksheet.write(row, i, str(checklog[checklog.index(logtype[getindex]):]).strip('[],\''))
            break 
        except Exception as error:
            worksheet.write(row, i, str(checklog[i]))
             
    row+=1
F.close()
workbook.close()
