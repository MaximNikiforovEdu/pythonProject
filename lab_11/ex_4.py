# принимает на вход граф G в виде списка ребер и множество вершин Q
# ребро - это tuple вида (u, v, cost)
from typing import List, Tuple, Optional


def min_edge(G, Q) -> Tuple[Optional[int]]:
    # инициализируем текущее минимальное ребро
    min_e: Tuple[Optional[int]] = None

    # перебираем все ребра и ищем минимальное, удовлетворяющее условиям
    # помните, что в Q может быть любой конец ребра!
    e: Tuple[int]
    for e in G:
        if ((e[0] in Q and e[1] not in Q) or (e[1] in Q and e[0] not in Q)) and (min_e == None or min_e[2] > e[2]):
            min_e = e

    # возвращаем ответ
    return min_e

if __name__ == '__main__':
    # считываем количество вершин
    N: int = int(input())

    # считываем вершины разреза
    Q: List[int] = list(map(int, input().split()))

    edges: List[Tuple[int]] = []
    # считываем ребра
    try:
        while True:
            edge: Tuple[int] = tuple(map(int, input().split()))
            edges.append(edge)
    except:
        pass


    # делаем работу и печатаем результат
    print(min_edge(edges, Q))