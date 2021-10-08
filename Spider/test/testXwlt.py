import xlwt


workbook = xlwt.Workbook(encoding="utf-8")
worksheet = workbook.add_sheet('sheet1')
worksheet.write(0,0,'hello') #行和列
workbook.save('student.xls')