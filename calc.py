x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))
op=input("Enter operation: ") 
if op=="+":
    print(x+y)
elif op=="-":
    print(x-y)
elif op=="*":
    print(x*y)
elif op=="/":
    print(x/y)
else:
    print("invalid option")