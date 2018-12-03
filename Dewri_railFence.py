'''
Hello my name is Ethan Dewri. This program will scramble text into a two rail cypher and give enctpted and decrypted
messages.

Scorces :
https://www.youtube.com/watch?v=qOlJwi9mu2Q
https://www.youtube.com/watch?v=uaCumJi4Iuw
'''

choice = input("You shall have the ability to encrypt or decrypt anything thou shall please. Type either 'encrypt' or 'decrypt': ")
plainText = input ("type your message here(make sure you leave no unnessary spaces): ")


def Scramble2Text(plainText):
    evenChars = ''
    oddChars = ''

    charCount = 0
    for ch in plainText:
        if charCount % 2 is 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch

        charCount = charCount + 1

        cipherText = oddChars + evenChars #order of it 
    return cipherText


def decryptMessage (cipherText):
    #this will seperate the two strings
    # // is interger division
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]

    plainText = ''
    
    for i in range (halfLength): #will put two characters together (1 even, 1 odd)
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(evenChars) > len(oddChars): #for uneven total of characters
        plainText = plainText + evenChars [-1]

    return plainText
    plain = Scramble2Text(message)
    print(plain)

if (choice == "encrypt"):
    print(Scramble2Text(plainText))

if (choice == "decrypt"):
    print(decryptMessage(plainText))
