𝒑𝒓𝒊𝒏𝒕("𝑯𝒆𝒍𝒍𝒐 𝑺𝒕𝒖𝒅𝒆𝒏𝒕! 👋 𝑺𝒖𝒑𝒆𝒓𝒎𝒂𝒏 𝑺𝒆𝒔𝒔𝒊𝒐𝒏 𝑷𝒓𝒐𝒋𝒆𝒄𝒕 1 শুরু হলো")
#𝐏𝐮𝐭𝐭𝐢𝐧𝐠 𝐬𝐢𝐧𝐠𝐥𝐞 𝐃𝐚𝐭𝐚 𝐨𝐟 𝐚 𝐒𝐭𝐮𝐝𝐞𝐧𝐭 (𝐃𝐢𝐜𝐭𝐢𝐨𝐧𝐚𝐫𝐲)
student={
    "name":"Istahadul Hoque",
    "math":87,
    "eng":78,
    "science":89
}
print(student)
print(student["name"])
print(student["math"])

#Putting all students data together (𝐋𝐢𝐬𝐭 𝐨𝐟 𝐃𝐢𝐜𝐭𝐢𝐨𝐧𝐚𝐫𝐢𝐞𝐬)
students=[
    {"name":"Istahadul Hoque",
    "math":87,
    "eng":78,
    "science":89},
{"name":"Rifat",
    "math":86,
    "eng":74,
    "science":81},
{"name":"Rafi",
    "math":77,
    "eng":88,
    "science":91}
]
print("Total Students:",len(students))
print(students)
# 𝐋𝐞𝐭'𝐬 𝐟𝐢𝐠𝐮𝐫𝐞 𝐨𝐮𝐭 𝐓𝐨𝐭𝐚𝐥 𝐌𝐚𝐫𝐤𝐬 𝐨𝐟 𝐞𝐚𝐜𝐡 𝐬𝐭𝐮𝐝𝐞𝐧𝐭𝐬
for x in students:
    x["total"]=x["math"]+x["eng"]+x["science"]
for x in students:
    print(x["name"],"->Total:",x["total"])

#𝐍𝐨𝐰 𝐋𝐞𝐭𝐬 𝐅𝐢𝐧𝐝 𝐎𝐮𝐭 𝐓𝐡𝐞 𝐓𝐨𝐩𝐩𝐞𝐫 (𝐇𝐢𝐠𝐡𝐞𝐬𝐭 𝐭𝐨𝐭𝐚𝐥)
highest=-1
toppper_name=""
for s in students:
    if s["total"]>highest:
        highest=s["total"]
        toppper_name=s["name"]
print("Topper:",toppper_name,"with",highest,"marks")

#𝐋𝐞𝐭'𝐬 𝐏𝐫𝐢𝐧𝐭 𝐎𝐮𝐭 𝐭𝐡𝐞 𝐫𝐞𝐚𝐥 𝐑𝐞𝐩𝐨𝐫𝐭 𝐂𝐚𝐫𝐝
for x in students:
    print("---Report Card---")
    print("Name:",x["name"])
    print("Math:",x["math"])
    print("English:",x["eng"])
    print("Science:",x["science"])
    print("Total:",x["total"])
    print("---------")
print("\nOverall Topper:",toppper_name,"with",highest,"marks")