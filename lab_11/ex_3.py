from typing import List, Tuple, Union
from lab_10.ex_5 import UnionFind
from lab_11.ex_2 import print_spanning_tree

def Kruskal_MST_optimal(N: int, edges: List[Tuple[int]]) -> Union[List[Tuple[int]], UnionFind]:
    # создаем СНМ со всеми вершинами
    uf: UnionFind = UnionFind()
    i: int
    for i in range(N):
        uf.make_set(i)

    # создаем пустой список для хранения ребер остова
    A: List[Tuple[int]] = []

    # сортируем список ребер
    edges.sort(key = lambda x: x[2])

    # перебираем ребра и выполняем алгоритм
    e: Tuple[int]
    for e in edges:
        if not uf.connected(e[0], e[1]):
            A.append(e)
            uf.union_set(e[0], e[1])
    # возвращаем остов, а представление G в виде
    # возвращаем остов и СНМ (для дальнейшей печати)
    return A, uf


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
    A: List[Tuple[int]]
    uf: UnionFind
    A, uf = Kruskal_MST_optimal(N, edges)
    print_spanning_tree(A)
    print(uf)