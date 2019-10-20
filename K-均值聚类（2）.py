'''
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


import seaborn as sns; sns.set()

from sklearn.datasets.samples_generator import make_blobs
plt.figure()
X, y = make_blobs(n_samples=300, centers=4,
                  random_state=0, cluster_std=0.60)
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.show()


from sklearn.cluster import KMeans
est = KMeans(4)
est.fit(X)
y_kmeans = est.predict(X)# 逐条判断每个测试图像所属的聚类中心点
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='rainbow')
plt.show()

'''

from sklearn.datasets import load_digits
digits = load_digits()

from sklearn.cluster import KMeans
est = KMeans(n_clusters=10)
clusters = est.fit_predict(digits.data)
print(est.cluster_centers_.shape)

import matplotlib.pyplot as plt
fig = plt.figure(figsize=(8, 3))
for i in range(10):
    ax = fig.add_subplot(2, 5, 1 + i,xticks=[], yticks=[] )
    ax.imshow(est.cluster_centers_[i].reshape((8, 8)), cmap=plt.cm.binary)

plt.show()

