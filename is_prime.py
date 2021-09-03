def is_prime(n):
    i = n - 1
    while (i > 1):
        if n % i == 0:
            return False
        i -= 1
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
