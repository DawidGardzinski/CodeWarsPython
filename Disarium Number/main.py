def disarium_number(number):
    list_number = [int(i) for i in str(number)]
    result = 0
    for i, val in enumerate(list_number):
        result += val ** (i + 1)
    return "Disarium !!" if result == number else "Not !!"

