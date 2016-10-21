'''
1. 读入ag0613.csv数据集，并计算数据的最大值、最小值、均值、标准差、中位数

2. 矩阵计算

3. 随机生成100个标准正态的数据，并计算数据的均值与标准差


'''
import numpy as np

#Q1
d=np.loadtxt('ag0613.csv', delimiter=',', skiprows=1,usecols=(0,), unpack=True)

print"max=",np.max(d),"\n","min=",np.min(d),"\n","mean=",np.mean(d),"\n",\
    "std=",np.std(d),"\n","median=",np.median(d)

#Q2
m=np.array([[1,2],[3,4]])
n=np.array([[2,5],[1,3]])
print np.dot(m,n)

#Q3
arr=np.random.randn(100)
print "mean=",np.mean(arr),"\n","std=",np.std(arr)