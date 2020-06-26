from typing import List


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


def merge_sort(array: List[int]) -> List[int]:
    def merge(left: List[int], right: List[int]) -> List[int]:
        length = len(left) + len(right)
        result: List[int] = list()
        i: int = 0
        j: int = 0
        k: int = 0
        while k < length:
            if (i < len(left)) and (j < len(right)):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                    k += 1
                else:
                    result.append(right[j])
                    j += 1
                    k += 1
            elif i < len(left):
                return result + left[i:len(left)]
            elif j < len(right):
                return result + right[j:len(right)]

        return result

    def sort(array: List[int]) -> List[int]:
        if len(array) == 1:
            return array
        else:
            length = len(array)
            middle = len(array) >> 1
            return merge(sort(array[0:middle]), sort(array[middle:length]))

    return sort(array)
