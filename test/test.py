import pandas as pd

data=pd.read_excel('tsp48.xls',header=None)

for i in range(0,48):
    for j in range (i,48):
       data[i][j]=data[j][i]

for i in range(0,48):
    data[i][i]=100000

data.to_csv('out48.csv')
