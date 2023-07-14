import random

def generatePassword(size, haveSpecial):
    
    alphabetUppercase = "ABCDEFGHJKLMNOPQRSTUVWXYZ"
    alphabet = "abcdefghjklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "!@#$%&*"
    newPassword = ""
    
    if haveSpecial:
        typeList = [alphabetUppercase, alphabet, numbers, special]
        for n in range(size):
            typeChar = random.choice(typeList)
            newPassword += random.choice(typeChar)
    else:
        typeList = [alphabetUppercase, alphabet, numbers]
        for n in range(size):
            typeChar = random.choice(typeList)
            newPassword += random.choice(typeChar)
            
    return newPassword

print(generatePassword(16, False))