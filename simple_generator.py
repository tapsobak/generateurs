def simple_gen(start, end):
    for num in range(start, end):
        yield (num * (num + 1))


if __name__ == "__main__":
    for num in simple_gen(1, 3):
        print(num)
