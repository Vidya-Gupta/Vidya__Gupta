#message = input("Enter a message here to encrypt:") 
def encrypt(message):
    encrypt = ''
    for m in message:
        a1 = ord(m)  #string is converted to number
        a2 = a1 + 5  #manupulating the string by adding some secret number
        a3 = chr(a2) #convert the number back to character
        encrypt = encrypt + a3
    return encrypt


#Decryption
#message1 = input("Enter a  message here to encrpt: ")
def decrypt(message1):
    decrypt = ''
    for n in message1:
        a4 = ord(n)
        a5 = a4 - 5
        a6 = chr(a5)
        decrypt = decrypt + a6
    return decrypt

secret = encrypt("Do not hack my password")
print(secret)
notsecret = decrypt("it%sty%mfhp%r%ruf")
print(notsecret)
