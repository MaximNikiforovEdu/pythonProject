from functools import reduce

from lab_5.ex_1 import PatternToNumber, Number2Pattern
from lab_5.ex_2 import HammingDistance


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

if __name__ == '__main__':
    text = input()
    kd = input()
    print(' '.join(FrequentWordsWithMismatches(text, int(kd.split(' ')[0]), int(kd.split(' ')[1]))))