factors = ((3, 'Pling'), (5, 'Plang'), (7, 'Plong'))


def convert(number):
    rain = [w for f, w in factors if number % f == 0]
    return "".join(rain) if rain else str(number)
