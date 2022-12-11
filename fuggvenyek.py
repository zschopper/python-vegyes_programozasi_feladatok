def primszam(num):
    to = num ** (1 / 2)

    if to == int(to):
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False
    i = 3
    while i <= int(to):
        if num % i == 0:
            return False
        i += 2

    return True
