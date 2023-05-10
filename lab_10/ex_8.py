# для метода sift_down понадобятся вспомогательные методы left_son, right_son, min_son
# не забудьте про аннотирование типов!
from typing import List

def left_son(p: int) -> int:
    # возвращаем индекс левого сына элемента p
    return (p + 1) * 2 - 1

def right_son(p: int) -> int:
    # возвращаем индекс правого сына элемента p
    return (p + 1) * 2

def min_son(heap: List[int], p: int) -> int:
    # возвращаем индекс минимального сына элемента p или -1, если p - лист
    return -1 if len(heap) <= left_son(p) else left_son(p) if len(heap) <= right_son(p) or heap[right_son(p)] > heap[left_son(p)] else right_son(p)

def sift_down(heap: List[int], p: int) -> None:
    minCh: int = min_son(heap, p)
    # пока мы не в листе и текущий элемент больше минимального из сыновей,
    # меняем их местами и погружаемся ниже
    while minCh != -1 and heap[p] > heap[minCh]:
        heap[minCh], heap[p] = heap[p], heap[minCh]
        p = minCh
        minCh = min_son(heap, p)


if __name__ == '__main__':
    # считать массив heap
    heap: List[int] = list(map(int, input().split()))

    # считать индекс всплываемого элемента
    p: int = int(input())

    # осуществляем всплытие
    sift_down(heap, p)

    # напечатать heap
    print(' '.join(map(str, heap)))