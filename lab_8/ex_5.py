from lab_8.ex_3 import Graph


def rewind(G, path=[]):
    # если пусть пустой или не является циклом, завершаем работу
    if path == [] or path[0] != path[-1]:
        return path

    # перебираем вершины пути и ищем первую с ненулевыми исходящими ребрами
    flag = False
    for v in path:
        for out_v in G.outgoing(v):
            if G[out_v] != 0:
                res = v
                flag = True
                break
        if flag:
            break
    # если на предыдущем шаге нашли подходящую вершину, конструируем новый путь,
    # иначе возвращаем старый
    if flag:
        return path[path.index(res):] + path[1:path.index(res) + 1]
    else:
        return path

if __name__ == '__main__':
    # Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
    # Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

    g = Graph([1, 2, 3, 4], [(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])
    g[(1, 2)] = 0
    g[(3, 4)] = 0
    g[(4, 1)] = 0
    g[(2, 3)] = 1
    print(rewind(g, [1, 2, 3, 4, 1]))
    print(rewind(g, [2, 3, 4, 1, 2]))