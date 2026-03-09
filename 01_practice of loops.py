#n = int (input("Enter a Number : "))
#for i in range (1 , 11):
#    print (f"{n} X {i} = {n * i}")

l = ["Ahmad", "Ali", "Ayan", "Faisal", "Ibtahash"]
for name in l :
    if ( name.startswith ("A")):
        print (f"Hi! {name}")

n=int(input("Enter a number : "))
i=1
sum=0
while (i<=n):
    sum+=i
    i+=1
    print (sum)