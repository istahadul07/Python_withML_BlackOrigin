# 1.Write a program to input 2 numbers & print their sum
Var1=int(input("Enter first number :"))
Var2=int(input("Enter second number :"))
print("Result :",Var1+Var2)


# 2.Write a Program to input side of square & print its area
x=int(input("Enter Side Lenght :"))
area=x*x
print("Area :",area)

# 3.Write a Program to input 2 floating point & print their average
a1=float(input("Enter first number: "))
a2=float(input("Enter second number: "))
avg=(a1+a2)/2
print("Average :",avg)

# 4.Write a Program to input 2 int numbers , a and b. Print True if a is greater than or equal to b. if not print False
num1=int(input("Enter Number 1:"))
num2=int(input("Enter Number 2:"))
logic1=(num1>num2)or(num1==num2)
print(logic1)


# 5.Consider the given expression: not True and False or Ture Which of the following will be correct output if the given expression
# is evaluated?
result = not True and False or True
print(result)

# 6. Write a program that asks the user to enter their full name and  prints the number of characters in their name (excluding spaces)
str1=input("Enter your Name: ")
str2=str1.replace(' ','')
x2=len(str2)
print("The length of the name exlcuding space:",x2)

#7.Write a program to count how many times the character  appears in a given string.
str3=input("Enter a string :")
str4=str3.count("#")
print("The number of # in given string :",str4)

#Istahadul Hoque
#CSE-53,7BM[IIUC]
