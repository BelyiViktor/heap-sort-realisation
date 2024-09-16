# Белый Виктор, группа ИУ7-15Б МГТУ им. Баумана
# Программа реализует вставку после элементов,
# делящихся на 3, удвоенного значения этих элементов.


from read_print import *

# Подключим реализацию heap sort на бинарном файле.
from heapsort import *


def main():
    with open('numbers.bin', 'wb+') as f:
        read(f)
        heap_sort(f)
        print_file(f)


main()
