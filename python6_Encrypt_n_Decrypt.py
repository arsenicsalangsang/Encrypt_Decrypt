#Caesar Cipher

#Encryption
text = input("Enter a single word: ").lower()
number = int(input("Enter the number: "))
code = ""
for ch in text:
    ordVal = ord(ch)
    cipherVal = ordVal + number
    if cipherVal > ord('z'):
        cipherVal = ord('a') + number - (ord('z') - ordVal + 1)
    code += chr(cipherVal)
    #print("ch: ", ch)
    #print("ov: ", ordVal)
    #print("cv: ", cipherVal)
print(code)

#Decryption
code = input("Enter the coded text: ").lower()
number = int(input("Enter the number: "))
text =""
for ch in code:
    ordVal = ord(ch)
    cipherVal = ordVal - number
    if cipherVal < ord('a'):
        cipherVal = ord('z') - (number - (ord('a') - ordVal + 1))
    text += chr(cipherVal)
    #print("ch: ", ch)
    #print("ov: ", ordVal)
    #print("cv: ", cipherVal)

print(text)