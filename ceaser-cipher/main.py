# Ceaser Cipher
# by CelestialEthan
# April 17, 2020


def menu(title, items):
    """ Displays Menu """
    print(title.center(60, "-"))
# Displays menu options
    for item in items:
        print(item)

    selection = int(input("\nEnter your selection: "))
    return selection


def encrypt():
    """ Encrypts message using provided rotation """
    message = input("Enter a message: ")
    rotation = int(input("Enter a rotation number: "))
    newMessage = translate(message, rotation)
    print("".join(newMessage))

def decrypt():
    message = input("Enter a message: ")
    rotation = int(input("Enter a rotation number or 0 if unknown: "))
    if rotation == 0:
# Runs the decryption 26 times to get all the possibilities 
        for rotation in range(1,26):
            newMessage = translate(message, rotation)
            print(str(rotation) + ". " + "".join(newMessage))      
    else:
# Multiply the rotation by -1 so make in shift backwards
        rotation = rotation * -1
        newMessage = translate(message, rotation)
        print("".join(newMessage))     


# Checks to ensure letter is in alphabet. Adjusts the ordinate depending
# on whether the letter is upper or lower case. Divides the result of the
# letter ordinate, adjustment and rotation by 26 and uses the remainder
# in order loop the alphabet no matter how large the rotation number is 

def translate(message, rotation):
    newMessage = []
    for letter in message:
        if letter.isalpha():
            if letter.isupper():
                adjustment = 65 
            else: 
                adjustment = 97
            letter = (ord(letter) - adjustment + rotation) % 26
            letter = chr(letter + adjustment)
        newMessage.append(letter)
    return newMessage

endProgram = False

while not endProgram:
# what the menu is going to print 
    menuItems = ["1. Encrypt message", "2. Decrypt message", "3. End program"]

    selection = menu("Ceaser Cipher", menuItems)
# Calls the fuction depedning on what the user selects
    if selection == 1:
        encrypt()
    elif selection == 2:
        decrypt()
    else:
        endProgram = True