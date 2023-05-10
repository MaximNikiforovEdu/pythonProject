# данный класс можно скопировать из упражнения 10.5, только при этом не забудьте
# изменить названия полей и методов на требуемые и не забудьте про аннотирование типов!
from typing import List
from lab_10.ex_5 import UnionFind


if __name__ == '__main__':
    # Этот код менять не нужно. При корректной реализации класса UnionFind он должен выдать корректный результат
    # Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
    uf = UnionFind()
    for i in range(10):
        uf.make_set(i)
    print(uf.connected(6, 2))
    print(uf.connected(9, 7))
    uf.union_set(9, 0)
    uf.union_set(8, 3)
    uf.union_set(1, 4)
    print(uf.connected(7, 6))
    uf.union_set(6, 9)
    uf.union_set(7, 4)
    uf.union_set(1, 6)
    uf.union_set(0, 6)
    print(uf.connected(9, 5))
    uf.union_set(1,8)
    uf.union_set(7,9)
    print(uf.connected(9,8))
    print(uf.connected(1,2))
    uf.union_set(1,6)
    print(uf)