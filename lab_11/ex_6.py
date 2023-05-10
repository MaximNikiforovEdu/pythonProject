# функция принимает на вход количество вершин в графе N и список ребер edges
# каждое ребро задано кортежом (u, v, cost)
# вернуть функция должна списки смежных вершин в описанном в задании формате
from typing import List, Tuple, Optional


def edges2adj(N: int, edges: List[Tuple[int]]) -> List[List[int]]:
    i: int
    ed_list: List[List[int]] = [[] for i in range(N)]
    edge: Tuple[int]
    for edge in edges:
        ed_list[edge[0]].append([edge[1], edge[2]])
        ed_list[edge[1]].append([edge[0], edge[2]])
    return ed_list


# принимает на вход граф G, построенный с помощью edges2adj, и массив предков
# находит сумму весов ребер, записанных в pi, печатает сумму и сам список pi
def print_spanning_tree(G: List[List[int]], pi: List[Optional[int]]) -> None:
    N: int = len(G)
    summa: int = 0
    v: int
    for v in range(N):
        if pi[v] != None:
            i: List[int]
            for i in G[v]:
                if i[0] == pi[v]:
                    summa += i[1]
    print(summa)
    print(pi)


if __name__ == '__main__':
    # считываем количество вершин
    N: int = int(input())

    # считываем массив предков pi (не забываем заменить -1 на None)
    pi: List[Optional[int]] = list(map(int, input().split()))
    i: int
    for i in range(N):
        if pi[i] == -1:
            pi[i] = None

    edges: List[Tuple[int]] = []
    try:
        while True:
            edge: Tuple[int] = tuple(map(int, input().split()))
            edges.append(edge)
    except:
        pass

    # делаем работу и печатаем результат
    G: List[List[int]] = edges2adj(N, edges)
    print_spanning_tree(G, pi)