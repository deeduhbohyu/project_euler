def largest_prime_factor():
    return helper(600851475143)

def helper(number):
    smallest_factor = 1

    count = 2
    while count < number:
        if number % count == 0:
            smallest_factor = count
            break
        count = count + 1

    if smallest_factor == 1:
        print number
        return number
    else:
        return helper(number / smallest_factor)

if __name__ == "__main__":
    largest_prime_factor()
