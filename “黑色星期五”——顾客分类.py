import pandas as pd
from pandasql import sqldf
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 导入数据
bf = pd.read_csv(r"F:\Python\book1\案例77：“黑色星期五”——顾客分类\数据集\BlackFriday.csv", header = 'infer')
bf.info()

## 2.数据预处理
##处理缺失值
bf.isna().any()

#计算缺失值的比率
missing_percentage = (bf.isnull().sum()/bf.shape[0]*100).sort_values(ascending=False)
missing_percentage = missing_percentage[missing_percentage!=0].round(2)
print(missing_percentage)

#缺失值使用 0 填充
bf.fillna(0,inplace=True)
bf.isna().any().sum()

#查看各数据取值
#type(bf)
def data_type(bf):
    for i in bf.columns:
        print(i,"------>>",bf[i].unique())

data_type(bf)


bf_C = bf.groupby(['City_Category','Age']).count().reset_index('Age')

fig=plt.figure(figsize=(14,8))
ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)
ax1.set_title('A城')
ax2.set_title('B城')
ax3.set_title('C城')

ax1.pie(bf_C.iloc[0:7,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow','gray','pink','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax2.pie(bf_C.iloc[7:14,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow','gray','pink','orange'],autopct='%1.1f%%',pctdistance = 0.7)
ax3.pie(bf_C.iloc[14:23,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow','gray','pink','orange'],autopct='%1.1f%%',pctdistance = 0.7)

ax1.axis('equal')
ax2.axis('equal')
ax3.axis('equal')
ax3.legend(['0-17','18-25','26-35','36-45','46-50','51-55' ,'55+'],loc="best")



plt.figure(figsize=(10,7))
plt.pie(bf_C.iloc[0:7,2],radius=0.5,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow','gray','pink','orange'],autopct='%1.1f%%',pctdistance = 0.5)
plt.pie(bf_C.iloc[7:14,2],radius=0.7,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow','gray','pink','orange'],autopct='%1.1f%%',pctdistance = 0.8)
plt.pie(bf_C.iloc[14:23,2],radius=1,wedgeprops=dict(width=0.3,edgecolor='w'),colors=['cyan','lightskyblue','linen','yellow','gray','pink','orange'],autopct='%1.1f%%',pctdistance = 1.1)
plt.text(0,0.8,"C")
plt.text(0,0.55,"B")
plt.text(0,0.3,"A")
plt.tight_layout()
plt.legend(['0-17','18-25','26-35','36-45','46-50','51-55' ,'55+'],loc="best")
plt.axis('equal')
plt.title('性别和婚姻状况')
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.show()

print('案例77 “黑色星期五”——顾客分类的输出运行结果')
