import os
from random import randint

# read the password as a string so we can iterate over it
pas = input("Send the Password : ")

keys = ["1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0" , "a" ,
        "b" , "c" , "d" , "e" , "f" , "g" , "h" , "i" , "j" , "k" , "l" ,
        "m" , "n" , "o" , "p" , "q" , "r" , "s" , "t" , "u" , "v", "w" , 
        "x" , "y" , "z"]

pwg = ""
# continue guessing until we match the target password
while pwg != pas:
    pwg = ""
    for i in range(len(pas)):
        # choose a random character from the full key list
        guessPass = keys[randint(0, len(keys) - 1)]
        pwg += guessPass

    # display progress for this attempt
    print(pwg)
    print("attacking.......please wait!")
    os.system("clrs")

print (f"The Pass is : {pwg}")