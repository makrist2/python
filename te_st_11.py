import numpy as np

matrix = np.array([[3, 8, 7, 2, 5, 3],
                   [5, 9, 6, 1, 9, 2],
                   [2, 6, 5, 0, 8, 1]])
i = 0
while i < 6:
    matrix_new = matrix[:, i]
    i += 1
    if i % 2 == 0:
        even = np.sort(matrix_new)
        print('Even column # %d = %s' % (i, even))
    else:
        odd = np.sort(matrix_new)[::-1]
        print('Odd column # %d = %s' % (i, odd))

#      PRINT RESULTS
# Odd column # 1 = [5 3 2]
# Even column # 2 = [6 8 9]
# Odd column # 3 = [7 6 5]
# Even column # 4 = [0 1 2]
# Odd column # 5 = [9 8 5]
# Even column # 6 = [1 2 3]