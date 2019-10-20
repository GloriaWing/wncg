# Numpy学习笔记

## 1.np.random.randn

### 利用Numpy产生随机数。

#### 如：

```python
import numpy as np
import random
list2=np.random.randn(2,3)

结果为随机生成一个2行3列的数组
```

## 2.生成的每一个数组都有着一个shape属性和dtype属性，shape属性表示此数组的每一维度的数量，dtype属性用来表示数组的数据类型。

#### 如：

```python
import numpy as np
import random
list2=np.random.randn(2,3)
print(list2.shape)
print(list2.dtype)


输出结果为：(2, 3)
          float64  
  说明随机生成的数组为一个2行3列的数组，它的数据类型为float64。
```

## 3.np.array(list)函数

### 作用：接收任意的数组，生成一个能够进行数据传递的新Numpy数组。

如：

```python
import numpy as np
import random
list1=[1,2,3,4,5,6]
list2=np.array(list1)
list2

结果为输出一个数据为list1中的数据的新的Numpy数组
```

## 4.np.zeros()可创建全零数组，np.ones()可创建全一数组。

## 5.np.arange(x)相当于python自带的range(x)的数组版本。

## 6.使用list.astype(np.xxx)可更改数组的数据类型(xxx为将要更改的数据类型)

#### 如：

```python
更改前：                                              更改后：
import numpy as np                                   import numpy as np                       import random                                        import random
list1=[1,2,3,4,5,6]                                  list1=[1,2,3,4,5,6]
list2=np.array(list1)                                list2=np.array(list1)                     list2.dytpe                                          list3=list2.astype(np.foalt64)       

结果为：dtype('int32')                                 结果为：dtype('float64')
```

注意：若把浮点数转换为整数，则直接去掉小数点后的数。

## 7.Numpy数组的运算

### 1)带有标量的算术操作，会把计算参数传递给数组的每一个元素。

#### 如：

```python
import numpy as np
import random
list2=np.random.randn(2,3)
list2*10

结果为输出一个随机生成的数组的数据全部乘以10的新数组
```

### 2)同尺寸数组比较，会产生一个布尔值数组。

#### 如：

```python
import numpy as np
list1=np.array([1,2,3,4,5,6])
list2=np.array([7,8,9,0,11,12])
list1>list2


结果为:array([False, False, False,  True, False, False])
```

## 8.数组的切片

### 将数组中的指定位置中数据替换掉

#### 如：

```python
import numpy as np
list1=np.array([1,2,3,4,5,6])
list1[1:3]=12
list1


输出结果为：array([ 1, 12, 12,  4,  5,  6])
```
