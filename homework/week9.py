# -*-coding:gbk-*-
import pandas as pd
from pandas import Series, DataFrame
import numpy as np


#若要反驳以下论断，请写出下列论断的零假设与备择假设
#（1） 百事可乐公司声称，其生产的罐装可乐的标准差为0.005磅
#  H0:生产的罐装可乐的标准差为0.005磅    H1:生产的罐装可乐的标准差大于0.005磅
#（2） 某社会调查员说从某项调查得知中国的离婚率高达38.5%
#  H0:中国的离婚率等于38.5%    H1:中国的离婚率小于38.5%
#（3） 某学校招生宣传手册中写道，该学校的学生就业率高达99%
#  H0:该学校的学生就业率等于99%    H1:该学校的学生就业率小于99%

#Q2： 某学生随机抽取了10包一样的糖并称量它们的包装的重量，判断这些糖的包装的平均重量是否为3.5g。
#     其中，这10包糖的重量如下（单位：g）：3.2,3.3,3.0,3.7,3.5,4.0,3.2,4.1,2.9,3.3

from scipy import stats as ss
df=DataFrame({'data':[3.2,3.3,3.0,3.7,3.5,4.0,3.2,4.1,2.9,3.3]})
print ss.ttest_1samp(a = df, popmean = 10)

#Ttest_1sampResult(statistic=array([-51.73285669]), pvalue=array([  1.89237804e-12]))
#可得包装的平均重量不是3.5g

#Q3： 计算Amtrak.xls 数据集的均值、标准差、方差、最大值、最小值、25%分位数、75%分位数、偏度、峰度
xls_file= pd.ExcelFile('d:/python/IDE/workspace/test/data/Amtrak.xls')
table=xls_file.parse('RegData',skiprows=1,header=None)

print table.describe()
print np.var(table)
print table.skew()
print table.kurt()
