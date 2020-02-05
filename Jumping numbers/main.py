def jumping_number(number):
    list_numbs = [int(i) for i in str(number)]

    for i in range(len(list_numbs) - 1):
        result = list_numbs[i] - list_numbs[i + 1]
        if (result is not -1) and (result is not 1):
            return "Not!!"
    return "Jumping!!"
    pass


