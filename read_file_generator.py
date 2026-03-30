def read_file(file):

    with open(file, "r") as f:
        for line in f:
            yield line


file_to_read = read_file("./text.txt")

if __name__ == "__main__":
    print(next(file_to_read))
    print(next(file_to_read))
    print(next(file_to_read))
    print(next(file_to_read))
