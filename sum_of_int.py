def sum_of_digits(n):
    if n/10 < 1:
        return n
    else:
        return sum_of_digits(int(n/10))+int(n%10)
    