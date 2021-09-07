def estimate_value(budget, exchange_rate):
    '''

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return:
    '''

    return budget / exchange_rate

def get_change(budget, exchanging_value):
    '''

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return:
    '''

    return budget - exchanging_value


def get_value(denomination, number_of_bills):
    '''

    :param denomination: int - the value of a bill.
    :param number_of_bills: int amount of bills you received.
    :return:
    '''

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    '''

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return:
    '''

    return int(budget / denomination)


def exchangeable_value(budget, exchange_rate, spread, denomination):
    '''

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return:
    '''
    exchangeable_rate = exchange_rate + spread/100
    return denomination * budget / (exchange_rate)

def unexchangeable_value():
    pass