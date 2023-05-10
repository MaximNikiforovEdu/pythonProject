from lab_6.ex_4 import partition


def verbosePrint(A, left, p, right):
    arr = ""
    if left > 0:
        arr += " ".join(map(str, A[:left])) + " "
    if p - 1 >= left:
        arr += "[" + " ".join(map(str, A[left:p])) + "] "
    else:
        arr += "[] "
    arr += " ".join(map(str, A[p:p + 1])) + " [" + " ".join(map(str, A[p + 1:right + 1])) + "]"
    if right < len(A) - 1:
        arr += " " + " ".join(map(str, A[right + 1:]))
    print(arr)


def quickSort(A, left=0, right=None, verbose=False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right or len(A) <= 1:
        return
    # производим разбиение с помощью partition
    p = partition(A, left, right)

    # печатаем массив
    if verbose:
        verbosePrint(A, left, p, right)
    else:
        print(" ".join(map(str, A)))

    # рекурсивно сортируем обе части
    quickSort(A, left, p - 1, verbose)
    quickSort(A, p + 1, right, verbose)


if __name__ == '__main__':
    # читаем список A (и возможно слово 'verbose' на второй строке)
    A = [int(i) for i in input().split(' ')]
    try:
        verbose = input()
        if verbose == 'verbose':
            verbose = True
    except EOFError:
        verbose = False
    # вызываем quickSort
    quickSort(A, 0, None, verbose)