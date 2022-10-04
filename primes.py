"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("Parameter must be positive.")

    list = []
    count = 0
    num = 3
    
    list.append(2)

    while count < number_of_primes - 1:
        if is_prime(num):
            list.append(num)
            count += 1
        num += 1

    return list

def is_prime(num):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True