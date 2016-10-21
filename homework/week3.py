
'''
1. 创建一个2*2的数组，计算对角线上元素的和

2. 创建一个长度为9的一维数据，数组元素0到8。将它重新变为3*3的二维数组

3. 创建两个3*3的数组，分别将它们合并为3*6、6*3的数组后，拆分为3个数组（维数不限定）

4. 说说numpy数组的优点

'''
import numpy as np

# Q1
a=np.array([[1,2],[3,4]])

print a ,"\n" ,a[0,0]+a[1,1],"\n"


# Q2
b=np.arange(9)
print b
b.shape=(3,3)
print b,"\n"


# Q3
m=np.arange(9).reshape(3,3)
n=np.arange(9).reshape(3,3)
print m
print n,"\n"

c=np.hstack((m,n))
d=np.vstack((m,n))
print c
print d,"\n"

print np.hsplit(c,3)
print np.vsplit(d,3)


"""
Q4: numpy数组的优点

    NumPy数组在数值运算方面的效率优于Python提供的list容器。
    使用NumPy可以在代码中省去很多循环语句，因此其代码比等价的Python代码更为简洁。

"""