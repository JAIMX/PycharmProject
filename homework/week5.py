'''
读入课程资源中作业数据的所有数据集


'''

import pandas as pd
import xlrd


result = pd.read_table('d:data/creditcard-dataset.txt', sep=',',index_col=0,
                       names=['1', '2', '3','4','5','6','7','8','9','10','11','12','13','14','15'])
print result


result2=pd.read_csv('d:data/Dress Sales.csv')
print result2


book = xlrd.open_workbook('d:data/ApplianceShipments.xls')
print book.sheet_names()
xls_file=pd.ExcelFile( 'd:data/ApplianceShipments.xls')
table=xls_file.parse('Data',parse_cols=1)
print table
















