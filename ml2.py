import numpy as np

a = np.array([1, 2, 3], dtype=np.int32)
print(a) #здесь дефолт ввывод массива только числа

z = np.zeros((2, 3))
print(z) #матрица 2 строки и 3 столбца

o = np.ones((2, 3))
print(o) #также ток 1

f = np.full((2, 3), fill_value=3)
print(f)    #также ток мы сами пишем чем заплонить матицу. Также можно поствить как тип данных может быть

r = np.arange(0, 10, 2)
print(r) #здесь масств от 0 до 10 через каждык 2 шага

l = np.linspace(0, 1, 5)
print(l) #почти такжее ток мы создаем массива и указваем сколько будет шагов

A = np.arange(12).reshape(3, 4)
print(A) #здесь мы создаем матрицу 3 на 4 где элементы от 0 до 11

row0 = A[0]
print(row0) #здесь мы получаем первую строку матрицы

col1 = A[:, 0]
print(col1) #здесь такжее ток столбец

block = A[0:2, 1:3]
print(block) #здесь мы получаем блок 2 на 2 то есть берем строки от 0 до 1 и столбы от 1 до 2

block[0, 0] = 123
print(block) #новый элемент матрицы

A = np.arange(10)
print(A) #массив от 0 до 9

idx = [0,2,5]
picked = A[idx]
print(picked) #здесь мы выбираем элементы с индексами 0, 2 и 5

mask = A % 2 == 0
print(mask) #те элементы которые четные

evens = A[mask]
print(evens) #здесь мы получаем четные элементы массива

B = np.arange(12)
B2 = B.reshape(3, 4)
print(B2) 

flat_view = B2.ravel()
print(flat_view)  # Плоский вид матрицы

flat_copy = B2.flatten()
print(flat_copy)  # Плоская копия матрицы

BT = B2.T
print(BT) # мы здесь меняем строки на столбцы и наоборот
print()

C = np.concatenate([B2, B2], axis=0)
print(C) # Здесь мы соединяем две матрицы по вертикали а если было бы 1 то по горизонтали

x = np.linspace(0, 2*np.pi, 100)
print(x)  # Генерация 100 точек от 0 до 2π

y = np.sin(x)
print(y)  # Генерация значений синуса для каждой точки

z = np.add(x, 5)
print(z)  # Добавление 5 к каждому элементу массива x

m = np.maximum(x, y)
print(m)  # Максимум между x и y для каждой точки

mean = y.mean()
print(mean)  # Среднее значение синуса

M = np.ones((3, 4))
v = np.arange(4)
M_plus_v = M + v
print(M_plus_v) # Здесь мы добавляем вектор к каждой строке матрицы

col = np.arange(3)[:, None]
print(col)  # [[0] [1] [2]]  # двумерный столбец
M_plus_col = M + col
print(M_plus_col) # Здесь мы добавляем столбец к каждой строке матрицы

X = np.random.default_rng(42).normal(size=(5, 3))
print(X)  # Генерация случайной матрицы 5x3 с нормальным распределением
mu = X.mean(axis=0)
print(mu)  # Среднее значение по столбцам

sigma = X.std(axis=0)
print(sigma)  # Стандартное отклонение по столбцам

X_norm = (X - mu) / sigma
print(X_norm)  # Нормализация матрицы X

rng = np.random.default_rng(seed=123)
U = rng.uniform(1, 10, size=(2, 3))
print(U)  # Генерация случайной матрицы 2x3 с равномерным распределением от 1 до 10
N = rng.normal(loc=0, scale=1, size=(2, 3))
print(N)  # Генерация случайной матрицы 2x3 с нормальным распределением
perm = rng.permutation(10)
print(perm)  # Генерация случайной перестановки от 0 до 9

# задание А

A = np.arange(12).reshape(3, 4)
print(A)
print(A.shape) # форма матрицы
print(A.ndim) # количество измерений
print(A.size) # количество элементов в матрице
print(A.dtype) # тип данных в матрице

A = A.reshape(4, 3)
print(A)

AT = np.may_share_memory(A, A.ravel())  # Проверка, делят ли матрица и ее транспонированная версия память
print(AT)  
AT2 = np.may_share_memory(A, A.flatten())
print(AT2)

# задание B
B = np.arange(1, 26).reshape(5, 5)
print(B)

Block = B[1:4, 1:4]
print(Block)

B[B > B.mean()] = 0
print(B)  # Здесь мы обнуляем элементы, которые больше среднего значения

idxrows = [0, 2, 4]  
rows = B[idxrows, 0]

rows = np.array([0, 1, 3])
cols = np.array([0, 2, 4])
picked = B[rows, cols] 
print(picked)  

# Задание C
rng = np.random.default_rng(1)
rngSize = rng.random(size=(100, 3))
sigma = rngSize.std(axis=0)
mu = rngSize.mean(axis=0)
res = (rngSize - mu) / sigma
C = np.concatenate([np.ones((rngSize.shape[0], 1)), res], axis=1)

row_norms = np.sqrt((sigma**2).sum())
print(row_norms)