# A md5 hash code generator using hashlib module

import hashlib

print("\n")
user_pass = input("Enter any Character or string or number : ")
print("\n")

enco = hashlib.md5(user_pass.encode())
res_hash = enco.hexdigest()

print("Your Hash Value : "+ str(hash(user_pass)))
print("\n")
print("Your encoded Hash code : ",res_hash)

print("\n")
print("Your Hash code has been Succesfully generated ")
print("\n")

'''
    Key points :
        encode : coverts string to bytes to an accept hash function
        digext : returns encoded data in byte format
        hexdigest : returns encoded data in hexadigest    
'''