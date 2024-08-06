def Substitution(text,key):
    """Encrypts the given text using the Ceaser Cipher with the specified key."""
    cipher = ""
    for i in text:
        if i.isspace():
            cipher += " "
        elif i.isalpha():
            c = ord(i) -65
            cipher += chr((c+key)%26 + 65)
        elif i.isalnum():
            c = (int(i) + key)%10
            cipher += str(c)
        else:
            cipher += i
    print("Cipher is: ",cipher)
    return cipher

def DecryptSubstitution(cipher, key):
    """Encrypts the given text using the Ceaser Cipher with the specified key."""
    plaintext = ""
    for i in cipher:
        if i.isspace():
            plaintext += " "
        elif i.isalpha():
            c = ord(i) - 65
            plaintext += chr((c - key) % 26 + 65)
        elif i.isalnum():
            c = (int(i) - key) % 10
            plaintext += str(c)
        else:
            plaintext += i
    print("Plaintext is: ", plaintext)
    return plaintext

plaintext = input("Enter PlainText: ")
key = int(input("Enter Key: "))

ciphertext = Substitution(plaintext.upper(),key)
DecryptSubstitution(ciphertext,key)