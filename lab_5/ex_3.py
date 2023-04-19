from functools import reduce

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


def HammingDistance(s1, s2):
    return reduce(lambda x, y: x + (1 if y[0] != y[1] else 0), zip(s1, s2), 0)


def Neighbours(Pattern, d):
    if d == 0:
        return {Pattern}

    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    Neighborhood = set()
    SuffixNeighbors = Neighbours(Pattern[1:], d)
    for neighbor in SuffixNeighbors:
        if HammingDistance(neighbor, Pattern[1:]) < d:
            for x in {'A', 'C', 'G', 'T'}:
                Neighborhood.add(x + neighbor)
        else:
            Neighborhood.add(Pattern[0] + neighbor)
    return Neighborhood


def FrequentWordsWithMismatches(text, k, d):
    FrequentPatterns = []
    Index = []
    len_text = len(text)
    # Заполняем список Index кодами всех d-соседей всех подстрок длины k строки text
    # Не нужно выполнять шаги 1-3 по отдельности - совместите их в одном цикле
    for i in range(len_text - k + 1):
        pochtiIndex = list(map(lambda x: PatternToNumber(x), Neighbours(text[i:i + k], d)))
        Index += pochtiIndex

    # Сортировка Index. Результат сохраняем в SortedIndex.
    SortedIndex = sorted(Index)

    len_sortedindex = len(SortedIndex)
    Count = Count = [1] * len_sortedindex
    # Цикл, который за один проход заполняет массив Count, используя SortedIndex
    for i in range(len_sortedindex):
        if SortedIndex[i] == SortedIndex[i - 1]:
            Count[i] = Count[i - 1] + 1

    # находим максимальное значение в Count
    maxCount = max(Count)

    # Реализация шага 7. Не используйте в явном виде циклы. Попробуйте использовать
    # функции filter, enumerate и map
    FrequentPatterns = list(map(lambda x: Number2Pattern(SortedIndex[x[0]], k),
                                filter(lambda x: x[1] == maxCount, enumerate(Count, start=0))))

    # нужно ли нам сортировать FrequentPatterns перед тем, как вернуть?
    return FrequentPatterns


text = input()
kd = input()
print(' '.join(FrequentWordsWithMismatches(text, int(kd.split(' ')[0]), int(kd.split(' ')[1]))))