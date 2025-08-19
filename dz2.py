import numpy as np

# rndarr = np.random.normal(loc=0, scale=1, size=100)
# data = (rndarr >= - 1) & (rndarr <= 1)
# print(data)

# matrix = np.random.normal(loc=200, scale=50, size=(200, 50))
# min_val = matrix.min(axis=0)
# mx_val = matrix.max(axis=0)
# full = (matrix - min_val) / (mx_val - min_val)
# print(full)

# array = np.arange(1, 1000)

# sum = array[(array % 3 == 0) & (array % 5 == 0)].sum()
# print(sum)

num = np.arange(101)


Full = ( (num.sum())**2 - (num**2).sum())
print(Full)