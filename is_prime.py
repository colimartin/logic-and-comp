import math

def is_prime(n):
    for i in range (2, int(n / 2) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    while True:
        n = int(input("> "))
        if n < 2:
            print("False")
        elif is_prime(n):
            print("True")
        else:
            print("False")
