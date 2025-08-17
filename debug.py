# for testing and debugging code


def count_by(x, n):
    result = []
    for i in range(1, n+1):
        result.append(i * x)
    return result


if __name__ == "__main__":
    x = 2
    n = 5
    print(count_by(x, n))
