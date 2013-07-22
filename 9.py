def special_pythagorean_triplet(x):

    for a in range(1, x - 1):
        b = (500000 - 1000 * a) / (1000 - a)

        c_squared = a**2 + b**2

        c = 1000 - a - b

        if c_squared == c**2:
            print a*b*c
            return



if __name__ == "__main__":
    special_pythagorean_triplet(1000)
