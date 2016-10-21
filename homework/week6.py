
'''
1. 读入  肝气郁结证型系数.xls  数据集，将数据集按照等距、小组等量 两种方式 分别分为5组数据，分别计算5组数据的中位数与标准差

2. 读入BHP1.csv，使用适当的方法填补缺失值

3. 读入BHP2.xlsx，与BHP1数据集合并为BHP数据集

4. 将BHP数据集中的成交量（volume）替换为 high、median、low 三种水平（区间自行定义）



'''
# -*-coding:gbk-*-
from scipy.interpolate import lagrange
import pandas as pd
import numpy as np

#Q1
data = pd.read_excel('d:data/肝气郁结证型系数.xls',skiprows=1,header=None)
cats=pd.cut(data, 5)
for i in range(0,5):
    a=list()
    for j in range(0,len(data)):
        if cats.labels[j]==i:a.append(data[0][j])
    print 'Group',i+1,"'s median is ",np.median(a)
    print 'Group',i+1,"'s std is ",np.std(a)

cats=pd.qcut(data, 5)
for i in range(0,5):
    a=list();
    for j in range(0,len(data)):
        if cats.labels[j]==i:a.append(data[0][j])
    print 'Group',i+1,"'s median is ",np.median(a)
    print 'Group',i+1,"'s std is ",np.std(a)



#Q2
data = pd.read_csv('d:data/BHP1.csv')
#自定义列向量插值函数
#s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
def ployinterp_column(s, n, k=5):
  y = s[list(range(n-k, n)) + list(range(n+1, n+1+k))] #取数
  y = y[y.notnull()] #剔除空值
  return lagrange(y.index, list(y))(n) #插值并返回插值结果

#逐个元素判断是否需要插值
for i in data.columns:
  for j in range(len(data)):
    if (data[i].isnull())[j]: #如果为空即插值。
      data[i][j] = ployinterp_column(data[i], j)


#Q3
data2 = pd.read_excel('d:data/BHP2.xlsx')
data3=pd.merge(data,data2,how='outer')
data3.to_excel('d:data/BHP.xls')


#Q4

for i in range(len(data3)):
        if data3['volume'][i]>5000000: data3['volume'][i]='high'
        elif data3['volume'][i]>3000000:data3['volume'][i]='median'
        elif data3['volume'][i]<=3000000:data3['volume'][i]='low'

data3.to_excel('d:data/BHP.xls')