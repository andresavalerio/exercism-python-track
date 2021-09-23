def is_armstrong_number(number):
    e = len(str(number))
    return number == sum([int(d)**e for d in str(number)])
