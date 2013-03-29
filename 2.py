def even_fib():
    second_last = 0
    last = 1

    sum = 0

    current_fib = second_last + last;

    while current_fib < 4000000:

        if current_fib % 2 == 0:
            sum = sum + current_fib

        second_last = last
        last = current_fib
        current_fib = second_last + last;

    print sum


if __name__ == "__main__":
    even_fib()
