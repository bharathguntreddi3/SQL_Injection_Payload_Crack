import hashlib

user_pass = input("Enter Any character or String or Number :")

# SHA - Secure Hash Algorithm(SHA) Takes a smaller input and produces a string that is bits, also known as 20-byte has value long
# SHA is the present most used and secure hashing algorithm for crypography and Crypt analytics

md5 = hashlib.md5(user_pass.encode())
sha1 = hashlib.sha1(user_pass.encode())
sha224 = hashlib.sha224(user_pass.encode())
sha256 = hashlib.sha256(user_pass.encode())
sha384 = hashlib.sha384(user_pass.encode())
sha512 = hashlib.sha512(user_pass.encode())

sha3_224 = hashlib.sha3_224(user_pass.encode())
sha3_256 = hashlib.sha3_256(user_pass.encode())
sha3_384 = hashlib.sha3_384(user_pass.encode())
sha3_512 = hashlib.sha3_512(user_pass.encode())

# If you Wanna update the hash data simply you can use 
# hash.update(data)
# data - which data you want yo update with


print("md5 hash Code :", md5.hexdigest())
print("SHA1 hash Code :", sha1.hexdigest())
print("SHA224 hash Code :", sha224.hexdigest())
print("SHA256 hash Code :", sha256.hexdigest())
print("SHA384 hash Code :", sha384.hexdigest())
print("SHA512 hash Code :", sha512.hexdigest())

print("SHA3_224 hash Code :", sha3_224.hexdigest())
print("SHA3_256 hash Code :", sha3_256.hexdigest())
print("SHA3_384 hash Code :", sha3_384.hexdigest())
print("SHA3_512 hash Code :", sha3_512.hexdigest())



# you can loop through the Algorithms

'''

print("\n")
sha_list = [md5, sha1, sha224, sha256, sha384, sha512, sha3_224, sha3_256, sha3_384, sha3_512]
for i in sha_list:
    print(i," hash code ",enco.hexdigest())

'''
