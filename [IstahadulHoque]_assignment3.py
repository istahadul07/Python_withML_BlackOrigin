#Problem 1:Write a program that asks the user to enter the names of their 3 favorite books and store them in a list. Then, print the list
list1=[]
book1=input("Enter the name of first book:")
book2=input("Enter the name of second book:")
book3=input("Enter the name of third book:")

list1=[book1,book2,book3]
print("The book list =",list1)

'''
Problem 2: Write a program to check if a list is the same when reversed (a palindrome). Use the copy() method to create a reversed copy of the list
and compare it with the original.
 ●Example lists to test:
 [4, 5, 6, 5, 4]
 ["hello", "world", "world", "hello"]
'''
list2=["hello", "world", "world", "hello"]
list3=list2.copy() #copy list2 into list3
list3.reverse() #reversed list3

if list2 == list3:
    print("a palindrome")
else:
    print("not a palindrome")

'''
Problem 3:Write a program to count the number of students who received a grade  of "B" in the following tuple:
 ("C", "D", "B", "A", "B", "C", "B", "A") '''
tuple1=("C", "D", "B", "A", "B", "C", "B", "A")
print("The number of students received grade B:",tuple1.count("B"))

'''
Problem 4:Convert the following tuple of student grades into a list and sort the  grades from "A" to "D" in ascending order:
 ("C", "D", "A", "B", "B", "A", "D“)
'''

tuple2=("C", "D", "A", "B", "B", "A", "D")
list2=list(tuple2) #converting tuple into list
list2.sort() #sorting list2
print("Sorted according to ascending order :",list2)

'''
Problem 5: Create a dictionary to store the meanings of the following words:
 "chair" : "a type of seat with four legs"
 "dog" : "a domestic animal, often kept as a pet"
'''

dictornary1={
    "chair": "a type of seat with four legs",
    "dog": "a domestic animal, often kept as a pet",
}
print(dictornary1)

'''
Problem 6: You are given a list of programming languages taken by students. Each unique language requires a separate classroom. Write a program to 
determine the number of classrooms needed.
 ["Python", "Java", "C++", "Python", "JavaScript", 
"Java", "Python", "Java", "C++", "C"]
'''
listR=["Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"]
setR=set(listR) #converting list into set. As set doesn't count duplicate value.
print("Required Classroom for given languages:",len(setR))

'''Problem 7:Write a program that prompts the user to enter marks for three subjects and stores them in a dictionary. The subject names should be used as keys, and 
the marks as values. Print the final dictionary.'''
dictsub={

}
subject1=int(input("Enter marks of subject1 :"))
subject2=int(input("Enter marks of subject2 :"))
subject3=int(input("Enter marks of subject3 :"))

dictsub.update({"obtained marks at Sub1 ":subject1})
dictsub.update({"obtained marks at Sub2 ":subject2})
dictsub.update({"obtained marks at Sub3 ":subject3})
print(dictsub)


'''
Problem 8: Figure out a way to store 9 & 9.0 as separate values in the set.
'''
set={("int",9),("float",9.0)}
print(set)


'''
Assignment 03
Machine learning with python
Istahadul Hoque,CSE-53 BM,IIUC
'''