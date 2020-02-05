def digital_root(n):
    if n < 10:
        return n
    else:
        list_n = [int(i) for i in str(n)]
        return digital_root(sum(list_n))
