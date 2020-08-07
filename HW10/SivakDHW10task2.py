def is_prime(number):
    if number > 1:
        for i in range(2, number // 2):
            if (number % i) == 0:
                return False
            return True
    return False
print(is_prime(27))