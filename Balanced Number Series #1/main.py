def balanced_num(number):
    list_numbs = [int(i) for i in str(number)]
    len_numbs = len(list_numbs)
    print(list_numbs)
    if len_numbs % 2 is not 0:
        middle = int(len_numbs/2)
        return  "Balanced" if sum(list_numbs[0:middle]) is sum(list_numbs[middle + 1:]) else "Not Balanced"
    else:
        first_middle = int(len_numbs/2 - 1)

        return "Balanced" if sum(list_numbs[0:first_middle]) is sum(list_numbs[first_middle + 2:]) else "Not Balanced"

print(balanced_num(959))