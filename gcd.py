def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1

    gcd, s_prev, t_prev = extended_gcd(b % a, a)

    s = t_prev - (b // a) * s_prev
    t = s_prev

    return gcd, s, t

def find_modular_inverse(a, m):
    gcd, s, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist.")
    return s % m

# Example usage
def run_extended_euclidean():
    a = int(input("Enter the value of a: "))
    m = int(input("Enter the value of m: "))

    try:
        modular_inverse = find_modular_inverse(a, m)
        print("Modular inverse of", a, "mod", m, "is", modular_inverse)
    except ValueError as e:
        print("Error:", str(e))

run_extended_euclidean()
