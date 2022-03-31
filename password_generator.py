# A simple random password generator using random module

import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ01234567890!@#$%^&*()-_+{}[]?<>./|;:,"

user = int(input("Enter the size of Your Password"))

password = "".join(random.sample(characters, user))

print("Your Random Generated Password : ", password)

