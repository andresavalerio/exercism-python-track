def classify(number):
    if number < 1:
        raise ValueError("number not positive")
    f = {1 if number > 1 else 0}
    for n in range(2, int((number**(1/2))+1)):
        if number % n == 0:
            f.add(n)
            f.add(int(number/n))
    sum_f = sum(f)
    return 'perfect' if sum_f == number else \
        ('abundant' if sum_f > number else 'deficient')
