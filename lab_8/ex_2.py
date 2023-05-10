from lab_8.ex_1 import Graph


# функция, создающая граф де Брёйна
def construct_de_Brujin(patterns):
    Brujin_graph = Graph()
    for pattern in patterns:
        Brujin_graph.add_vertex(pattern[:len(pattern) - 1])
        Brujin_graph.add_vertex(pattern[1:])
        Brujin_graph.add_edge((pattern[:len(pattern) - 1], pattern[1:]))
    return Brujin_graph


if __name__ == "__main__":
    patterns = []
    pattern = []
    # считываем строки в patterns, пока не кончатся
    while True:
        try:
            pattern = input()
        except EOFError:
            break
        patterns.append(pattern)
    G = construct_de_Brujin(patterns)
    print(G)