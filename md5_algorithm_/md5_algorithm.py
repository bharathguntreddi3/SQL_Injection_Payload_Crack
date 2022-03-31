# cracking passwords by md5 hashes using md5 Algorithm

import hashlib
import time
import sys
import os

print("\n")
tup_time = time.localtime() # get struct_time
current_time = time.asctime(tup_time)
print("Your Current Time & Date is ",current_time)

# current_time = time.strftime("%m/%d/%Y, %H:%M:%S", tup_time) 
# print(current_time)      

print("\n")

# Hash : The hash value is an integer which is used to quickly compare dictionary keys while looking at a dictionary.
# Hashing : The Hashing is the method of converting a data of any size into a fixed length.Hasing used to Encrypt a password.
'''
    Key points :
        encode : coverts string to bytes to an accept hash function
        digext : returns encoded data in byte format
        hexdigest : returns encoded data in hexadigest    
'''
user_hash = input("Enter the md5 hash :")
# passwords_list = input("Enter the passwords file : ")
temp = 0

try:
    open_file = open(r"passwords_list.txt", "r")
except:
    print("Invalid file Name")
    quit()

for i in open_file:
    enco = i.encode("utf-8")
    digest = hashlib.md5(enco.strip()).hexdigest() # converted to hexadigest form
    print(i)
    
    if digest == user_hash:
        print("Password Has Found : ", i)
        temp = 1
        break
if temp == 0:
    print("Password Has not Found ")
    