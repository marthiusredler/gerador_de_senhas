import random

def generatePassword(size: int, haveSpecial: bool):
    """
    That module can generate a new password.
    size: int (number of characters the password must have)
    haveSpecial: bool (whether the generated password can contain special characters)
    """
    
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

if __name__ == "__main__":
    print(generatePassword(16, True))
    