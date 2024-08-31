def helper():
    upper_bound = 4e6
    res = 0
    a, b = 1, 2
    while b <= upper_bound:
        if b % 2 == 0:
            res += b
        a, b = b, a + b
    return str(res)


if __name__ == "__main__":
    print(helper())
