'''
my_data=[['slashdot','USA','yes',18,'None'],


['google','France','yes',23,'Premium'],

['digg','USA','yes',24,'Basic'],

['kiwitobes','France','yes',23,'Basic'],

['google','UK','no',21,'Premium'],

['(direct)','New Zealand','no',12,'None'],

['(direct)','UK','no',21,'Basic'],

['google','USA','no',24,'Premium'],

['slashdot','France','yes',19,'None'],

['digg','USA','no',18,'None'],

['google','UK','no',18,'None'],

['kiwitobes','UK','no',19,'None'],

['digg','New Zealand','yes',12,'Basic'],

['slashdot','UK','no',21,'None'],

['google','UK','yes',18,'Basic'],

['kiwitobes','France','yes',19,'Basic']]


以上为某个网站的用户购买行为信息，第1列为来源网站，第2列为用户所在地区，第3列为是否阅读过FAQ，第4列为浏览网页数，第5列为购买的服务类型（目标变量）。通过构造合适的分类模型，预测用户最终的购买服务类型



'''
# coding: utf-8

# In[59]:

from pandas import DataFrame
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.naive_bayes import BernoulliNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt


# In[60]:

my_data=[['slashdot','USA','yes',18,'None'], 

['google','France','yes',23,'Premium'], 

['digg','USA','yes',24,'Basic'], 

['kiwitobes','France','yes',23,'Basic'], 

['google','UK','no',21,'Premium'], 

['(direct)','New Zealand','no',12,'None'], 

['(direct)','UK','no',21,'Basic'], 

['google','USA','no',24,'Premium'], 

['slashdot','France','yes',19,'None'], 

['digg','USA','no',18,'None'], 

['google','UK','no',18,'None'], 

['kiwitobes','UK','no',19,'None'], 

['digg','New Zealand','yes',12,'Basic'], 

['slashdot','UK','no',21,'None'], 

['google','UK','yes',18,'Basic'], 

['kiwitobes','France','yes',19,'Basic']]




# In[61]:

data=pd.DataFrame(my_data,columns=['from','area','faq','visits','service'])


# In[62]:

# 将文字转化为数字
col_from=pd.Categorical.from_array(data['from']) 
col_area=pd.Categorical.from_array(data['area'])
col_faq=pd.Categorical.from_array(data['faq'])
col_visits=pd.Categorical.from_array(data['visits'])
col_service=pd.Categorical.from_array(data['service'])

data['from']=col_from.codes
data['area']=col_area.codes
data['faq']=col_faq.codes
data['visits']=col_visits.codes
data['service']=col_service.codes


# In[63]:

x=data.iloc[:,:4].as_matrix().astype(int)
y=data.iloc[:,4].as_matrix().astype(int)


# In[64]:

#拆分训练数据与测试数据 
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.6)


# In[65]:

####knn最邻近算法####
#训练KNN分类器 
clf = KNeighborsClassifier(algorithm='kd_tree')
clf.fit(x_train, y_train)


# In[51]:

#测试结果
answer = clf.predict(x_test)
print(x_test)
print(answer)
print(y_test)
print 'KNN分类器模型准确率',(np.mean( answer == y_test))
print classification_report(y_test,answer)


# In[52]:

####贝叶斯分类器####
#训练贝叶斯分类器
clf = BernoulliNB() 
clf.fit(x_train,y_train)


#测试结果
answer = clf.predict(x_test)
print(x_test)
print(answer)
print(y_test)
print(np.mean( answer == y_test))
print(classification_report(y_test, answer, target_names = ['低', '高']))


# In[56]:

####决策树####
from sklearn.tree import DecisionTreeClassifier as DTC
dtc = DTC(criterion='entropy') #建立决策树模型，基于信息熵
dtc.fit(x_train, y_train) #训练模型

#导入相关函数，可视化决策树。
#导出的结果是一个dot文件，需要安装Graphviz才能将它转换为pdf或png等格式。
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO
with open("tree.dot", 'w') as f:
  f = export_graphviz(dtc, out_file = f)


#测试结果
answer = dtc.predict(x_test)
print(x_test)
print(answer)
print(y_test)
print(np.mean( answer == y_test))
print(classification_report(y_test, answer))


# In[58]:

####SVM####
from sklearn.svm import SVC
clf =SVC()
clf.fit(x_train, y_train)  

#测试结果
answer = clf.predict(x_test)
print(x_test)
print(answer)
print(y_test)
print(np.mean( answer == y_test))
print(classification_report(y_test, answer))


# In[ ]:



