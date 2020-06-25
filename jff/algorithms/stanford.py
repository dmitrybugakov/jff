def multiplication(x, y, n) -> int:
    if n == 1:
        return int(x) * int(y)
    else:
        k: int = n >> 1
        a = x[0:k]
        b = x[k:n]
        c = y[0:k]
        d = y[k:n]

        ac = multiplication(a, c, k)
        ad = multiplication(a, d, k)
        bc = multiplication(b, c, k)
        bd = multiplication(b, d, k)

    return 10 ** n * ac + 10 ** k * (ad + bc) + bd


def karatsuba(x, y, n) -> int:
    if n == 1:
        return int(x) * int(y)
    else:
        k: int = n >> 1
        a = x[0:k]
        b = x[k:n]
        c = y[0:k]
        d = y[k:n]
        p = str(int(a) + int(b))
        q = str(int(c) + int(d))

        ac = karatsuba(a, c, k)
        bd = karatsuba(b, d, k)
        pq = karatsuba(p, q, k)
        adbc = pq - ac - bd

        return 10 ** n * ac + 10 ** k * adbc + bd
