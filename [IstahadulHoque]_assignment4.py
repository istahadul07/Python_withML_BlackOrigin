#Problem 1: Print numbers from 100 to 1

i=100
while i>0:
    print(i)
    i-=1
'''
Problem 2: Write a program that takes an integer number from the user and counts how
many digits it has using a while loop.
'''
number=int(input("Enter number :"))
count=0
if number==0:
    count=1
    print(count)
else:
    while number>0:
        number=number//10
        count+=1

    print(count)

'''
 Problem 3: Write a program that asks the user to enter numbers and adds them to a 
 total.Stop the loop when the user enters 0, and then print the total sum
'''
sum=0
while True:
    number1=int(input("Enter number :"))
    if number1==0:
        break
    else:
        sum=sum+number1

print(sum)

'''
Problem 4: Write a program that takes a number from the user and prints its digits in 
reverse order using a while loop
'''
number2=int(input("Enter number :"))
digit=0
while number2>0:
    number3=number2%10
    digit=digit*10+number3
    number2=number2//10
print("Reverse order of given number :",digit)

'''
Problem 5:Print the elements of the following list using a loop:
 [2, 5, 10, 17, 26, 37, 50, 65, 82, 101]
'''
list1=[2, 5, 10, 17, 26, 37, 50, 65, 82, 101]
i=0
while i<len(list1):
    print(list1[i])
    i+=1

'''
Problem 6:Search for a number x in this tuple using loop:
 (3, 6, 9, 12, 15, 18, 21, 24, 27, 30)
'''
tuple1=(3, 6, 9, 12, 15, 18, 21, 24, 27, 30)
x=int(input("Enter the number to search in tuple1 :"))
i=0
count=0
while i<len(tuple1):
    if tuple1[i]==x:
        print(x,"is found in the tuple1")
        count=count+1
        break
    else:
        i += 1
        #print("is not in tuple1")

if count==0:
    print("No number found")

