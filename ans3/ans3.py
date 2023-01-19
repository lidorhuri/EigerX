def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        x = n % 10
        return x + sum_of_digits(n //10)

print(sum_of_digits(2347623))