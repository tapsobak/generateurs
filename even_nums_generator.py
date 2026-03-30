def even_nums(list_):
    for num in list_:
        if num % 2 == 0:
            yield num


if __name__ == "__main__":
    for even in even_nums([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]):
        print(even)
