def bfs(matrix, root, marks):
    n = len(matrix)
    marks[root] = 1
    queue = [root]
    res = []
    while queue:
        x = queue.pop(0)
        for i in range(n):
            if matrix[x][i] and not marks[i]:
                marks[i] = 1
                queue.append(i)
        res.append(x)
    return res


if __name__ == '__main__':
    r_n = list(map(int, input().split()))
    matrix = []
    for i in range(r_n[1]):
        matrix.append(list(map(int, input().split())))
    marks = [0] * r_n[1]
    print(' '.join(map(str, bfs(matrix, r_n[0], marks))))