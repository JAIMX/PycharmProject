'''
对macrodata.csv数据集

1. 画出realgdp列的直方图

2. 画出realgdp列与realcons列的散点图，初步判断两个变量之间的关系




对tips数据集

3. 画出不同sex与day的交叉表的柱形图

4. 画出size的饼图




'''

# -*-coding:gbk-*-
import matplotlib.pyplot as plt
import pandas as pd

#Q1
data = pd.read_csv('d:/python/IDE/workspace/test/data/macrodata.csv')
x=list()
y=list()

for i in range(0,200,4):
    x.append(data['year'][i])
    y.append(data['realgdp'][i]+data['realgdp'][i+1]+data['realgdp'][i+2]+data['realgdp'][i+3])

x.append(data['year'][200])
y.append(data['realgdp'][200]+data['realgdp'][201]+data['realgdp'][202])

plt.subplot(121)
plt.bar(x,y,color='k')
plt.subplot(122)
plt.title('Relationship of realgdp and realcons')
plt.xlabel('realgdp')
plt.ylabel('realcons')
plt.scatter(data['realgdp'],data['realcons'],color='k',marker='.')

plt.show()

# 可以初步判断两变量之间呈正线性相关关系

#Q2
tips = pd.read_csv('d:/python/IDE/workspace/test/data/tips.csv')

party_counts = pd.crosstab(tips.day, tips.sex)
party_counts.plot(kind='bar', stacked=True)
plt.show()

a=list(tips['size'])
b=list()
for i in range(1,7):
   b.append(a.count(i))

plt.figure(1,figsize=(8,8))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])
labels = 'one', 'two', 'three', 'four','five','six'
explode =[0.1,0.1,0.1,0.1,0.1,0.1]

plt.pie(b, labels=labels,explode=explode,autopct='%1.1f%%', startangle=67)

plt.title("Customers'size")

plt.show()