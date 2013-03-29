def sum_square_difference(max_num):

    sum = 0

    for i in range (1, max_num + 1):
        for j in range(i + 1, max_num + 1):
            sum = sum + i * j

    sum = sum * 2

    print sum


if __name__ == "__main__":
    sum_square_difference(100)
