from functools import reduce

from lab_5.ex_1 import Number2Pattern, PatternToNumber


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
if __name__ == '__main__':
    text = input()
    k = int(input())
    print('\n'.join(
        map(lambda x: Number2Pattern(x, len(text)), sorted(map(lambda x: PatternToNumber(x), Neighbours(text, k))))))