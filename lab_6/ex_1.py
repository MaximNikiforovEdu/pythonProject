def merge(A, left, mid, right):
    # вспомогательный массив, в который будут сливаться элементы
    AUX = []

    # список, в который мы будем записывать порядок сливания элементов
    indexes = []

    # Инициализируем указатели i и j
    i = left
    j = mid + 1
    # Цикл, осуществляющий слияние
    while i <= mid and j <= right:
        if A[i] <= A[j]:
            indexes.append(i)
            AUX.append(A[i])
            i += 1
        else:
            indexes.append(j)
            AUX.append(A[j])
            j += 1

    # Дописываем хвост (почитайте справку к функции extend для списков) и не забываем про indexes
    AUX.extend(A[j:right + 1] if i > mid else A[i:mid + 1])
    indexes.extend([k for k in range(j, right + 1)] if i > mid else [k for k in range(i, mid + 1)])
    # Возвращаем назад в массив A результат нашей работы (обратите внимание на присваивание срезу!)
    A[left:right + 1] = AUX

    return indexes

# читаем массив A, массив B, склеиваем их
if __name__ == '__main__':
    array = input().split(' ')
    A = [int(i) for i in array]
    array = input().split(' ')
    B = [int(i) for i in array]
    mid = len(A) - 1
    A.extend(B)
    # вызываем merge, результат преобразуем к нужному виду и выводим
    merge_arr = merge(A, 0, mid, len(A) - 1)
    print(' '.join(str(i) for i in A))
    print(' '.join(str(i) for i in merge_arr))