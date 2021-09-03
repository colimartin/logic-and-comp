import math

def is_prime(n):
    i = n - 1
    while (i > 1):
        if n % i == 0:
            return False
        i -= 1
    return True

def prime_factorization(n):
    factors = []
    if is_prime(n):
        return [n]
    i = 2
    while i < n:
        if is_prime(i):
            if n % i == 0:
                factors.append(i)
                n = n / i
                i = 2
            else:
                i += 1
        else:
            i += 1
    factors.append(i)
    return factors

if __name__ == "__main__":
    while True:
        n = int(input("> "))
        print(prime_factorization(n))