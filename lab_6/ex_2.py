from lab_6.ex_1 import merge


def mergeSort(A, left=0, right=None, verbose=False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if len(A[left:right + 1]) <= 1:
        return

    # определяем середину
    mid = (right + left) // 2

    # рекурсивно сортируем обе половины
    mergeSort(A, left, mid, verbose)
    mergeSort(A, mid + 1, right, verbose)
    # печатаем массив и производим слияние с помощью функции merge
    if verbose:
        arr = ""
        if left != 0:
            arr += " ".join(map(str, A[:left])) + " "
        arr += "[" + " ".join(map(str, A[left:mid + 1])) + "] [" + " ".join(map(str, A[mid + 1: right + 1])) + "]"
        if right != len(A) - 1:
            arr += " " + " ".join(map(str, A[right + 1:]))
        print(arr)
    else:
        print(' '.join(str(i) for i in A))
    merge(A, left, mid, right)

if __name__ == '__main__':
    # читаем список A (и возможно слово 'verbose' на второй строке)
    A = [int(i) for i in input().split(' ')]
    # вызываем mergeSort и не забываем напечатать результат его работы еще раз!

    try:
        verbose = input()
        if verbose == 'verbose':
            verbose = True
    except EOFError:
        verbose = False

    mergeSort(A, 0, len(A) - 1, verbose)
    print(" ".join(map(str, A)))