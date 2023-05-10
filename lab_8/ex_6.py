from lab_8.ex_3 import Graph
from lab_8.ex_4 import walk
from lab_8.ex_5 import rewind


def eulerian_cycle(G):
    # конструируем первоначальный цикл из первой в лексикографическом порядке вершины графа
    cycle = walk(G)

    # если цикл пустой или цикл - не цикл, то заканчиваем работу
    if cycle == [] or cycle[0] != cycle[-1]:
        return None

    # делаем перемотку, продолжаем идти, делаем перемотку, продолжаем идти и т.д.
    # как только цикл перестанет меняться (расти), заканчиваем работу и возвращаем результат
    while True:
        k = list(cycle)
        cycle = list(rewind(G, cycle))
        if k == cycle:
            break
        cycle = list(walk(G, cycle))
        if cycle == [] or cycle[0] != cycle[-1]:
            return None
    return cycle


# функция для проверки, остались ли в графе непосещенные ребра
def check_cycle(G):
    # перебираем все ребра и смотрим, есть ли непосещенные
    for e in G.edges():
        if G[e]:
            return False

    # если все ребра перебрали и непосещенных не нашли, возвращаем положительный ответ
    return True


if __name__ == '__main__':
    # считываем вершины
    vertices = [int(i) for i in input().split(' ')]
    # конструируем граф
    G = Graph(vertices, [])

    # считываем ребра и добавляем их в граф
    while True:
        try:
            e = tuple(int(i) for i in input().split(' '))
        except EOFError:
            break
        G.add_edge(e)

    # находим цикл, проверяем, все ли корректно и печатаем результат
    cycle = eulerian_cycle(G)
    if check_cycle(G):
        if cycle == None:
            print(None)
        else:
            print(' '.join(map(str, cycle)))
    else:
        print(None)