# day 4
# List
lists=["Istahadul Hoque",24,"IIUC",3.62]
lists[1]=23 #mutable
print(lists)
#tuple
tuples=("Virat Kohli",35,"India",17)
print(tuples)
tuples1=(1,2,3)
print(tuples1)
#tuples methods
tup=(2,3,1,1,2)
print(tup.index(3))

#probelm1-store value in list by user input
book1=input("enter the value of book1 :")
book2=input("enter the value of book2 :")
book3=input("enter the value of book3 :")

lists=[book1,book2,book3]
print(lists)

#insert into list
book_list = []
book1 = input("Enter 1st book's name: ")
book2 = input("Enter 2nd book's name: ")
book3 = input("Enter 3rd book's name: ")
book_list.insert(0, book1)
book_list.insert(1, book2)
book_list.insert(2, book3)

print("Book List:",book_list)


#check whether string is palindrome or not.
list3=[1,2,3,2,1]
list4=list3.copy()
list4.reverse()

if list4==list3:
    print("palindrome")
else:
    print("Not palindrome")

#count B in a list
grades = ("C", "D", "B", "A", "B", "C", "B", "A")
tup1=grades.count("A")
print(tup1)

#Sort the list
grades_tuple = ("C", "D", "A", "B", "B", "A", "D")
grades_list = list(grades_tuple)
print(grades_list)
grades_list.sort()
print("Sorted grades from A to D:",grades_list)


#dictonary function "key":"value",
info={
    "name":"Tasin",
    "age":22,
    "gender":"Male",
    "Adult":True,
    "occupation":"studnet",
    "subjects":["Macs","CN","CG","ML","NM"],
    "skills":("Web development","UX-UI design"),

}
#how to edit-using key
info["name"]="istahadul"
print(info)
print(info["Adult"])

#multiple dictonary
studentinfo={
    "name":"Neymar",
    "skill":"Dribbling",
    "age":33,
    "stats" : {
    "goals":"89",
    "assists":"55",
}
}
new_update={
    "club":"barcelona",
    "nationality": "brazilian",
}
studentinfo.update(new_update)
print(studentinfo)
print("goals :",studentinfo["stats"]["goals"])

#sets immutable/unique
set={1,2,3,4,6,None,False,"Istahadul Hoque",1,2,(1,2,3,4),"Istahadul Hoque"}
print(set)
print(type(set))
print(len(set))#duplicate data will not be counted


var={1,2,3,4,5}
var.clear()
print(type(var))
var.add(1)
var.add(2)
var.add(3)
var.pop()
print(var)

set1={1,2,3}
set2={2,3,4,5}
print("union :",set1.union(set2))
print("Intersection :",set1.intersection(set2))
print("Difference:",set1.difference(set2))

# create a dictionary to store the meanings of the following words;
# "chair": "a type of seat with four legs"
# "dog": "a domestic animal, often kept as a pet"
dictonary={
    "chair":"A type of seat with four legs",
    "dog":"a domestic animal, often kept as  a pet"
}
# print(dictonary)
# lista={}
marks ={

}
phy=int(input("Enter phy marks:"))
che=int(input("Enter chem marks:"))
math=int(input("Enter math marks:"))

marks.update({"physics":phy})
marks.update({"chemistry":che})
marks.update({"math":math})
print(marks)

set={("int",9),("float",9.0)}
print(set)

#Istahadul Hoque,CSE-53[BM]