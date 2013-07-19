def smallest_multiple(max_num):
    multiple = 1

    for i in range(2, max_num + 1):
        if multiple % i != 0:
            smallest_prime_factor = get_smallest_prime_factor(i)
            multiple = multiple * smallest_prime_factor

    print multiple



def get_smallest_prime_factor(x):
    for i in range(2, x):
        if x % i == 0:
            return i
    return x


if __name__ == "__main__":
    smallest_multiple(10)
    smallest_multiple(20)
