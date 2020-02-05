import math


def strong_num(number):
    list_numbers = [int(i) for i in str(number)]
    result = sum(map(lambda x: math.factorial(x), list_numbers))
    return "STRONG!!!!" if result == number else "Not Strong !!"
