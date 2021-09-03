def is_prime(n):
    for i in range (2, int(n / 2) + 1):
        if n % i == 0:
            return False
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