def post_processing(matrix, root, marks):
    n = len(matrix)
    print(root, end='')
    marks[root] = 1
    for i in range(n):
        if matrix[root][i] and not marks[i]:
            marks[i] = 1, 1
            print(' ', end='')
            post_processing(matrix, i, marks)


def pre_processing(matrix, root, marks, first=True):
    n = len(matrix)
    marks[root] = 1
    for i in range(n):
        if matrix[root][i] and not marks[i]:
            marks[i] = 1

            pre_processing(matrix, i, marks, False)
    if first:
        print(root, end='')
    else:
        print(root, end=' ')


if __name__ == '__main__':
    r_n = list(map(int, input().split()))
    matrix = []
    for i in range(r_n[1]):
        matrix.append(list(map(int, input().split())))
    marks = [0] * r_n[1]
    post_processing(matrix, r_n[0], list(marks))
    print()
    pre_processing(matrix, r_n[0], marks)