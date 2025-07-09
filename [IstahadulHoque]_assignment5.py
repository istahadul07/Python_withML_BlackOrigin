#problem 1: Print the elements of the following list using a loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
list1=[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
for x in list1:
    print(x)

#problem 2: Search for a number x in this tuple using loop: (3, 6, 9, 12, 15, 18, 21, 24, 27, 30)
tuple1=(1,4,9,16,25,36,49,64)
num=int(input("Enter number :"))
for x in tuple1:
    if x==num:
        print(x,"is Found")
        break
else:
    print("Not found")

#problem 3 Write a program using for and range() to print all odd numbers between 1 and 50.
for y in range(1,51,2):
    print(y)

#problem 4:Write a program to print numbers starting from 10 up to 100, increasing by 10 each time.
for x1 in range(10,100,10):
    print(x1)

#problem 5:Write a program using for and range() to print numbers from 50 down to 1, decreasing by 5 each time.
for z in range(50,1,-5):
    print(z)

#problem 6:Write a program using a while loop to find the sum of the first n natural numbers, where n is input by the user
number=int(input("Enter a number :"))
i=1
result=0
while i<=number:
    result=result+i
    i=i+1
print(result)

#problem 7: Write a program using a for loop to calculate the factorial of a given number n.
number2=int(input("Enter a number :"))
fact=1
i=number2
while i>0:
    fact=fact*i
    i-=1

print(fact)


#Istahadul Hoque
#CSE 53,BM