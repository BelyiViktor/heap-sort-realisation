# Реализация пирамидальной сортировки на Python

# Процедура для преобразования в двоичную кучу поддерева с
# корневым узлом i, что является индексом в get_item(f, ). n - размер кучи.

# Подключим функции для использования файла как списка(доступ по индексам, функция swap).
from file_to_list import *


def heapify(f, n, i):

    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    # Проверяем существует ли левый дочерний элемент больший, чем корень

    if l < n and get_item(f, i) < get_item(f, l):
        largest = l

    # Проверяем существует ли правый дочерний элемент больший, чем корень

    if r < n and get_item(f, largest) < get_item(f, r):
        largest = r

    # Заменяем корень, если нужно
    if largest != i:
        swap_items(f, i, largest)

        # Применяем heapify к корню
        heapify(f, n, largest)


# Основная функция для сортировки массива заданного размера
def heap_sort(f):
    f.seek(0)
    n = 0
    while _ := f.read(8):
        n += 1

    # Построение max-heap.
    for i in range(n, -1, -1):
        heapify(f, n, i)

    # Превращаем дерево в упорядоченный массив
    for i in range(n - 1, 0, -1):
        # Наибольший элемент кучи уходит на своё место в списке
        swap_items(f, i, 0)
        heapify(f, i, 0)
