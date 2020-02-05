import math


def comp(list_a, list_b):
    list_b = list(map(lambda x: int(math.sqrt(x)), list_b))
    for elem in list_b:
        if elem not in list_a:
            return False
    return True


a1 = [121, 144, 19, 161, 19, 144, 19, 11]
a2 = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]

print(comp(a1, a2))
