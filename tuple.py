#tuple=collection which is ordered and unchangeable
#       used to group together related data

student=("Bro","male","21")

print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here!")