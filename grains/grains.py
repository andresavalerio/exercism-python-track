def square(number):
    if number > 64 or number < 1:
        raise ValueError("Value not on the chessboard")
    return 2 ** (number - 1)


def total():
    return sum([square(i) for i in range(1, 65)])
