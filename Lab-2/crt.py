from functools import reduce

def chinese_remainder(n, a):
    def extended_gcd(a, b):
        if b == 0:
            return a, 1, 0
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y
    
    def mod_inverse(a, m):
        gcd, x, _ = extended_gcd(a, m)
        if gcd != 1:
            raise ValueError("Inverse doesn't exist")
        return x % m
    
    # Compute the product of all moduli
    prod = reduce(lambda x, y: x * y, n)
    
    # Solve using the CRT formula
    result = 0
    for ni, ai in zip(n, a):
        pi = prod // ni
        inverse = mod_inverse(pi, ni)
        result += ai * pi * inverse
    
    return result % prod

# Example usage
n = [3, 5, 7]  # Moduli (pairwise coprime)
a = [2, 3, 2]  # Remainders

result = chinese_remainder(n, a)
print(f"The solution is x ≡ {result} (mod {reduce(lambda x, y: x * y, n)})")
