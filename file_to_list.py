# Стоит отметить, что доступна и отрицательная индексация)

# Функция получения элемента по индексу.
def get_item(f, ind):
    # Рассматриваются случаи,
    # когда какие знаки у индексов,
    # чтобы обеспечить отрицательную индексацию.
    if ind >= 0:
        f.seek(ind * 8)
    else:
        f.seek(ind * 8, 2)
    return f.read(8)


# Функция swap.
def swap_items(f, ind1, ind2):
    # Рассматриваются случаи,
    # когда какие знаки у индексов,
    # чтобы обеспечить отрицательную индексацию.
    if ind1 < 0 and not ind2 < 0:
        f.seek(8 * (ind1 + 1), 2)
        a = f.read(8)
        f.seek(8 * ind2)
        b = f.read(8)
        f.seek(-8, 1)
        f.write(a)
        f.seek(8 * ind1, 2)
        f.write(b)
        return
    if ind2 < 0 and not ind1 < 0:
        f.seek(8 * ind1)
        a = f.read(8)
        f.seek(8 * ind2, 2)
        b = f.read(8)
        f.seek(-8, 1)
        f.write(a)
        f.seek(8 * ind1)
        f.write(b)
        return
    if ind2 < 0 and ind1 < 0:
        f.seek(8 * (ind1 + 1), 2)
        a = f.read(8)
        f.seek(8 * ind2, 2)
        b = f.read(8)
        f.seek(-8, 1)
        f.write(a)
        f.seek(8 * ind1, 2)
        f.write(b)
        return
    else:
        f.seek(8 * ind1)
        a = f.read(8)
        f.seek(8 * ind2)
        b = f.read(8)
        f.seek(-8, 1)
        f.write(a)
        f.seek(8 * ind1)
        f.write(b)
        return
