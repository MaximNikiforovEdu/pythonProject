def sort_podschet(arr, n):
    n += 1
    arr2 = [0 if 10 ** (n - 1) > i else int(str(i)[len(str(i)) - n:len(str(i)) - n + 1]) for i in arr]
    len_arr2 = len(arr2)
    k = max(arr2)
    b = [0] * len_arr2
    c = [0] * (k + 1)
    r = [0] * (k + 1)
    for i in arr2:
        c[i] += 1
    r[0] = c[0]
    for i in range(1, k + 1):
        r[i] = r[i - 1] + c[i]
    for i in range(len_arr2 - 1, -1, -1):
        r[arr2[i]] -= 1
        b[r[arr2[i]]] = arr[i]
    return b


def sort_cifro(arr):
    tmp = 1
    r = 1
    max_arr = max(arr)
    while (tmp * 10 <= max_arr):
        r += 1
        tmp *= 10
    rez = []
    for i in range(r):
        arr = sort_podschet(list(arr), i)
        rez.append(list(arr))
    return rez


arr = input().split(' ')
arr = [int(i) for i in arr]
sorting_steps = sort_cifro(arr)
for steps in sorting_steps:
    print(' '.join(str(i) for i in steps))