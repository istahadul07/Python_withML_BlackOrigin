#conditional Statement

age=int(input("Enter you Age :"))
Legleage=18
if age>=Legleage:
    print("You are eligible for Vote")
else:
    print("You are not eligible")




#whether person is eligible for marraige or not!
gender=input("Enter your gender(m/f):")
age=int(input("Enter you Age :"))
maleage=21
femaleage=18

if gender=="m":
    if age>=maleage:
       print("You are eligible for Marraige")
    else:
        print("You are not eligible for Marraige")
else:
    if age>=femaleage:
         print("You are eligible for Marraige")
    else:
         print("You are not eligible for Marraige")

#question 1

age=int(input("Enter you Age :"))
if age<5:
    print("Free entry!")
elif age<=12:
    print("Child ticket!100 TK")
elif age<=59:
    print("Regular Ticket:250 TK")
else:
    print("Senior Tickket:150 TK")


#triangles
A=int(input("Enter Side A :"))
B=int(input("Enter Side B :"))
C=int(input("Enter Side C :"))
if A==B and A==C:
    print("Equilateral")
elif A==B or A==C or B==C:
    print("Isosceled")
else:
    print("Scalene")


#single line if-else
number=int(input("Enter a number :"))
con=24
print("The number is correct") if number>=con else print("The number is incorrect")

age=int(input("Enter you Age :"))
print("Free entry!" if age < 5 else "Child ticket!100 TK" if age <= 12 else "Regular Ticket:250 TK" if age <= 59 else "Senior Tickket:150 TK")

#
age1=int(input("Enter you Age :"))
result=("Adult","Junior")[age1<12]
print(result)

#lists,tuples,Dictonary and set

# list
agn=[10,20.3,30,40,'tasin',3>4]

print((agn))

# #lenght
print(len(agn))
# #list is an mutable
agn[0]=20
agn[4]='tasfia'
print((agn))

# #slicing
print(agn[1:4])
print(agn[:4])

#methods append[adding a value to list]
list=[10,14,12,12]
list.append("CSE")
print(list)

#reverse the list by reverse() func
list1=[10,14,12,19]
list1.reverse()
print(list1)

#indexing a value to list [specific index]
list2=[13,21,23,42]
list2.insert(2,4)
list2.insert(3,"Tasin")
print(list2)

#pop
list2.pop(2)
print(list2)


#day--03
#Istahadul Hoque,CSE-53 BM
