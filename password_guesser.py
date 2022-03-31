# A password checker/guesser checks the password for its existence

from random import *
# random module is used for the password detection but for a real instance, 
# We can use the hashlib

user = input("Enter Your Password : ")

password = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',0,1,2,3,4,5,6,7,8,9,'!','@','#','$','%','^','&','*',' ','(',')','{','}','[',']','?','-','_','+','>','<','/','|','.']

guess = " "

while(guess != user):
    guess = " "
    for i in range(len(user)):
        guess_word = password[randint(0,58)]
        guess = str(guess_word) + str(guess)
        
        print(guess)

print("your password is ", guess)

# Takes a long time to show the passowrd