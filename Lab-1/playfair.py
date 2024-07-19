def PlayFair(text,key):
    cipher = ""
    dia = []
    duo = ""
    for i in text:
        if duo =="":
            duo += i
        elif (duo == i or (duo =="I" and i =="J") or (duo == "J" and i == "I")):
            duo+="X"
            dia.append(duo)
            duo = i
        else:
            duo += i


plaintext = input("Enter PlainText: ")
key = input("Key: ")
PlayFair(plaintext.upper(),key.upper())

