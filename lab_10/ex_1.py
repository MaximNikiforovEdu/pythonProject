# Не забудьте про аннотирование типов!
from typing import List

class QuickFind:
    # конструктор, создающий пустой массив для хранения СНМ
    def __init__(self) -> None:
        self._id: List[int] = []

    # добавляет в СНМ еще один элемент
    def make_set(self) -> None:
        self._id.append(len(self._id))

    # возвращает идентификатор множества, в котором лежит элемент x
    def find_set(self, x: int) -> int:
        return self._id[x]

    # возвращает строку с элементами множества
    def __str__(self) -> str:
        return ' '.join(map(str, self._id))

    # объединяет два множества, представленные своими элементами x и y
    def union_set(self, x: int, y: int) -> None:
        id_x: int = self.find_set(x)
        id_y: int = self.find_set(y)
        if id_x != id_y:
            while id_y in self._id:
                self._id[self._id.index(id_y)] = id_x

    # возвращает True, если x и y связаны, и False в противном случае
    def connected(self, x: int, y: int) -> bool:
        return self._id[x] == self._id[y]


if __name__ == '__main__':
    # считайте N
    N: int = int(input())

    # создайте СНМ и положите в нее N элементов с помощью make_set
    uf: QuickFind = QuickFind()
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