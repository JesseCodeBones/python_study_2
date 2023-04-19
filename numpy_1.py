import numpy as np
a = np.array([1,2,3])
print(a)

a = np.array([1, 2, 3, 4, 5], ndmin =  2)  
print(a)

a = np.array([1,  2,  3], dtype = float)  
print (a)

## 一，类型

# 名称	描述
# bool_	布尔型数据类型（True 或者 False）
# int_	默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
# intc	与 C 的 int 类型一样，一般是 int32 或 int 64
# intp	用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）
# int8	字节（-128 to 127）
# int16	整数（-32768 to 32767）
# int32	整数（-2147483648 to 2147483647）
# int64	整数（-9223372036854775808 to 9223372036854775807）
# uint8	无符号整数（0 to 255）
# uint16	无符号整数（0 to 65535）
# uint32	无符号整数（0 to 4294967295）
# uint64	无符号整数（0 to 18446744073709551615）
# float_	float64 类型的简写
# float16	半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
# float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
# float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
# complex_	complex128 类型的简写，即 128 位复数
# complex64	复数，表示双 32 位浮点数（实数部分和虚数部分）
# complex128	复数，表示双 64 位浮点数（实数部分和虚数部分）

# int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
dt = np.dtype('i4')
print(dt)

dt = np.dtype([('age',np.int8)]) 
print(dt)

dt = np.dtype([('age', np.int8), ('type', np.int8)]) 
a = np.array([(10,12,),(20,12,),(30,12,)], dtype = dt) 
print(a['age'])
print(a['type'])

student = np.dtype([('name','S20'), ('age', 'i1'), ('marks', 'f4')]) 
a = np.array([('abc', 21, 50),('xyz', 18, 75)], dtype = student) 
print(a['name'])


## 二，数组属性

# 属性	说明
# ndarray.ndim	秩，即轴的数量或维度的数量
# ndarray.shape	数组的维度，对于矩阵，n 行 m 列
# ndarray.size	数组元素的总个数，相当于 .shape 中 n*m 的值
# ndarray.dtype	ndarray 对象的元素类型
# ndarray.itemsize	ndarray 对象中每个元素的大小，以字节为单位
# ndarray.flags	ndarray 对象的内存信息
# ndarray.real	ndarray元素的实部
# ndarray.imag	ndarray 元素的虚部
# ndarray.data	包含实际数组元素的缓冲区，由于一般通过数组的索引获取元素，所以通常不需要使用这个属性。

a = np.arange(24)
print(a)
b = a.reshape(2,3,4)
print(b)

a = np.array([[1,2,3],[4,5,6]])  
print (a.shape)

a = np.array([[1,2,3],[4,5,6]]) 
b = a.reshape(3,2)  
print (b)

# itemsize 
# 数组的 dtype 为 int8（一个字节）  
x = np.array([1,2,3,4,5], dtype = np.int8)  
print (x.itemsize)
 
# 数组的 dtype 现在为 float64（八个字节） 
y = np.array([1,2,3,4,5], dtype = np.float64)  
print (y.itemsize)



# 创建数组

#empty zeros ones
x = np.zeros([3,2], dtype=int)
print(x)

#buffer to np array
s =  b'Hello World' 
a = np.frombuffer(s, dtype =  'S1')  
print (a)

#numpy.arange(start, stop, step, dtype)
x = np.arange(10,20,2)  
print (x)

# numpy.logspace 等比数列
# numpy.linspace 等差数列



# 切片和索引

a = np.arange(10)
s = slice(2,7,2)   # 从索引 2 开始到索引 7 停止，间隔为2
print (a[s])

a = np.arange(10)  
b = a[2:7:2]   # 从索引 2 开始到索引 7 停止，间隔为 2
print(b)

print('列编辑')
a = np.array([[1,2,3],[3,4,5],[4,5,6]])  
print (a[...,1])   # 第2列元素
print (a[1,...])   # 第2行元素
print (a[...,1:])  # 第2列及剩下的所有元素

#矩阵索引
x = np.array([[1,  2],  [3,  4],  [5,  6]]) 
y = x[[0,1,2],  [0,1,0]]  
# (0, 0) (1, 1) (2, 0) 来定位二位矩阵
print (y)

#只取虚数
a = np.array([1,  2+6j,  5,  3.5+5j])  
print (a[np.iscomplex(a)])


# 矩阵运算
a = np.array([[ 0, 0, 0],
           [10,10,10],
           [20,20,20]])
b = np.array([1,2,3])
print(b*a)

#矩阵迭代
a = np.arange(6).reshape(2,3)
print ('原始数组是：')
print (a)
print ('\n')
print ('迭代输出元素：')
for x in np.nditer(a):
    print (x, end=", " )
print ('\n')


# transform
 
a = np.arange(8)
print ('原始数组：')
print (a)
print ('\n')
 
b = a.reshape(4,2) # 4列2行
print ('修改后的数组：')
print (b)


# 连接数组 concatenate
# 函数	描述
# concatenate	连接沿现有轴的数组序列
# stack	沿着新的轴加入一系列数组。
# hstack	水平堆叠序列中的数组（列方向）
# vstack	竖直堆叠序列中的数组（行方向）

a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
print ('沿轴 0 连接两个数组：')
print (np.concatenate((a,b)))

print ('沿轴 1 连接两个数组：')
print (np.concatenate((a,b),axis = 1))


#堆叠数组stack
a = np.array([[1,2],[3,4]])
 
print ('第一个数组：')
print (a)
print ('\n')
b = np.array([[5,6],[7,8]])
 
print ('第二个数组：')
print (b)
print ('\n')
 
print ('沿轴 0 堆叠两个数组：')
print (np.stack((a,b),0))
print ('\n')
 
print ('沿轴 1 堆叠两个数组：')
print (np.stack((a,b),1))

#分割数组 split


# 数组元素的添加与删除
# 函数	元素及描述
# resize	返回指定形状的新数组
# append	将值添加到数组末尾
# insert	沿指定轴将值插入到指定下标之前
# delete	删掉某个轴的子数组，并返回删除后的新数组
# unique	查找数组内的唯一元素



# 文件操作
# load() 和 save() 函数是读写文件数组数据的两个主要函数，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npy 的文件中。
# savez() 函数用于将多个数组写入文件，默认情况下，数组是以未压缩的原始二进制格式保存在扩展名为 .npz 的文件中。
# loadtxt() 和 savetxt() 函数处理正常的文本文件(.txt 等)