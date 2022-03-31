from base64 import encode, decode
import hashlib

user_hash = input("Enter the md5 hash :")

try:
    open_file = open(r"passwords_list.txt", "rw")
except:
    print("Invalid file Name")
    quit()

for i in open_file:
    enco = i.encode("utf-8")
    digest = hashlib.md5(enco.strip()).hexdigest()
    if digest == user_hash:
        print("Password Has Found")
        print("Password : "+ i)

    