def verbosePrint(A, left, lt, gt, right):
    arr = ""
    if left > 0:
        arr += " ".join(map(str, A[:left])) + " "
    if lt - 1 >= left:
        arr += "[" + " ".join(map(str, A[left:lt])) + "] "
    else:
        arr += "[] "
    arr += " ".join(map(str, A[lt:gt + 1])) + " [" + " ".join(map(str, A[gt + 1:right + 1])) + "]"
    if right < len(A) - 1:
        arr += " " + " ".join(map(str, A[right + 1:]))
    print(arr)


def quickSort3Way(A, left=0, right=None, verbose=False):
    # если параметр right == None, то это первый вызов и надо исправить его на реальное значение
    if right == None:
        right = len(A) - 1

    # если массив пустой или состоит всего из одного элемента, заканчиваем
    if left >= right:
        return

    # инициализируем всевозможные указатели
    lt = left
    gt = right
    v = A[left]
    i = left + 1

    # производим трехпутевое разбиение за один проход в соответствии с алгоритмом
    while i <= gt:
        if A[i] < v:
            A[i], A[lt] = A[lt], A[i]
            lt += 1
            i += 1
        elif A[i] > v:
            A[i], A[gt] = A[gt], A[i]
            gt -= 1
        else:
            i += 1

            # печатаем массив в нужном формате
    if verbose:
        verbosePrint(A, left, lt, gt, right)
    else:
        print(" ".join(map(str, A)))

    # рекурсивно сортируем обе части (кроме той, что равна опорному элементу!)
    quickSort3Way(A, left, lt - 1, verbose)
    quickSort3Way(A, gt + 1, right, verbose)


if __name__ == '__main__':
    # читаем список A (и возможно слово 'verbose' на второй строке)
    A = [int(i) for i in input().split(' ')]
    try:
        verbose = input()
        if verbose == 'verbose':
            verbose = True
    except EOFError:
        verbose = False

    # вызываем quickSort3Way
    quickSort3Way(A, 0, None, verbose)