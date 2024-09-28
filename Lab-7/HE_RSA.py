import math

p = 11; q = 13

n = p * q
phi = (p-1)*(q-1)
print(f"totient({n}) = {phi}")

# private key - pick a random integer
e = 7
if (math.gcd(e, phi) == 1):
    print(f"{e} is co-prime with {phi}")

d = pow(e, -1, phi)
if ( (e * d) % phi == 1):
    print(f"{d} is the modular inverse of {e} mod {phi}")

# Encryption
message = int(input("Enter the message: "))
cipher = pow(message, e, n)
print(f"Encrypted message: {cipher}")

# Decryption
plain = pow(cipher, d, n)
print(f"Decrypted message: {plain}")

if ( plain == message):
    print("Decryption successful")

m1 = 9
m2 = 11

print(f"Message 1: {m1}")
print(f"Message 2: {m2}")

m1_encrypted = pow(m1, e, n)
m2_encrypted = pow(m2, e, n)

print(f"Encrypted message 1: {m1_encrypted}")
print(f"Encrypted message 2: {m2_encrypted}")

print(f"Product of the messages: {m1*m2}")
print(f"Encrypted product: {(m1_encrypted * m2_encrypted) % n}")
print(f"Decrypted product: {pow(m1*m2, e, n) % n}")


if ( (m1_encrypted * m2_encrypted) % n == pow(m1*m2, e, n) % n):
    print("Homomorphic property holds")