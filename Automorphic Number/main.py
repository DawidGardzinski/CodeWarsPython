def automorphic(n):
    return "Automorphic" if int(str(n**2)[-len(str(n)):]) == n else "Not!!"
