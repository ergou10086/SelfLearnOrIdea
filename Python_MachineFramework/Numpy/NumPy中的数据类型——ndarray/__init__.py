# `ndarray` 是 NumPy 中的一个核心数据结构，它代表了一个多维的、同类型元素的数组。与 Python 内建的列表不同
# `ndarray` 可以在数值计算中提供更高效的操作，因为它是用 C 语言实现的，可以在内存中高效地存储和处理数据\

# `ndarray` 中的所有元素都是同一种数据类型（比如整数、浮动数等）

import numpy as np
floats = np.array([0.0, 0.1, 0.2, 0.3, 0.4])
floats #注：Numpy 不会显示浮点数小数点后面尾随的0。


# 多维：ndarray` 可以是多维的数组（比如二维矩阵、三维数组等），这使得它在处理图像、科学计算和数据分析等任务中非常有用。
a = np.array(
[[ 1, 2, 3],
 [ 4, 5, 6]])
a
type(a)


# 大小和形状：ndarray有一个属性 `shape`，它描述了数组每一维的大小。比如一个 3x4 的矩阵，`shape` 会返回 `(3, 4)`。
# ndarray对象的属性：使用`(实例变量名).(属性)`形式的语句可以获取 ndarray 实例中所包含的属性值。
# 确定array元素类型
import numpy as np
a = np.array(
[[ 1, 2, 3],
 [ 4, 5, 6]
 ])

# 确定array的维度
print(a.ndim)
print(a.shape)
# 确定array的元素数量和元素大小
print(a.size)      # 查看array的元素数量
print(a.itemsize)  # 查看存储每个元素需要的字节数


# 创建多维数组
# 创建一个二维数组
# 语法：np.array(object, dtype=None, copy=True, order='K', subok=False, ndmin=0)
# 参数为：object：数组的数据对象
# dtype：数据类型，可选参数，默认为None，表示使用默认的数据类型
# copy：是否复制数据，可选参数，默认为True
# order：内存中数据存储的顺序，可选参数，默认为'K'
# subok：是否返回子类，可选参数，默认为False
# ndmin：返回数组的最小维数，可选参数，默认为0
# 返回值：一个包含传入数据的NumPy数组
import numpy as np
data3 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr1 = np.array(data3)
arr1


# 指定元素填充
import numpy as np
# 语法：np.zeros(shape, dtype=float, order='C')
# 参数为：shape：数组形状
# dtype：数据类型，可选参数，默认为float
# order：内存中数据存储的顺序，可选参数，默认为'C'，表示按行存储

np.zeros(5) # 生成一个一维数组，包含5个元素，每个元素都是0
np.ones((2, 4), dtype=int) # 生成一个2行4列的二维数组，每个元素都是1

#np.empty()不会初始化数组的值也就是说，数组中的数据是随机的，取决于内存中之前存储的数据。因此，np.empty() 的主要特点是速度很快，因为它没有像 np.zeros() 或 np.ones() 那样对数组进行初始化。
np.empty((2, 4)) # 生成一个2行4列的二维数组，每个元素都是随机数

np.full((3, 5), 13) # 生成一个3行5列的二维数组，每个元素都是13

np.ones_like(a)   # 生成一个形状和a相同的数组，但元素都是1



# ndarray--坐标轴和维度
import numpy as np
# 数组 a 的维度（形状）
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)
print(a.shape)
print(a.ndim)  # 维度的数量，相当于 shape 的元素数量

# axis，维度被称为轴。指定坐标轴的方法是将 axis 对应为shape的索引。
# 3*2的矩阵示例
a = np.arange(6).reshape(3, 2)
print(a)
print(a.shape)



# 作为函数参数的axis
# sum 函数，当参数中指定 axis=0 进行加法运算时，程序会对axis=0的箭头方向上的元素进行加法运算。
b = np.array([a, a])
np.sum(b, axis=2)
print(b.sum(axis=1).shape)
print(b)



# 高维度数组切片
# 只需要将各个维度中的切片组合起来，不同维度之间使用逗号进行分隔`[:, :, :]`
b = np.arange(20).reshape(4, 5) # 4×5的二维数组
print(b)
# 将第1~2行，第2~3列提取出来
# 将第0~1行，第1~4列提取出来
print(b[1:3, 2:4])
print(b[2:4, 3:5])