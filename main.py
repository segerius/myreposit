def plus(a):
    c = []
    for i in range(a):
        c.append(i)
    return c


def minus(a, b):
    return a - b


if __name__ == '__main__':
    print(plus(3))
    print(minus(3, 1))
