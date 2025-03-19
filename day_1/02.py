import numpy as np

X = np.array([[51, 55], [14, 19], [0, 4]])
# print(X)

# print(X[0])


# for row in X:
#     print(row)


X = X.flatten()

# print(np.array([0, 2, 4]))  # [0 2 4]
# print(X[np.array([[0, 2, 4]])])  # [51 14  0]

print(X > 15)  # [ True  True False  True False False]
print(X[X > 15])  # [51 55 19]
