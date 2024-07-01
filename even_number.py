MAX_NUMBER = int(input("Insert a Range: "))


def even_numbers():
    for i in range(MAX_NUMBER + 1):
        if i % 2 == 0:
            print(i)


even_numbers()
