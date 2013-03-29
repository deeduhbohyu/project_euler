def sum_of_multiples():
    sum = 0
    cur_multiple = 0
    multiple = 3

    while cur_multiple < 1000:
        cur_multiple = cur_multiple + multiple
        sum = sum + cur_multiple

    cur_multiple = 0
    multiple = 5
    
    while cur_multiple < 1000:
        cur_multiple = cur_multiple + multiple
        sum = sum + cur_multiple

    print sum

def sum_of_multiples_dw():
        
    sum = 0
    cur_multiple = 0
    multiple = 3

    for i in range(0, 1000):
        if i % 3 == 0 or i % 5 == 0:
            sum = sum + i
    print sum 

if __name__ == "__main__":
    sum_of_multiples()
    sum_of_multiples_dw()
