# для метода sift_up понадобится вспомогательный метод parent
# не забудьте про аннотирование типов!
from typing import List

def parent(p: int) -> int:
    # возвращаем индекс родителя элемента p (не забудьте про сложности округления
    # и целочисленного деления в Питоне! протестируйте свой метод!)
    return (p + 1) // 2 - 1

def sift_up(heap: List[int], p: int) -> None:
    # если мы в корне, то выходим
    if p == 0:
        return

    prnt: int = parent(p)
    # пока мы не в корне и текущий элемент меньше родительского, меняем их и поднимаемся выше
    while p != 0 and heap[p] < heap[prnt]:
        heap[p], heap[prnt] = heap[prnt], heap[p]
        p = prnt
        prnt = parent(p)


if __name__ == '__main__':
    # считать массив heap
    heap: List[int] = list(map(int, input().split()))

    # считать индекс всплываемого элемента
    p: int = int(input())

    # осуществляем всплытие
    sift_up(heap, p)

    # напечатать heap
    print(' '.join(map(str, heap)))