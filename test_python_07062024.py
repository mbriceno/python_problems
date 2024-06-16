from functools import reduce
from resource import setrlimit, RLIMIT_AS, getrlimit


def sort_dict() -> dict:

    dict_it = {
        "t": 2,
        "c": 1,
        "e": 40,
        "b": 9
    }
    return dict(sorted(dict_it.items(), key=lambda x: x[1]))


def nearby_zero(ts):

    if not ts:
        return 0

    min_t = -99999
    for t in ts:
        if abs(t) <= abs(min_t):
            min_t = t

    return min_t


def sum_digits(s1: int, s2: int) -> tuple[int, int]:
    return (
        int(reduce(lambda x, y: int(x) + int(y), str(s1))),
        int(reduce(lambda w, z: int(w) + int(z), str(s2)))
    )


def intersection_sum(s1: int, s2:  int) -> int:

    sum_s1, sum_s2 = sum_digits(s1, s2)

    list_s1 = []
    list_s2 = []

    for i in range(0,  20000000):
        s1 = s1 + sum_s1
        list_s1.append(s1)
        s2 = s2 + sum_s2
        list_s2.append(s2)

        if s1 in list_s2:
            return s1

        if s2 in list_s1:
            return s2

        sum_s1, sum_s2 = sum_digits(s1, s2)
    else:
        return 0


if __name__ == '__main__':

    print(sort_dict())

    print(nearby_zero([-3, -4, -15, 3]))
    print(nearby_zero([3, 4, 15, 1]))
    print(nearby_zero([-3, -4, -15, -7]))
    print(nearby_zero([]))
    print(nearby_zero([-234]))
    print(nearby_zero([-3, -4, -15, 1]))

    print(getrlimit(RLIMIT_AS))
    setrlimit(RLIMIT_AS, (512000000, -1))

    try:
        print(intersection_sum(312, 311))
    except Exception as e:
        print(e)
