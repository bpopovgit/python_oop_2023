def print_row(number, row_):
    print(' ' * (number - row_), end='')
    print(*['*'] * row_)


def print_triangle(n):
    for row in range(1, n + 1):
        print_row(n, row)


def print_reverse_triangle(n):
    for row in range(n - 1, 0, -1):
        print_row(n, row)


def create_triangle(n):
    print_triangle(n)
    print_reverse_triangle(n)


create_triangle(int(input()))