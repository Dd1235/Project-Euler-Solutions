def helper():
    return sum(i if (i % 3 == 0 or i % 5 == 0) else 0 for i in range(1, 1000))


if __name__ == "__main__":
    print(helper())
