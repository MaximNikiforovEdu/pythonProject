from lab_8.ex_2 import construct_de_Brujin
from lab_8.ex_6 import eulerian_cycle


# вспомогательная функция, которая перематывает путь до уже заданной вершины v
def rewind2v(G, path, v):
    return path[path.index(v):] + path[1:path.index(v) + 1]

# вспомогательная функция, конвертирующая эйлеров путь/цикл в строку
def conv2string(cycle):
    len_cycle = len(cycle)
    len_cycle_0 = len(cycle[0])
    s = cycle[0]
    for i in range(1, len_cycle - 1):
        s += cycle[i][len_cycle_0 - 1:]
    return s


# основная функция, выполняющая алгоритм реконструкции строки по фрагментам
def reconstruct(kmers):
    # построить размеченный граф де Брёйна по фрагментам
    G = construct_de_Brujin(kmers)

    # подсчитать входящие и исходящие степени вершин. Обратите внимание, что для ребра e = (u,v)
    # необходимо к соответствующим степеням вершин u и v прибавлять не 1, а метку ребра (u,v),
    # обозначающую его кратность!
    # степени удобно хранить в метке самой вершины
    for i in G.vertices():
        G[i] = [0, 0]
    # считаем степени
    for e in G.edges():
        G[e[0]][0] += G[e]
        G[e[1]][1] += G[e]

        # находим вершины u и v в соответствии со строками 2 и 3 алгоритма
    for ver in G.vertices():
        if G[ver][0] < G[ver][1]:
            u = ver
            break
    for ver in G.vertices():
        if G[ver][0] > G[ver][1]:
            v = ver
            break

    # добавляем ребро (u, v) в граф
    G.add_edge((u, v))

    # находим эйлеров цикл с помощью функции из упражнения 8.6
    cycle = eulerian_cycle(G)

    # перематываем его на нужную вершину, используя вспомогательную функцию rewind2v
    cycle = rewind2v(G, cycle, v)

    # конвертируем в строку и возвращаем результат
    return conv2string(cycle)

if __name__ == '__main__':
    kmers = []
    # считываем фрагменты
    while True:
        try:
            kmer = input()
        except EOFError:
            break
        kmers.append(kmer)

    # делаем работу и выводим результат
    print(reconstruct(kmers))