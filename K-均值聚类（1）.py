'''
import numpy as np
from sklearn.cluster import KMeans
data = np.random.rand(100, 3) #生成一个随机数据，样本大小为100, 特征数为3

#假如我要构造一个聚类数为3的聚类器
estimator = KMeans(n_clusters=3)#构造聚类器
estimator.fit(data)#聚类
label_pred = estimator.labels_ #获取聚类标签
centroids = estimator.cluster_centers_ #获取聚类中心
inertia = estimator.inertia_ # 获取聚类准则的总和

'''
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics




# 1 准备数据
digits_train = pd.read_csv("F:\Python\k\optdigits.tra", header=None)
digits_test = pd.read_csv("F:\Python\k\optdigits.tes", header=None)
# 从样本中抽取出64维度像素特征和1维度目标
x_train = digits_train[np.arange(64)]
y_train = digits_train[64]
x_test = digits_test[np.arange(64)]
y_test = digits_test[64]

# 2 建立模型
# 初始化kMeans聚类模型 聚类中心数量为10个
kmeans = KMeans(n_clusters=10)
# 聚类
kmeans.fit(x_train)
# 逐条判断每个测试图像所属的聚类中心你
y_predict = kmeans.predict(x_test)

# 3 模型评估
# 使用ARI进行性能评估 当聚类有所属类别的时候利用ARI进行模型评估
print("k均值聚类的ARI值：", metrics.adjusted_rand_score(y_test, y_predict))



# 如果没有聚类所属类别，利用轮廓系数进行评估


