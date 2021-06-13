# We start by importing the string module
import string
# Secondly we import everything from the random module
from random import *
# Next we define the characters we will be using in the passwords
# The characters will be derived from the ascii, digits and punctuation strings which were imported
characters = string.ascii_letters + string.digits + string.punctuation
# We generate a password by joining random characters from the stated character domain
# We loop this for the desired amount characters which the password should contain
password = "".join(choice(characters) for x in range(int(input("Please state the desired amount of characters for the password"))))
# At last we return the password to the user
print("This is your password, please store it in a safe place:", password)
