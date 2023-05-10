# для корректной работы функции обхода мы можем хранить граф, например, с помощью матрицы смежности
from typing import List, Tuple
from lab_9.ex_7 import bfs


def edges2matrix(N: int, edges: List[Tuple[int]]) -> List[List[int]]:
    matrix: List[List[int]] = [[0] * N for i in range(N)]
    e: Tuple[int]
    for e in edges:
        matrix[e[0]][e[1]] = 1
        matrix[e[1]][e[0]] = 1
    return matrix


def is_safe(G: List[List[int]], e: Tuple[int]) -> bool:
    # e - это tuple с ребром
    u: int = e[0]
    v: int = e[0]

    # сохраняем ребро e и удаляем его из G
    flag: bool = False
    if G[u][v] == 1:
        G[u][v] = 0
        flag = True

    # запускаем обход из вершины u.
    # Если во время обхода встретилась v, то ВОЗВРАЩАЕМ в граф ребро e с помощью savedEdgeInfo
    # и выдаем отрицательный результат
    N: int = len(G)
    obhod: List[int] = bfs(G, u, [0] * N)
    if flag:
        G[u][v] = 1
    if v in obhod:
        return False
    else:
        return True


if __name__ == '__main__':
    # считываем первую строку
    N: int
    u: int
    v: int
    N, u, v = map(int, input().split())
    edges: List[Tuple[int]] = []
    try:
        while True:
            edge: Tuple[int] = tuple(map(int, input().split()))
            edges.append(edge)
    except:
        pass
    # создаем представление графа для обхода
    G: List[List[int]] = edges2matrix(N, edges)

    # делаем работу и печатаем результат
    print(is_safe(G, (u, v)))