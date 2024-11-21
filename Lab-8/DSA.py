import random

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def mod_exp(base, exp, mod):
    result = 1
    base = base % mod
    while exp > 0:
        if (exp % 2) == 1:
            result = (result * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return result

def generate_keys():
    q = 191
    p = 383
    g = 2
    x = random.randint(1, q - 1)
    y = mod_exp(g, x, p)

    return (p, q, g, y, x)

def sign(message, p, q, g, x):
    k = random.randint(1, q - 1)
    print("k:", k)

    r = mod_exp(g, k, p) % q
    if r == 0:
        return sign(message, p, q, g, x) 

    H = sum([ord(c) for c in message]) % q

    k_inv = mod_inverse(k, q)
    s = (k_inv * (H + x * r)) % q
    if s == 0:
        return sign(message, p, q, g, x)  

    return (r, s)

def verify(message, signature, p, q, g, y):
    r, s = signature

    if not (0 < r < q and 0 < s < q):
        return False

    H = sum([ord(c) for c in message]) % q
    w = mod_inverse(s, q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    v = ((mod_exp(g, u1, p) * mod_exp(y, u2, p)) % p) % q
    return True


message = "This is a test message"
print("Message:", message)

p, q, g, y, x = generate_keys()

print("Public key (p, q, g, y):", (p, q, g, y))
print("Private key x:", x)

signature = sign(message, p, q, g, x)
print("\nMessage:", message)
print("Signature (r, s):", signature)

is_valid = verify(message, signature, p, q, g, y)
print("\nSignature valid:", is_valid)