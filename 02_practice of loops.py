#n = int (input("Enter a Number : "))
#i=1
#while (i<11):
#    print (f"{n} X {i} = {n * i}")
#    i+=1
n = int (input("Enter a Number : "))
for i in range (2 , n):
    if (n%i)==0:
        print ("It is not a prime number.")
        break
    else:
        print ("It is a prime number.")
        break



