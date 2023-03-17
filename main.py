import random
print("Welcome")

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+-=[]{};':./<>?"

passwordLength = int(input("Password Length"))

newPassword = []
for x in range(passwordLength):
    newPassword.append(random.choice(characters))

finalPassword = ''.join(map(str, newPassword))
print("Password", finalPassword)
