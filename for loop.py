#for loop in Python
#Q.1 Write a program to print first ten natural numbers?
for i in range(1,11):
    print(i) 

#Q.2 Write a program to print first 10 even numbers?
for i in range(2,22,2):
    print(i)

#Q.3 Write a program to print first 10 odd numbers?
for i in range(1,20,2):
    print(i)       

#Q.4 Write a program to print first 10 whole numbers?
for i in range(0,10):
    print(i)

#Q.5 Write a program to print square of first 10 natural numbers?
for i in range(1,11):
    print(i**2)   

#Q.6 Write a program to print the square root of every alternate number in the range 1 to 10?
for i in range(1,10,2):
    print(i**0.5)

#Q.7 Write a program to print the following series in the form of a row(in a horizontal way): 10,20,30.....290,3000?
# We need to use end function to print the following series in the form of a row.
for i in range(10,301,10):
    print(i,end=",")

#Q.8 Write a program to print first 10 naturalnumbers in reverse order?
for i in range(10,0,-1):
    print(i)

#Q.9 Write a program to print sum of first ten natural numbers?
sum=0
for i in range(1,11,1):
    sum=sum+i
print(sum)    

#Q.10 Write a program to print the sum of first ten even numbers?
sum=0
for i in range(2,22,2):
    sum=sum+i
print(sum)
 
