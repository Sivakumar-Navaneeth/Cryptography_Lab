def Ceaser(text):
    cipher = ""
    for i in text:
        if i.isspace():
            cipher += " "
        elif i.isalpha():
            c = ord(i) -65
            cipher += chr((c+3)%26 + 65)
        elif i.isalnum():
            c = (int(i) + 3)%10
            cipher += str(c)
        else:
            cipher += i
    print("Cipher is: ",cipher)

plaintext = input("Enter PlainText: ")
Ceaser(plaintext.upper())