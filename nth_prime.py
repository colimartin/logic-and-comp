def is_prime(n):
    i = n - 1
    while (i > 1):
        if n % i == 0:
            return False
        i -= 1
    return True

def nth_prime(n):
    i = 1
    k = 2
    while i < n:
        k += 1
        if is_prime(k):
            i += 1
    return k

if __name__ == "__main__":
    while True:
        n = int(input("> "))
        print(nth_prime(n))