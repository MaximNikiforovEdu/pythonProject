# большую часть методов можно скопировать из упражнения 10.4
# не забудьте про аннотирование типов!
from typing import List


class UnionFind:
    # конструктор, создающий пустые массивы для СНМ и эвристики ранга
    def __init__(self) -> None:
        self._id: List[int] = []
        self._rank: List[int] = []

    # добавляет в СНМ еще один элемент
    # не забудьте про ранг нового элемента!
    def make_set(self, x: int) -> None:
        self._id.append(len(self._id))
        self._rank.append(0)

    # возвращает корень дерева, которому принадлежит x
    # этот метод необходимо модифицировать, добавив в него эвристику сжатия путей
    def root(self, x: int) -> int:
        y: int = x
        szatie: List[int] = []
        while (x != self._id[x]):
            szatie.append(x)
            x = self._id[x]
        y: int
        for y in szatie:
            self._id[y] = x
        return x

    # возвращает строку с элементами множества
    # этот метод необходимо модифицировать, добавив в него печать массива rank
    def __str__(self) -> str:
        return ' '.join(map(str, self._id)) + '\n' + ' '.join(map(str, self._rank))

    # объединяет два множества, представленные своими элементами x и y
    # этот метод необходимо модифицировать, добавив в него эвристику ранга
    def union_set(self, x: int, y: int) -> None:
        if not self.connected(x, y):
            if self._rank[self.root(y)] > self._rank[self.root(x)]:
                self._rank[self.root(y)] = max(self._rank[self.root(x)] + 1, self._rank[self.root(y)])
                self._id[self.root(x)] = self._id[self.root(y)]
            else:
                self._rank[self.root(x)] = max(self._rank[self.root(y)] + 1, self._rank[self.root(x)])
                self._id[self.root(y)] = self._id[self.root(x)]

    # возвращает True, если x и y связаны, и False в противном случае.
    def connected(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


if __name__ == '__main__':
    # считайте N
    N: int = int(input())

    # создайте СНМ и положите в нее N элементов с помощью make_set
    uf: UnionFind = UnionFind()
    elem: int
    for elem in range(N):
        uf.make_set(elem)

    # следующая конструкция позволит вам считывать данные из файла, пока они есть
    try:
        while True:
            # считайте команду, определите ее тип и выполните ее, вызвав соответствующий метод uf
            line: List[str] = input().split()
            if line == ["print"]:
                print(uf)
            else:
                line_0: str = line[0]
                line_1: int = int(line[1])
                line_2: int = int(line[2])
                if line_0 == '+':
                    uf.union_set(line_1, line_2)
                else:
                    print(uf.connected(line_1, line_2))
    except:
        pass