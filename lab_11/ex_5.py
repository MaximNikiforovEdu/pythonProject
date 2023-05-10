from typing import List, Tuple, Optional
from lab_11.ex_4 import min_edge
from lab_11.ex_2 import print_spanning_tree


def Prim_MST(G: List[Tuple[int]], N: int) -> List[Tuple[int]]:
    # создаем пустой список для хранения ребер остова
    A: List[Tuple[int]] = []

    # создаем список для покрытых вершин и кладем в него любую вершину
    Q: List[int] = [0]

    # перебираем ребра, можно запустить "вечный" цикл и завершить его с помощью break,
    # который вызовется, когда min_edge вернет None
    while True:
        # выполняем алгоритм, не забываем добавлять ребро в A, а непокрытую (!) вершину в Q
        min_ed: Tuple[Optional[int]] = min_edge(G, Q)
        if min_ed == None:
            break
        if min_ed[0] not in Q:
            Q.append(min_ed[0])
        else:
            Q.append(min_ed[1])
        A.append(min_ed)

    # возвращаем остов
    return A


if __name__ == '__main__':
    # считываем количество вершин
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
    A: List[Tuple[int]] = Prim_MST(edges, N)
    print_spanning_tree(A)