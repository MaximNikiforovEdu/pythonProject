# возможно какие-то методы можно скопировать из упражнения 10.1
# не забудьте про аннотирование типов!
from typing import List

class UnionFind:
    # конструктор, создающий пустой массив для хранения СНМ
    def __init__(self) -> None:
        self._id: List[int] = []

    # добавляет в СНМ еще один элемент
    def make_set(self) -> None:
        self._id.append(len(self._id))

    # возвращает корень дерева, которому принадлежит x
    def root(self, x: int) -> int:
        while(x != self._id[x]):
            x = self._id[x]
        return x

    # возвращает строку с элементами множества
    def __str__(self) -> str:
        return ' '.join(map(str, self._id))

    # объединяет два множества, представленные своими элементами x и y
    def union_set(self, x: int, y: int) -> None:
        if not self.connected(x, y):
            self._id[self.root(y)] = self._id[self.root(x)]

    # возвращает True, если x и y связаны, и False в противном случае
    def connected(self, x: int, y: int) -> bool:
        return self.root(x) == self.root(y)


if __name__ == '__main__':
    # считайте N
    N: int = int(input())

    # создайте СНМ и положите в нее N элементов с помощью make_set
    uf: UnionFind = UnionFind()
    elem: int
    for elem in range(N):
        uf.make_set()

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