class Graph:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self, V=None, E=None):
        self.V = None
        self.E = None
        self.marks_E = None
        self.marks_V = None
        if V != None:
            for v in V:
                self.add_vertex(v)
            self.marks_V = [None] * len(V)
        if E != None:
            for e in E:
                self.add_edge(e)

    # метод конструирования строкового представления графа
    def __str__(self):
        V = self.vertices()
        E = self.edges()
        s = "vertices:\n" + ' '.join(V) + "\nedges:\n"
        for e in E:
            s += e[0] + ' -> ' + e[1] + '\n'
        return s[0: len(s) - 1]

    # метод добавления метки вершине или ребру
    def __setitem__(self, x, d):
        i = 0
        if type(x) is tuple:
            for e in self.E:
                if e == x:
                    break
                i += 1
            self.marks_E[i] = d
        else:
            for v in self.V:
                if v == x:
                    break
                i += 1
            self.marks_V[i] = d

    # метод возврата метки вершины или ребра
    def __getitem__(self, x):
        i = 0
        if type(x) is tuple:
            for e in self.E:
                if e == x:
                    return self.marks_E[i]
                i += 1
        else:
            for v in self.V:
                if v == x:
                    return self.marks_V[i]
                i += 1

    # Добавляет в граф вершину v. Метка вершины должна быть None.
    def add_vertex(self, v):
        if self.V == None:
            self.V = [v]
            self.marks_V = [None]
        elif v not in self.V:
            (self.V).append(v)
            (self.marks_V).append(None)

    # Добавляет в граф ориентированное ребро e. Ребро е представляется кортежем (класс tuple)
    # двух имён рёбер (v, u). Метка ребра устанавливается в None.
    def add_edge(self, e):
        if self.E == None:
            self.E = [e]
            self.marks_E = [1]
        elif e not in self.E:
            (self.E).append(e)
            (self.marks_E).append(1)
        else:
            for i in range(len(self.E)):
                if self.E[i] == e:
                    self.marks_E[i] += 1

    # генератор или итератор, перечисляющий все рёбра графа
    def edges(self):
        sorted_E = sorted(self.E)
        for e in sorted_E:
            yield e

    # генератор или итератор, перечисляющий все вершины графа
    def vertices(self):
        sorted_V = sorted(self.V)
        for v in sorted_V:
            yield v

    # генератор или итератор, перечисляющий все рёбра, выходящие из вершины v
    def outgoing(self, v):
        res = []
        for e in self.E:
            if e[0] == v:
                res.append(e)
        return sorted(res)

if __name__ == '__main__':
    # Этот код менять не нужно. При корректной реализации класса Graph он должен выдать корректный результат
    # Раскомментируйте этот код, когда перестанете получать сообщения об ошибках

    g = Graph([1, 2, 3], [(1, 2), (2, 3), (3, 1), (2, 3)])
    print(g[(1, 2)])
    print(g[(2, 3)])
    print(g[(3, 1)])