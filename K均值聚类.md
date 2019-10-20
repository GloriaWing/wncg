# Python K均值聚类

Python K均值聚类是一种无监督的机器学习算法，能够实现自动归类的功能。

---

算法步骤如下：

（1）随机产生K个分类中心，一般称为质心。

（2）将所有样本划分到距离最近的质心代表的分类中。（距离可以是欧氏距离、曼哈顿距离、夹角余弦等）

（3）计算分类后的质心，可以用同一类中所有样本的平均属性来代表新的质心。

（4）重复（2）（3）两步，直到满足以下其中一个条件：

```
    1）分类结果没有发生改变。

    2）最小误差（如平方误差）达到所要求的范围。

    3）迭代总数达到设置的最大值。
```

---

常见的K均值聚类算法还有2分K均值聚类算法，其步骤如下：

（1）将所有样本作为一类。

（2）按照传统K均值聚类的方法将样本分为两类。

（3）对以上两类分别再分为两类，且分别计算两种情况下误差，仅保留误差更小的分类；即第（2）步产生的两类其中一类保留，另一类进行再次分类。

（4）重复对已有类别分别进行二分类，同理保留误差最小的分类，直到达到所需要的分类数目。

---

#### 参数的意义：

- n_clusters:簇的个数，即你想聚成几类

- init: 初始簇中心的获取方法

- n_init: 获取初始簇中心的更迭次数，为了弥补初始质心的影响，算法默认会初始10次质心，实现算法，然后返回最好的结果。

- max_iter: 最大迭代次数（因为kmeans算法的实现需要迭代）

- tol: 容忍度，即kmeans运行准则收敛的条件

- precompute_distances：是否需要提前计算距离，这个参数会在空间和时间之间做权衡，如果是True 会把整个距离矩阵都放到内存中，auto 会默认在数据样本大于featurs*samples 的数量大于12e6 的时候False,False 时核心实现的方法是利用Cpython 来实现的

- verbose: 冗长模式

- random_state: 随机生成簇中心的状态条件。

- copy_x: 对是否修改数据的一个标记，如果True，即复制了就不会修改数据。bool 在scikit-learn 很多接口中都会有这个参数的，就是是否对输入数据继续copy 操作，以便不修改用户的输入数据。这个要理解Python 的内存机制才会比较清楚。

- n_jobs: 并行设置

- algorithm: kmeans的实现算法，有：‘auto’, ‘full’, ‘elkan’, 其中 'full’表示用EM方式实现

---

### Methods

- fit(X\[,y\]): 

　   计算k-means聚类。 

- fit_predictt(X\[,y\]):

　   计算簇质心并给每个样本预测类别。 

- fit_transform(X\[,y\])：

  计算簇并 transform X to cluster-distance space。

- get_params(\[deep\])： 

　   取得估计器的参数。 

- predict(X):

　   给每个样本估计最接近的簇。 

- score(X\[,y\]): 

　  计算聚类误差 

- set_params(**params): 

　为这个估计器手动设定参数。 

- transform(X\[,y\]): 将X转换为群集距离空间。

---

### sklearn

- 自带的小数据集（packaged dataset）：sklearn.datasets.load_<name>

```undefined
              load_digits()：用于多分类任务的数据集
```

- 可在线下载的数据集（Downloaded Dataset）：sklearn.datasets.fetch_<name>

- 计算机生成的数据集（Generated Dataset）：sklearn.datasets.make_<name>

- svmlight/libsvm格式的数据集:sklearn.datasets.load\_svmlight\_file(...)

- 从买了data.org在线下载获取的数据集:sklearn.datasets.fetch_mldata(...)

---

### sklearn 中 make_blobs模块使用

- **n_samples**: 待生成的样本的总数。

- **n_features**:  每个样本的特征数。

- **centers**:  要生成的样本中心（类别）数，或者是确定的中心点。

- **cluster_std**:  每个类别的方差。例如我们希望生成2类数据，其中一类比另一类具有更大的方差，可以将cluster_std设置为\[1.0,3.0\]。

- **random_state**: 随机状态实例或无，可选（默认为无）。如果是int，则random\_state是随机数生成器使用的种子；如果是random state实例，则random\_state是随机数生成器；如果不是，则random数生成器是np.random使用的随机状态实例。

---

### matplotlib

- fig.add_subplot(1, 1, 1)：第一个参数子图总列数，第二个参数子图总行数，第三个参数子图位置。

- cmp：colormap，可以理解为接受一个数值，输出一个指定的颜色的字典。下面这张图就展示了常见的一些cmap。

---
