
# coding: utf-8

# In[67]:
from __future__ import division
import pandas as pd
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



# In[68]:

data=pd.read_csv('ex14.csv',header=0,index_col=0,encoding='gb18030')


# In[69]:

# 查看图形
fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.scatter(data['DXBZ'],data['CZBZ'],data['WMBZ'],marker='o')
ax3D.set_xlabel('DXBZ')
ax3D.set_ylabel('CZBZ')
ax3D.set_zlabel('WMBZ')
plt.show()


# In[70]:

# cluster
for linkage in ('ward', 'average', 'complete'):
    clustering = AgglomerativeClustering(linkage=linkage, n_clusters=3)
    clustering.fit(data)
    cluster_pred = clustering.fit_predict(data)
    print 'clusters :',cluster_pred
    data[u'类型']=cluster_pred
    print data
    fig = plt.figure()
    ax3D = fig.add_subplot(111, projection='3d')
    ax3D.scatter(data['DXBZ'],data['CZBZ'],data['WMBZ'],c=cluster_pred,marker='o')
    ax3D.set_xlabel('DXBZ')
    ax3D.set_ylabel('CZBZ')
    ax3D.set_zlabel('WMBZ')
    plt.show()
    print data.groupby([u'类型']).mean()


# In[71]:

# kmeans

kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
kmeans_pred = kmeans.fit_predict(data)
print 'kmeans cluster:',kmeans_pred
data[u'类型']=kmeans_pred
print data
fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.scatter(data['DXBZ'],data['CZBZ'],data['WMBZ'],c=kmeans_pred,marker='o')
ax3D.set_xlabel('DXBZ')
ax3D.set_ylabel('CZBZ')
ax3D.set_zlabel('WMBZ')
plt.show()
print data.groupby([u'类型']).mean()


# In[72]:

# DBSCAN
db = DBSCAN(eps=2.2, min_samples=3)
db.fit(data)
db_pred=db.fit_predict(data)
data[u'类型']=db_pred
print data
print 'clster 1:',len(db_pred[db_pred==1])/len(db_pred)
print 'clster 0:',len(db_pred[db_pred==0])/len(db_pred)
print 'clster -1:',len(db_pred[db_pred==-1])/len(db_pred)
db_pred[db_pred==1] = 3
db_pred[db_pred==0] = 2
db_pred[db_pred==-1] = 1
fig = plt.figure()
ax3D = fig.add_subplot(111, projection='3d')
ax3D.scatter(data['DXBZ'],data['CZBZ'],data['WMBZ'],c=db_pred,marker='o')
ax3D.set_xlabel('DXBZ')
ax3D.set_ylabel('CZBZ')
ax3D.set_zlabel('WMBZ')
plt.show()
print data.groupby([u'类型']).mean()





