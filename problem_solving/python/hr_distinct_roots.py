def num_distinct_roots(a, b, c):
    discriminant = b ** 2- 4 * a * c
    if discriminant > 0:
        return 2
    elif discriminant < 0:
        return 0
    return 1