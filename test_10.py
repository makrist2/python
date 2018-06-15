def saddle_point(matrix):
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            cur = matrix[i][j]
            min_r = min(matrix[i])
            max_c = max(map(lambda x: x[j], matrix))
            if cur == min_r == max_c:
                return [i, j]
    return False


assert saddle_point([[3, 2, 1], [1, 3, 4]]) != True
assert saddle_point([[3, 8, 7], [5, 9, 6], [2, 6, 7]]) == [1, 0]