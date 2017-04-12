#_*_coding:utf-8_*_
import xlrd
data = xlrd.open_workbook('userdata.xlsx')
sheet = data.sheet_by_index(0)
print sheet.name
print sheet.nrows
print sheet.ncols
for r in range(1,sheet.nrows,1):
    print "net user " + sheet.cell(r,1).value +" " + sheet.cell(r,2).value + " /add /passwordchg:No"
    print "netuser " + sheet.cell(r,1).value + " /pwnexp:y"
    print "mkdir E:\\renshi\\" + sheet.cell(r,1).value