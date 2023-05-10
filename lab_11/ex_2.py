# функция для представления графа в виде, удобном для обхода виде
from typing import List, Tuple
from lab_11.ex_1 import edges2matrix
from lab_11.ex_1 import is_safe


# Мы будем параллельно использовать сразу два представления графа - список ребер для Крускала
# и матрицу смежности (или ваше на выбор) для работы функции is_safe
def Kruskal_MST(N: int, edges: List[Tuple[int]]) -> List[Tuple[int]]:
    # инициализируем матрицу смежности графом с N вершинами и БЕЗ ребер
    G: List[List[int]] = edges2matrix(N)

    # создаем пустой список для хранения ребер остова
    A: List[Tuple[int]]= []

    # сортируем список ребер
    edges.sort(key=lambda x: x[2])

    # перебираем ребра и выполняем алгоритм
    e: Tuple[int]
    for e in edges:
        # если ребро безопасное, добавим его в A и не забудем добавить в G
        if is_safe(G, (e[0], e[1])):
            A.append(e)
            G[e[0]][e[1]], G[e[1]][e[0]] = 1, 1
    # возвращаем остов, а представление G в виде матрицы смежности на больше не нужно
    return A


# функция печати остова в нужном формате
def print_spanning_tree(A) -> None:
    razmer: int = 0
    edges: List[Tuple[int]] = []
    e: Tuple[int]
    for e in A:
        razmer += e[2]
        edges.append((e[0], e[1]))
    edges.sort()
    print(razmer)
    print(' '.join(map(str, edges)))


if __name__ == '__main__':
    # считываем первую строку
    N: int = int(input())

    edges: List[Tuple[int]] = []
    # считываем ребра
    try:
        while True:
            edge: Tuple[int] = tuple(map(int, input().split()))
            edges.append(edge)
    except:
        pass

    # делаем работу и печатаем результат
    A: List[Tuple[int]] = Kruskal_MST(N, edges)
    print_spanning_tree(A)