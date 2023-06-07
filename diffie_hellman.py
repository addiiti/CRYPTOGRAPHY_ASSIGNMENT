import random

def is_prime(n, k=5):
    # Miller-Rabin primality test
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

def is_primitive_root(g, p):
    # Check if g is a primitive root modulo p
    if not is_prime(p):
        return False

    primes = [2]
    for possible_prime in range(3, p - 1, 2):
        if is_prime(possible_prime):
            primes.append(possible_prime)

    for prime in primes:
        if pow(g, (p - 1) // prime, p) == 1:
            return False

    return True

def diffie_hellman(g, p, x, y):
    if not is_prime(p):
        raise ValueError("p is not a prime number")

    if not is_primitive_root(g, p):
        raise ValueError("g is not a primitive root modulo p")

    # Calculate the public keys
    public_key_x = pow(g, x, p)
    public_key_y = pow(g, y, p)

    # Calculate the shared secret keys
    shared_key_x = pow(public_key_y, x, p)
    shared_key_y = pow(public_key_x, y, p)

    return shared_key_x, shared_key_y

# Example usage
g = None
p = None

while True:
    if g is None:
        g = int(input("Enter the generator (g): "))

    if p is None:
        p = int(input("Enter the prime number (p): "))

    if is_prime(p) and is_primitive_root(g, p):
        break
    else:
        print("Invalid values, please try again.")
        g = None
        p = None

x = int(input("Enter the private key for user 1: "))
y = int(input("Enter the private key for user 2: "))

shared_key_1, shared_key_2 = diffie_hellman(g, p, x, y)
print("Shared Key for User 1:", shared_key_1)
print("Shared Key for User 2:", shared_key_2)

print("Key exchange successful!")
