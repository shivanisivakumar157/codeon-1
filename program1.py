n=int(input("enter the number"))
n1=0
n2=1
if n==1:
    print(n1)
elif n==2:
     print(n1,n2,end=",") 
else:
    print(n1,n2,end=",") 
    for i in range (n-2):
     n3=n1+n2
     n1=n2
     n2=n3
     print(n3,end=",")
