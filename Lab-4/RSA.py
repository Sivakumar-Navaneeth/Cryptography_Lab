import random

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def generate_keypair(p, q):
    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = random.randrange(1, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(1, phi)

    # Compute modular inverse of e
    d = pow(e, -1, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = [pow(ord(char), e, n) for char in message]
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_message = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted_message)

# Generate random prime numbers p and q
p = 61
q = 53

# Generate public and private keys
public_key, private_key = generate_keypair(p, q)

message = input("Enter a message: ")
encrypted_message = encrypt(message, public_key)

# Decrypt the encrypted message
decrypted_message = decrypt(encrypted_message, private_key)

print("Encrypted message:", encrypted_message)
print("Decrypted message:", decrypted_message)