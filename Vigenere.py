def Vignere(text,key):
    print(text,key)
    cipher = ""
    kl = len(key)
    k = 0
    for i in text:
        if i.isspace():
            cipher += " "
        c = ord(i) - 65
        key1 = ord(key[k]) - 65
        cipher += chr((c+key1)%26 + 65)
        k = (k+1)%kl
    print("Cipher is: ",cipher)

plaintext = input("Enter PlainText: ")
key = input("Key: ")
Vignere(plaintext.upper(),key.upper())