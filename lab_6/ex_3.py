from lab_6.ex_1 import merge


def mergeSortNonRec(A):
    # запоминаем длину массива
    n = len(A)

    # инициализируем переменную, в которой будем хранить длину сливаемых массивов
    width = 1

    # запускаем внешний цикл, который будет перебирать удваивающиеся значения width
    while width < n:
        i = 0
        # запускаем цикл, который будет сливать половины подмассивов размером 2*width
        while i < n:
            merge(A, i, i + width - 1, min(i + 2 * width - 1, n - 1))
            # не забываем увеличивать i на нужное значение
            i += width * 2
        # не забываем увеличивать width на нужное значение
        width *= 2

        # выводим массив в нужном формате
        print(" ".join(map(str, A)))
if __name__ == '__main__':
    # читаем массив A
    A = [int(i) for i in input().split(' ')]
    # вызываем mergeSortNonRec
    mergeSortNonRec(A)