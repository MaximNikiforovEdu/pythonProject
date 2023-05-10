# не забудьте про аннотирование типов!
from typing import List


class Heap:
    # конструктор, инициализирующий все необходимые поля необходимыми значениями
    def __init__(self) -> None:
        self.heap: List[int] = []

    def left_son(self, p: int) -> int:
        return (p + 1) * 2 - 1

    def right_son(self, p: int) -> int:
        return (p + 1) * 2

    def parent(self, p: int) -> int:
        if p == 0:
            return p
        return (p + 1) // 2 - 1

    def min_son(self, p: int) -> int:
        return -1 if len(self.heap) <= self.left_son(p) else self.left_son(p) if len(self.heap) <= self.right_son(p) or self.heap[self.right_son(p)] > self.heap[self.left_son(p)] else self.right_son(p)

    def sift_up(self, p: int) -> None:
        if p == 0:
            return
        prnt: int = self.parent(p)
        while p != 0 and self.heap[p] < self.heap[prnt]:
            self.heap[p], self.heap[prnt] = self.heap[prnt], self.heap[p]
            p = prnt
            prnt = self.parent(p)

    def sift_down(self, p: int) -> None:
        minCh: int = self.min_son(p)
        while minCh != -1 and self.heap[p] > self.heap[minCh]:
            self.heap[minCh], self.heap[p] = self.heap[p], self.heap[minCh]
            p = minCh
            minCh = self.min_son(p)

    # метод для добавления элемента x в кучу
    def add(self, x: int) -> None:
        self.heap.append(x)
        self.sift_up(len(self.heap) - 1)

    # метод для возврата минимума
    def min(self) -> int:
        return self.heap[0]

    # метод для возврата минимума и удаления его из кучи
    def get_min(self) -> int:
        if (len(self.heap) == 1):
            return self.heap.pop()
        minim = self.min()
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return minim

    # печать массива с бинарным деревом кучи
    def __str__(self) -> str:
        return ' '.join(map(str, self.heap))


# Этот код менять не нужно. При корректной реализации класса Heap он должен выдать корректный результат
# Раскомментируйте этот код, когда перестанете получать сообщения об ошибках
if __name__ == '__main__':
    heap: Heap = Heap()
    heap.add(1)
    heap.add(10)
    heap.add(8)
    heap.add(32)
    heap.add(11)
    heap.add(38)
    heap.add(42)
    heap.add(78)
    heap.add(31)
    print(heap)