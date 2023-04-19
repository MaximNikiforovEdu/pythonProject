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
    # Базис №1
    if d == 0:
        return {Pattern}

    # Базис №2
    if len(Pattern) == 1:
        return {'A', 'C', 'G', 'T'}

    Neighborhood = set()
    # Рекурсивно находим d-соседей суффикса Pattern
    SuffixNeighbors = Neighbours(Pattern[1:], d)
    # Цикл по всем найденным соседям - шаг 2 алгоритма (рекурсивная часть)
    for neighbor in SuffixNeighbors:
        if HammingDistance(neighbor, Pattern[1:]) < d:
            for x in {'A', 'C', 'G', 'T'}:
                Neighborhood.add(x + neighbor)
        else:
            Neighborhood.add(Pattern[0] + neighbor)
    # Не будем преобразовывать ответ в список и сортировать его
    # Помните - то, что мы здесь возвращаем, мы же потом и используем на верхних шагах рекурсии!
    return Neighborhood


# читаем text как текст и k как число с клавиатуры
# вызываем Neighbours, результат преобразуем к нужному виду и выводим
text = input()
k = int(input())
print('\n'.join(
    map(lambda x: Number2Pattern(x, len(text)), sorted(map(lambda x: PatternToNumber(x), Neighbours(text, k))))))