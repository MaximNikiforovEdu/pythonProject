ACGTtoInt = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
IntToACGT = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}


def Number2Pattern(index, k):
    if k == 1:
        return IntToACGT[index]
    q = index // 4
    r = index % 4
    return Number2Pattern(q, k - 1) + IntToACGT[r]


def PatternToNumber(dna):
    if len(dna) == 0:
        return 0

    char = dna[-1]
    dna = dna[:-1]

    return PatternToNumber(dna) * 4 + ACGTtoInt[char]


def FrequentWordsWithSorting(text, k):
    FrequentPatterns = []
    index = []
    len_text = len(text)
    # Цикл, который заполняет список Index в соответствии с шагами 1-2 алгоритма
    # Попробуйте не выполнять в явном виде шаг 1 - записывайте в Index сразу числа...
    for i in range(len_text - k + 1):
        index.append(PatternToNumber(text[i:i + k]))

    # Сортировка Index. Результат сохраняем в SortedIndex
    # Обратите внимание: встроенный метод sort() ничего не возвращает, а сортирует на месте (in-place)!
    SortedIndex = sorted(index)

    Count = [1] * (len_text - k + 1)
    # Цикл, который за один проход заполняет массив Count, используя SortedIndex
    for i in range(1, len_text - k + 1):
        if SortedIndex[i] == SortedIndex[i - 1]:
            Count[i] = Count[i - 1] + 1

    # находим максимальное значение в Count
    maxCount = max(Count)

    # Реализация шага 6. Не используйте в явном виде циклы. Попробуйте использовать
    # функции filter, enumerate и map
    FrequentPatterns = list(map(lambda x: Number2Pattern(SortedIndex[x[0]], k),
                                filter(lambda x: x[1] == maxCount, enumerate(Count, start=0))))

    # нужно ли нам сортировать FrequentPatterns перед тем, как вернуть?
    return Count, FrequentPatterns


# читаем text как текст и k как число с клавиатуры
# вызываем FrequentWordsWithSorting, результат преобразуем к нужному виду и выводим
if __name__ == '__main__':
    text = input()
    k = int(input())
    print(' '.join(str(i) for i in FrequentWordsWithSorting(text, k)[0]))
    print(' '.join(FrequentWordsWithSorting(text, k)[1]))