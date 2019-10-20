from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import GridSearchCV
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset_url = "http://mlr.cs.umass.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
data = pd.read_csv(dataset_url, sep=';')

print(data.head())
print()
print(data.shape)
print()
print(data.describe())
print()

colormap = plt.cm.viridis
plt.figure(figsize=(12,12))
plt.title('Correlation of Features', y=1.05, size=15)
sns.heatmap(data.astype(float).corr(),linewidths=0.1,vmax=1.0, square=True,
            linecolor='white', annot=True)
plt.show()


y = data.quality                  # set 'quality' as target
x = data.drop('quality', axis=1)  # rest are features
print(y.shape, x.shape)           # check correctness
y1 = (y > 5).astype(int)

seed = 8 # set seed for reproducibility
x_train, x_test, y_train, y_test = train_test_split(x, y1, test_size=0.2,
                                                    random_state=seed)
print()
print(x_train.shape, x_test.shape, y_train.shape, y_test.shape)

RF= RandomForestClassifier(random_state=seed)

values = {'n_estimators':[50,100,200],'max_depth':[None,30,15,5],
               'max_features':['auto','sqrt','log2'],'min_samples_leaf':[1,20,50,100]}
RF = GridSearchCV(RF,param_grid=values,scoring='accuracy')
print()
print(RF)
print()

RF = RandomForestClassifier(n_estimators=100,random_state=seed)
RF.fit(x_train,y_train)
RF = RF.predict(x_test)
print('案例67：葡萄酒评分的输出运行结果')
print(accuracy_score(y_test,RF))
print(log_loss(y_test,RF))