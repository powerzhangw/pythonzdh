import  xlrd
'''
xls = xlrd.open_workbook("testdata.xlsx")
#sheet =xls.sheets()[0]
#sheet = xls.sheet_by_name("Sheet1")
sheet = xls.sheet_by_index(0)
print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.nrows):
#    print (sheet.row_values(i)[0])
#   print(sheet.row(i)[1].value)
    print(sheet.cell(i,1).value)
'''
import  xlwt
wr=xlwt.Workbook()
sheet = wr.add_sheet("test")
sheet.write(0,0,"test1")
sheet.write(0,1,"test1")
wr.save("tim.xls")

