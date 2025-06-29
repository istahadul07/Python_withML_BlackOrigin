'''Question 1: Movie Ticket Pricing Based on Age Write a program that takes the user's age and prints the ticket price:
 Age below 5 → "Free entry!"
 Age between 5 and 12 → "Child Ticket: 100 Taka"
 Age between 13 and 59 → "Regular Ticket: 250 Taka"
 Age 60 or above → "Senior Ticket: 150 Taka"
'''

age=int(input("Enter your age: "))
if age<5:
    print("Free entry!")
elif age<13:
    print("Child Ticket: 100 Taka")
elif age<60:
    print("Regular Ticket: 250 Taka")
else:
    print("Senior Ticket: 150 Taka")
'''
Question 2: Water Level Indicator Write a program that asks the user to  enter the current water level in liters.
≥ 100 liters → "Overflow Warning!"
 70–99 liters → "Tank is full."
 30–69 liters → "Tank is half-filled."
 < 30 liters → "Refill the water tank."
'''

waterlevel=int(input("Enter the current water level in liters: "))
if waterlevel>=100:
    print("Overflow Warning!")
elif 70<=waterlevel<100:
    print("Tank is full")
elif 30<=waterlevel<70:
    print("Tank is half-filled")
else:
    print("Refill the water tank.")


'''
Question 3: Determine the Type of Triangle Write a program that takes 
three sides of a triangle and determines its type:
 If all sides are equal → "Equilateral Triangle"
 If any two sides are equal → "Isosceles Triangle"
 If all sides are different → "Scalene Triangle"
'''

sideA=int(input("Enter the side A length of the triangle: "))
sideB=int(input("Enter the side B length of the triangle: "))
sideC=int(input("Enter the side C length of the triangle: "))

if sideA==sideB and sideA==sideC:
    print("Equilateral Triangle")
elif sideA==sideB or sideA==sideC or sideB==sideC:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

'''
Question 4:Write a program that asks the user to enter a number and checks 
whether it is divisible by 2. Print "Divisible by 2" if it is, otherwise print 
"Not Divisible by 2"
'''
number=int(input("Enter a number: "))
if number % 2 == 0:
    print("Divisible by 2")
else:
    print("Not Divisible by 2")
'''
Question 5:Write a program that takes three numbers as input and prints the 
largest among them. If two or more numbers are equal and the 
largest, print "There is a tie"
'''
numA=int(input("Enter  number A: "))
numB=int(input("Enter  number B: "))
numC=int(input("Enter  number C: "))
if (numA==numB and numA==numC and numB==numC):
    print("There is a tie")
elif numA > numB and numA > numC:
    print("The largest number is :",numA)
elif numB > numC and numB > numA:
    print("The largest number is :",numB)
elif numC > numA and numC > numB:
    print("The largest number is :",numC)
else:
    print("There is a tie")

'''
Question 6:Write a program that takes four numbers as input and prints the 
maximum value among them using a built-in function
'''
num1 = int(input("Enter  num1: "))
num2 = int(input("Enter  num2: "))
num3 = int(input("Enter  num3: "))
num4 = int(input("Enter  num4: "))

print("The largest number using built in fucntion (max):",max(num1, num2, num3, num4))
'''
Question 7: Write a program that asks the user to enter a number and checks if 
it is a multiple of 5. Print "Multiple of 5" if it is, otherwise print "Not a 
multiple of 5"
'''
number=int(input("Enter a number: "))
if number%5==0 and number>0:
    print("Multiple of 5")
else:
    print("Not a multiple of 5")


#Istahadul Hoque,CSE-53 BM ,Assignment 02