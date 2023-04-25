def sort_podschet(arr):
    k = max(arr)
    chast = [0 for i in range(k + 1)]
    len_arr = len(arr)
    rez = []
    for i in arr:
        chast[i] += 1
    for i in range(k + 1):
        for j in range(chast[i]):
            rez.append(str(i))
    return rez

if __name__ == '__main__':
    arr = input().split(' ')
    arr = [int(i) for i in arr]
    print(' '.join(sort_podschet(arr)))