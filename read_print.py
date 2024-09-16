from struct import pack, unpack


# Функция чтения файла.
def read(f):
    while True:
        try:
            n = int(input('Введите, пожалуйста, размер последовательности: '))
            if 0 > n:
                print('Обратите внимание: размер массива - число неотрицательное.')
                continue
            break
        except ValueError:
                print('Размер последовательности должен являться числовым типом.')
                continue
    for i in range(n):
        while True:
            try:
                number = int(input(f'Введите, пожалуйста, {i}й член последовательности: '))
                if not -2147483648 <= number <= 2147483647:
                    print('Число должно принадлежать отрезку [-2147483648, 2147483647].')
                    continue
                break
            except ValueError:
                print('На вход ожидается число типа int.')
        f.write(pack('q', number))


# Функция распечатки файла.
def print_file(f):
    print('Числа из файла:')
    f.seek(0)
    while bnum := f.read(8):
        print(unpack('q', bnum)[0])
