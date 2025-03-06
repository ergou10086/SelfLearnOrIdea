import numpy as np
x = np.arange(20).reshape(4, 5)   #  4 行 5 列的二维数组。
print(x)
print(x[3])  # 打印第4维
print(x[:4])   # 从数组 x 的开头到第 4 行（不包括第 4 行）的所有行
print(x[2:5:1])    # 从第 3 行（索引为 2）开始，到第 5 行（不包括第 5 行），步长为 1 进行切片
print(x[:-3:1])   # 从数组 x 的开头到倒数第 3 行（不包括倒数第 3 行），步长为 1 进行切片
print(x[1:5:2])   # 从第 2 行（索引为 1）开始，到第 5 行（不包括第 5 行），步长为 2 进行切片，会取到第 2 行和第 4 行。
# 多维的数组每个轴可以有一个索引。这些索引以逗号分隔的元组给出：
print(x[:2, 2:])   # 表示取第 1 行（索引为 0）到第 1行，并且从第 3 列（索引为 2）开始到最后一列的所有元素
print(x[1:3, 1])   # 取第 2 行和第 3 行（索引为 1 和 2）的第 2 列（索引为 1）的元素。
print(x[:,2])


y = np.arange(60).reshape(3, 4, 5)
print(y.shape)
print(y)
print(y[1, ...])   # 访问数组某个维度的全部内容， ...代替多个冒号
print(y[:, :, 1])



# 花式索引
a = np.arange(12)*2
i = np.array([1, 1, 3, 8, 5] )
print(a)
print(i)
print(a[i])
#  j 是一个索引数组，用于从 a 中选择特定的元素，NumPy 根据 j 的形状返回一个新数组，
# 每个元素对应 a 中的索引值
a = np.arange(12)*2
print(a)
# 选择a[3],a[4]组成了二维数组的第一维
j = np.array([[3, 4], [9, 7]])
print(a[j])

# 我们还可以为多个维度提供索引。每个维度的索引数组必须具有相同的形状。
a = np.arange(12).reshape(3,4)
print(a)
i = np.array( [ [0,1],                        # indices for the first dim of a
               [1,2] ] )
j = np.array( [ [2,1],                        # indices for the second dim
               [3,3] ] )
print(a[i, j])




# 用布尔数组进行索引
# 对于数组的每个维度，我们给出一个1D布尔数组，选择我们想要的切片：
import numpy as np
a = np.arange(12).reshape(3,4)
print(a)
b1 = np.array([False,True,True])
b2 = np.array([True,False,True,False])
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(a[b1,:])
# array([[ 4,  5,  6,  7],
#        [ 8,  9, 10, 11]])
print(a[b2])

# 1D布尔数组的长度必须与要切片的尺寸（或轴）的长度一致。
# 或者直接根据布尔运算来找到对应的值
array=np.arange(15)
print(array)
print(array[(array>=5) & (array<=10)])


# ndarray的切片和python中的切片，有一个重要的区别
# numpy 中，数组切片是原始数组的视图。而python中，切片是原始数组的复制。