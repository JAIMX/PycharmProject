'''
1. ����ag0613.csv���ݼ������������ݵ����ֵ����Сֵ����ֵ����׼���λ��

2. �������

3. �������100����׼��̬�����ݣ����������ݵľ�ֵ���׼��


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